def memory(n):
	"""
	>>> f = memory(10)
	>>> f(lambda x: x * 2)
	20
	>>> f(lambda x: x - 7)
	13
	>>> f(lambda x: x > 5)
	True
	"""
	def f(g):
		nonlocal n
		n = g(n)
		return n
	return f

def mystery(p,q):
	p[1].extend(q)
	q.append(p[1:])

p = [2, 3]
q = [4, [p]]
mystery(q, p)
print(p)
print(q)

def add_this_many(x, el, s):
	""" Adds el to the end of s the number of times x occurs
	in s.
	>>> s = [1, 2, 4, 2, 1]
	>>> add_this_many(1, 5, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5]
	>>> add_this_many(2, 2, s)
	>>> s
	[1, 2, 4, 2, 1, 5, 5, 2, 2]
	"""
	s1 = s[:]
	for y in s1:
		if x == y:
			s.append(el)


def filter(iterable, fn):
	"""
	>>> is_even = lambda x: x % 2 == 0
	>>> list(filter(range(5), is_even)) # a list of the values yielded from the call to filter
	[0, 2, 4]
	>>> all_odd = (2*y-1 for y in range (5))
	>>> list(filter(all_odd, is_even))
	[]
	>>> def naturals():
	... 	i = 0
	... 	while True:
	... 		i += 1 
	... 		yield i
	>>> s = filter(naturals(), is_even)
	>>> next(s)
	2
	>>> next(s)
	4
	"""
	for i in iterable:
		if fn(i):
			yield i



def merge(a, b):
	"""
	>>> def sequence(start, step):
	... 	while True:
	... 		yield start
	... 		start += step
	>>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
	>>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
	>>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
	>>> [next(result) for _ in range(10)]
	[2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
	"""
	i = next(a) # 将 yield value bind to i, j to yield a or b once when compared ,expected i == j.
	j = next(b)
	while True:
		if i > j:
			yield j
			j = next(b)
		elif i == j:
			yield j 
			i = next(a)
			j = next(b)
		elif i < j:
			yield i
			i = next(a)


# def sequence(start, step):
# 	while True:
# 		yield start
# 		start += step

# a = sequence(2, 3)
# b = sequence(3, 2)
# result = merge(a, b)
# print([next(result) for _ in range(10)])

