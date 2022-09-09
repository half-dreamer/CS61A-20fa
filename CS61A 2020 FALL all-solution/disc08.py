#没有对答案


class A():
	def __init__(self, x):
		self.x = x
	def __repr__(self):
		return self.x
	def __str__(self):
		return self.x * 2
class B():
	def __init__(self):
		print("boo!")
		self.a = []
	def add_a(self, a):
		self.a.append(a)
	def __repr__(self):
		print(len(self.a))
		ret = ""
		for a in self.a:
			ret += str(a)
		return ret

class Test:
	def __str__(self):
		return "str1"
	def __repr__(self):
		return "repr1"



def sum_nums(lnk):
	"""
	>>> a = Link(1, Link(6, Link(7)))
	>>> sum_nums(a)
	14
	"""
	if lnk is Link.empty:
		return 0
	return lnk.first + sum_nums(lnk.rest)

def multiply_lnks(lst_of_lnks): 
	"""
	>>> a = Link(2, Link(3, Link(5)))
	>>> b = Link(6, Link(4, Link(2)))
	>>> c = Link(4, Link(1, Link(0, Link(2))))
	>>> p = multiply_lnks([a, b, c])
	>>> p.first
	48
	>>> p.rest.first
	12
	>>> p.rest.rest.rest is Link.empty
	True
	"""
	total_label = 1
	for lnk in lst_of_lnks:
		if lnk is Link.empty:
			return Link.empty
		total_label *= lnk.first
	return Link(total_label, multiply_lnks([lnk.rest for lnk in lst_of_lnks]))
	


def flip_two(lnk):
	"""
	>>> one_lnk = Link(1)
	>>> flip_two(one_lnk)
	>>> one_lnk
	Link(1)
	>>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
	>>> flip_two(lnk)
	>>> lnk
	Link(2, Link(1, Link(4, Link(3, Link(5)))))
	"""
	if lnk.rest == Link.empty:
		return
	else:
		while lnk.rest != Link.empty:
			lnk.first, lnk.rest.first = lnk.rest.first, lnk.first
			lnk = lnk.rest.rest

def filter_link(link, f):
	"""
	>>> link = Link(1, Link(2, Link(3)))
	>>> g = filter_link(link, lambda x: x % 2 == 0)
	>>> next(g)
	2
	>>> next(g)
	StopIteration
	>>> list(filter_link(link, lambda x: x % 2 != 0))
	[1, 3]
	"""
	while link is not Link.empty:
		if f(link.first):
			yield link.first
		link = link.rest


def make_even(t):
	"""
	>>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
	>>> make_even(t)
	>>> t.label
	2
	>>> t.branches[0].branches[0].label
	4
	"""
	def odd_plus_one(n):
		if n % 2 == 0:
			return n
		else:
			return n + 1

	if t.is_leaf():
		t.label = odd_plus_one(t.label)
	else:
		t.label = odd_plus_one(t.label)
		for b in t.branches:
			make_even(b)

def square_tree(t):
	"""Mutates a Tree t by squaring all its elements."""

	t.label = t.label * t.label
	for b in t.branches:
		square_tree(b)


def combine_tree(t1, t2, combiner):
	"""
	>>> from operator import mul
	>>> a = Tree(1, [Tree(2, [Tree(3)])])
	>>> b = Tree(4, [Tree(5, [Tree(6)])])
	>>> combined = combine_tree(a, b, mul)
	>>> combined.label
	4
	>>> combined.branches[0].label
	10
	"""
	if t1.is_leaf() and t2.is_leaf:
		return Tree(combiner(t1.label, t2.label))
	else:
		return Tree(combiner(t1.label, t2.label), [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)])


def alt_tree_map(t, map_fn):
	"""
	>>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
	>>> negate = lambda x: -x
	>>> alt_tree_map(t, negate)
	Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
	"""
	def f(t, map_fn, x):
		if x == 0 :
			return Tree(map_fn(t.label), [f(b, map_fn, x=1) for b in t.branches])
		if x == 1:
			return Tree(t.label, [f(b, map_fn, x =0) for b in t.branches])
		

	return f(t, map_fn, x=0)

def find_paths(t, entry):
	"""
	>>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
	>>> find_paths(tree_ex, 5)
	[[2, 7, 6, 5], [2, 1, 5]]
	>>> find_paths(tree_ex, 12)
	[]
	"""
	paths = []
	if t.label == entry:
		paths.append([t.label])
	for b in t.branches:
		for path in find_paths(b, entry):
			paths.append([t.label] + path)
	return paths
	
		
	



class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'


class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

