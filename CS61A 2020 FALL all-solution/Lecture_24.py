l1 = [-4, -3, -2 ,3 ,2, 4, -2, 33, 23]
l2 = [1, 2, 3, 4, 5,1,2,3,4,5]

def min_abs_indices(s):
	abs_min = min(map(abs, s))
	return [i for i in range(len(s)) if abs(s[i]) == abs_min]

def large_adj_sum(s):
	max_list = [s[i] + s[i+1] for i in range(len(s)-1)]
	return max(max_list)

def map_dict(s):
	return {d:[x for x in s if x%10 == d] for d in range(10) if d in [x%10 for x in s]}

def all_have_any_equal(s):
	return min([s.count(x) for x in s]) > 1
