import ast

from .group_similar_constructs import GroupSimilarConstructsVisitor

class GetAllNodes(ast.NodeVisitor):
    def __init__(self):
        self.nodes = []
    def generic_visit(self, node):
        self.nodes.append(node)
        super().generic_visit(node)

def get_all_nodes(node):
    getter = GetAllNodes()
    getter.visit(node)
    return [subnode for subnode in getter.nodes if subnode is not node]

class GetName(GroupSimilarConstructsVisitor):
    def __init__(self):
        self.name = None
    def visit_Name(self, node):
        self.name = node.id
    def visit_function_def(self, func_node, is_async):
        self.name = func_node.name
    def visit_ClassDef(self, class_node):
        self.name = class_node.name
    def visit_alias(self, alias_node):
        self.name = name_of_alias(alias_node)

def get_name(node):
    getter = GetName()
    getter.visit(node)
    assert getter.name is not None
    return getter.name

def name_of_alias(alias_node):
    if alias_node.asname is not None:
        return alias_node.asname
    return alias_node.name
