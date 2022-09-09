import ast

class GroupSimilarConstructsVisitor(ast.NodeVisitor):
    def visit_function_def(self, func_node, is_async):
        return self.generic_visit(func_node)

    def visit_FunctionDef(self, func_node):
        return self.visit_function_def(func_node, is_async=False)

    def visit_AsyncFunctionDef(self, func_node):
        return self.visit_function_def(func_node, is_async=True)

    def visit_comprehension_generic(self, targets, comprehensions, node):
        return self.generic_visit(node)

    def visit_DictComp(self, comp_node):
        return self.visit_comprehension_generic([comp_node.key, comp_node.value], comp_node.generators, comp_node)

    def visit_ListComp(self, comp_node):
        return self.visit_comprehension_generic([comp_node.elt], comp_node.generators, comp_node)

    def visit_SetComp(self, comp_node):
        return self.visit_comprehension_generic([comp_node.elt], comp_node.generators, comp_node)

    def visit_GeneratorExp(self, comp_node):
        return self.visit_comprehension_generic([comp_node.elt], comp_node.generators, comp_node)
