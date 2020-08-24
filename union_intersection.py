def intersection(list_1, list_2):
  return list(set(list_1) & set(list_2))


def union(list_1, list_2):
  return list(set(list_1) | set(list_2))

print("testing intersection on inputs [1, 2, 'a', 'b'], [2, 3, 'a']...")
assert intersection([1, 2, 'a', 'b'], [2, 3, 'a']) == [2, 'a'], "intersection([1,2,'a','b'], [2,3,'a']) should equal [2, 'a']"
print("PASSED")

print("testing union on inputs [1,2,'a','b'], [2,3,'a']...")
assert union([1, 2, 'a', 'b'], [2, 3, 'a']) == [1, 2, 3, 'a', 'b'], "union([1,2,'a','b'], [2,3,'a']) should equal [1, 2, 3, 'a', 'b']"
print("PASSED")
