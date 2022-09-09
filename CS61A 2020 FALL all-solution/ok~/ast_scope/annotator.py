
import ast
import abc

from .group_similar_constructs import GroupSimilarConstructsVisitor
from .utils import name_of_alias

class IntermediateScope(abc.ABC):
    """
    Represents a scope for the purposes of the annotator object. This isn't actually a scope but something from which
        scope can be deduced.
    """
    def __init__(self):
        self.referenced_variables = set()
        self.written_variables = set()
        self.nonlocal_variables = set()
        self.global_variables = set()

    def load(self, variable):
        self.referenced_variables.add(variable)

    def modify(self, variable):
        self.written_variables.add(variable)

    def globalize(self, variable):
        self.global_variables.add(variable)

    def nonlocalize(self, variable):
        self.nonlocal_variables.add(variable)

    @abc.abstractmethod
    def global_frame(self):
        pass

    @abc.abstractmethod
    def find(self, name, global_acceptable=True):
        """
        Finds the actual frame containing the variable name, or None if no frame exists
        """
        pass

    def true_parent(self):
        parent = self.parent
        while isinstance(parent, IntermediateClassScope):
            parent = parent.parent
        return parent

class IntermediateGlobalScope(IntermediateScope):
    def find(self, name, is_assignment, global_acceptable=True):
        if not global_acceptable:
            return None
        return self

    def global_frame(self):
        return self

class IntermediateFunctionScope(IntermediateScope):
    def __init__(self, node, parent):
        super().__init__()
        self.node = node
        self.parent = parent

    def global_frame(self):
        return self.true_parent().global_frame()

    def find(self, name, is_assignment, global_acceptable=True):
        if name in self.global_variables:
            return self.global_frame()
        if name in self.nonlocal_variables:
            return self.true_parent().find(name, is_assignment, global_acceptable=False)
        if name in self.written_variables:
            return self
        return self.true_parent().find(name, is_assignment, global_acceptable)


class IntermediateClassScope(IntermediateScope):
    def __init__(self, node, parent, class_binds_near):
        super().__init__()
        self.node = node
        self.parent = parent
        self.class_binds_near = class_binds_near
    def global_frame(self):
        return self.true_parent().find(self)
    def find(self, name, is_assignment, global_acceptable=True):
        if self.class_binds_near:
            # anything can be in a class frame
            return self
        if is_assignment:
            return self
        return self.parent.find(name, is_assignment, global_acceptable)

class GrabVariable(ast.NodeVisitor):
    """
    Dumps variables from a given name object into the given scope.
    """
    def __init__(self, scope, variable, annotation_dict):
        self.scope = scope
        self.variable = variable
        self.annotation_dict = annotation_dict

    def visit_generic(self, node):
        raise RuntimeError("Unsupported node type: {node}".format(node=node))

    def visit_Name(self, node):
        super().visit_generic(node)

    def load(self):
        self.annotation_dict[self.variable] = self.variable.id, self.scope, False
        self.scope.load(self.variable.id)

    def modify(self):
        self.annotation_dict[self.variable] = self.variable.id, self.scope, True
        self.scope.modify(self.variable.id)

    def visit_Load(self, _):
        self.load()

    def visit_Store(self, _):
        self.modify()

    def visit_Del(self, _):
        self.modify()

    def visit_AugLoad(self, _):
        raise RuntimeError("Unsupported: AugStore")

    def visit_AugStore(self, _):
        raise RuntimeError("Unsupported: AugStore")

class ProcessArguments(ast.NodeVisitor):
    def __init__(self, expr_scope, arg_scope):
        self.expr_scope = expr_scope
        self.arg_scope = arg_scope

    def visit_arg(self, node):
        self.arg_scope.visit(node)
        visit_all(self.expr_scope, node.annotation, getattr(node, 'type_comment', None))

    def visit_arguments(self, node):
        super().generic_visit(node)

    def generic_visit(self, node):
        self.expr_scope.visit(node)

class AnnotateScope(GroupSimilarConstructsVisitor):
    def __init__(self, scope, annotation_dict, class_binds_near):
        self.scope = scope
        self.annotation_dict = annotation_dict
        self.class_binds_near = class_binds_near

    def annotate_intermediate_scope(self, node, name, is_assign):
        self.annotation_dict[node] = name, self.scope, is_assign

    def visit_Name(self, name_node):
        GrabVariable(self.scope, name_node, self.annotation_dict).generic_visit(name_node)

    def visit_alias(self, alias_node):
        variable = name_of_alias(alias_node)
        self.annotate_intermediate_scope(alias_node, variable, True)
        self.scope.modify(variable)

    def visit_arg(self, arg):
        self.annotate_intermediate_scope(arg, arg.arg, True)
        self.scope.modify(arg.arg)

    def create_subannotator(self, scope):
        return AnnotateScope(scope, self.annotation_dict, self.class_binds_near)

    def visit_function_def(self, func_node, is_async):
        del is_async
        self.annotate_intermediate_scope(func_node, func_node.name, True)
        self.scope.modify(func_node.name)
        subscope = self.create_subannotator(IntermediateFunctionScope(func_node, self.scope))
        visit_all(self, getattr(func_node, 'type_comment', None), func_node.decorator_list)
        ProcessArguments(self, subscope).visit(func_node.args)
        visit_all(subscope, func_node.body, func_node.returns)

    def visit_Lambda(self, func_node):
        self.annotate_intermediate_scope(func_node, '<lambda>', None)
        subscope = self.create_subannotator(IntermediateFunctionScope(func_node, self.scope))
        ProcessArguments(self, subscope).visit(func_node.args)
        visit_all(subscope, func_node.body)

    def visit_comprehension_generic(self, targets, comprehensions, typ):
        del typ
        current_scope = self
        for comprehension in comprehensions:
            self.annotate_intermediate_scope(comprehension, '<comp>', None)
            subscope = self.create_subannotator(IntermediateFunctionScope(comprehension, current_scope.scope))
            visit_all(current_scope, comprehension.iter)
            visit_all(subscope, comprehension.target, comprehension.ifs)
            current_scope = subscope
        visit_all(current_scope, targets)

    def visit_ClassDef(self, class_node):
        self.annotate_intermediate_scope(class_node, class_node.name, True)
        self.scope.modify(class_node.name)
        subscope = self.create_subannotator(IntermediateClassScope(class_node, self.scope, self.class_binds_near))
        ast.NodeVisitor.generic_visit(subscope, class_node)

    def visit_Global(self, global_node):
        for name in global_node.names:
            self.scope.globalize(name)

    def visit_Nonlocal(self, nonlocal_node):
        for name in nonlocal_node.names:
            self.scope.nonlocalize(name)

def visit_all(visitor, *nodes):
    for node in nodes:
        if node is None:
            pass
        elif isinstance(node, list):
            visit_all(visitor, *node)
        else:
            visitor.visit(node)
