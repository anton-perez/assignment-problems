def intersection(list_1, list_2):
  intersection_list = list(set(list_1) & set(list_2))
  intersection_nums = sorted([i for i in intersection_list if type(i) is int])
  intersection_strs = sorted([i for i in intersection_list if type(i) is str])

  return intersection_nums + intersection_strs


def union(list_1, list_2):
  union_list = list(set(list_1) | set(list_2))
  union_nums = sorted([i for i in union_list if type(i) is int])
  union_strs = sorted([i for i in union_list if type(i) is str])

  return union_nums + union_strs

print("testing intersection on inputs [1, 2, 'a', 'b'], [2, 3, 'a']...")
assert intersection([1, 2, 'a', 'b'], [2, 3, 'a']) == [2, 'a'], "intersection([1,2,'a','b'], [2,3,'a']) should equal [2, 'a']"
print("PASSED")

print("testing union on inputs [1,2,'a','b'], [2,3,'a']...")
assert union([1, 2, 'a', 'b'], [2, 3, 'a']) == [1, 2, 3, 'a', 'b'], "union([1,2,'a','b'], [2,3,'a']) should equal [1, 2, 3, 'a', 'b']"
print("PASSED")
