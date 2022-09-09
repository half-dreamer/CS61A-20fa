
from .annotator import AnnotateScope, IntermediateGlobalScope
from .pull_scope import PullScopes
from .utils import get_all_nodes, get_name
from .graph import DiGraph

class ScopeInfo:
    def __init__(self, tree, global_scope, error_scope, node_to_containing_scope):
        self._tree = tree
        self._global_scope = global_scope
        self._error_scope = error_scope
        self._node_to_containing_scope = node_to_containing_scope

    @property
    def global_scope(self):
        return self._global_scope

    @property
    def static_dependency_graph(self):
        """
        Returns a static dependency graph of all the top-level functions and classes in the
            given piece of code.

        Note: this function assumes all top level code is original definitions
            and thus does not handle reassignment of functions or classes, or
            any other variables.
        """
        variables = self.global_scope.symbols_in_frame
        g = DiGraph()
        g.add_nodes_from(variables)
        varis = self.global_scope.variables
        for construct in varis.functions | varis.classes:
            for node in get_all_nodes(construct):
                if node not in self:
                    continue
                if self[node] is not self._global_scope:
                    continue
                g.add_edge(get_name(construct), get_name(node))
        return g

    def __contains__(self, node):
        return node in self._node_to_containing_scope

    def __getitem__(self, node):
        return self._node_to_containing_scope[node]

def annotate(tree, class_binds_near=False):
    annotation_dict = {}
    annotator = AnnotateScope(IntermediateGlobalScope(), annotation_dict, class_binds_near=class_binds_near)
    annotator.visit(tree)

    pull_scopes = PullScopes(annotation_dict)
    pull_scopes.visit(tree)
    return ScopeInfo(tree, pull_scopes.global_scope, pull_scopes.error_scope, pull_scopes.node_to_containing_scope)
