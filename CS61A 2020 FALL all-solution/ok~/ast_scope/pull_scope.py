import ast

from .scope import GlobalScope, ErrorScope, FunctionScope, ClassScope
from .annotator import IntermediateGlobalScope, IntermediateFunctionScope, IntermediateClassScope, visit_all
from .group_similar_constructs import GroupSimilarConstructsVisitor

class PullScopes(GroupSimilarConstructsVisitor):
    def __init__(self, annotation_dict):
        self.annotation_dict = annotation_dict
        self.node_to_corresponding_scope = {}
        self.node_to_containing_scope = {}
        self.global_scope = GlobalScope()
        self.error_scope = ErrorScope()

    def convert(self, int_scope):
        if int_scope is None:
            return self.error_scope
        if isinstance(int_scope, IntermediateGlobalScope):
            return self.global_scope
        return self.node_to_corresponding_scope[int_scope.node]

    def pull_scope(self, node, include_as_variable=True):
        name, intermediate_scope, is_assign = self.annotation_dict[node]
        true_intermediate_scope = intermediate_scope.find(name, is_assign)
        scope = self.convert(true_intermediate_scope)
        if include_as_variable:
            self.node_to_containing_scope[node] = scope
        return scope

    def visit_Name(self, node):
        scope = self.pull_scope(node)
        scope.add_variable(node)
        super().generic_visit(node)

    def visit_arg(self, node):
        scope = self.pull_scope(node)
        scope.add_variable(node)
        super().generic_visit(node)

    def visit_alias(self, node):
        scope = self.pull_scope(node)
        scope.add_import(node)
        super().generic_visit(node)

    def visit_function_def(self, node, is_async):
        del is_async
        scope = self.pull_scope(node)
        if node not in self.node_to_corresponding_scope:
            self.node_to_corresponding_scope[node] = FunctionScope(node, scope)
        scope.add_function(node, self.node_to_corresponding_scope[node], include_as_variable=True)
        super().generic_visit(node)

    def visit_Lambda(self, node):
        scope = self.pull_scope(node, include_as_variable=False)
        if node not in self.node_to_corresponding_scope:
            self.node_to_corresponding_scope[node] = FunctionScope(node, scope)
        scope.add_function(node, self.node_to_corresponding_scope[node], include_as_variable=False)
        super().generic_visit(node)

    def visit_comprehension_generic(self, targets, comprehensions, node):
        # mate sure to visit the comprehensions first
        visit_all(self, comprehensions)
        visit_all(self, targets)

    def visit_comprehension(self, node):
        scope = self.pull_scope(node, include_as_variable=False)
        if node not in self.node_to_corresponding_scope:
            self.node_to_corresponding_scope[node] = FunctionScope(node, scope)
        scope.add_function(node, self.node_to_corresponding_scope[node], include_as_variable=False)
        super().generic_visit(node)

    def visit_ClassDef(self, node):
        scope = self.pull_scope(node)
        if node not in self.node_to_corresponding_scope:
            self.node_to_corresponding_scope[node] = ClassScope(node, scope)
        scope.add_class(node, self.node_to_corresponding_scope[node])
        super().generic_visit(node)
