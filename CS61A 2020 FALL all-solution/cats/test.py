from functools import reduce
s = lambda x : x < 5
a = filter(s , range(2, 23))
def cube(x,y):
	return x*x
b = reduce(cube, [2,3,4,5])

print_progress = lambda d: print('ID:', d['id'], 'Progress:', d['progress'])
print_progress({'id': 1, 'progress': 0.6})
