class EulerTour:
    def __init__(self, tree):
        self._tree = tree

    @property
    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree(), 0, [])

    def _tour(self, p, d, path):
        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        pass

    def _hook_postvisit(self, p, d, path, results):
        pass


class PreorderPrintIndentedLabeledTour(EulerTour):
    """
    A subclass of EulerTour that produces a labeled and indented, preorder list of tree's element.
    """

    def _hook_previsit(self, p, d, path):
        label = ".".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


class ParenthesizeTour(EulerTour):
    """
    A subclass of a EulerTour that prints a parenthetic string representation of a tree
    """

    def _hook_previsit(self, p, d, path):
        if path and path[-1] > 0:
            print(", ", end="")
        print(p.element(), end="")
        if not self.tree().is_leaf(p):
            print(" (", end="")

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(")", end="")


class DiskSpaceTour(EulerTour):
    """
    A subclass of EulerTour that computes disk space for a tree
    """

    def _hook_postvisit(self, p, d, path, results):
        return p.element().space() + sum(results)
