class Pair:
	"""Represents the built-in pair data structure in scheme."""
	def __init__(self, first, rest):
		self.first = first
		# if not scheme_valid_cdrp(rest):
		# 	raise("cdr can only be a pair, nil, or a promise but was {}".format(rest))
		self.rest = rest

	def map(self, fn):
		"""map fn to every element in the list, and return a new Pair.
		>>> Pair(1, Pair(2, Pair(3, nil))).map(lambda x: x * x)
			Pair(1, Pair(4, Pair(9, nil)))
		"""
		assert isinstance(self.rest, Pair) or self.rest is nil, "rest element must be a Pair or nil"
		return Pair(fn(self.first), self.rest.map(fn))

	def __repr__(self):
		return "Pair({}, {})".format(self.first, self.rest)

class nil:
	"""Represents the special empty pair nil in scheme"""
	def map(self, fn):
		return nil

	def __repr__(self):
		return 'nil'

	def __getitem__(self, i):
		raise IndexError("Index out of range")

def calc_eval(exp):
	"""Evaulate a Calculator expression represented as a Pair"""
	if isinstance(exp, Pair):
		fn = calc_eval(exp.first)
		args = list(exp.rest.map(calc_eval))
		return calc_apply(fn, args)
	elif exp in OPERATORS:
		return OPERATORS[exp]
	else:
		return exp

def calc_apply(fn, args):
	"""Applies a Calculator operation to a list of numbers"""
	return fn(args)


(and (= 1 1) 3)

nil = nil()
print(Pair(1, Pair(2,Pair(3, nil))).map(lambda x : x**3))
