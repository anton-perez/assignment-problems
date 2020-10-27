def unlist_nonrecursive(x):
  sub_list = x
  while not (type(sub_list) != list or len(sub_list) != 1):
    sub_list = sub_list[0]
  return sub_list


def unlist_recursive(x):
  if type(x) != list or len(x) != 1:
    return x
  return unlist_recursive(x[0])

print('Testing unlist_nonrecursive on input [[[[1], [2,3], 4]]]...')
assert unlist_nonrecursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
print('PASSED')

print('Testing unlist_nonrecursive on input [[[[1]]]]...')
assert unlist_nonrecursive([[[[1]]]]) == 1
print('PASSED')

print('Testing unlist_recursive on input [[[[1], [2,3], 4]]]...')
assert unlist_recursive([[[[1], [2,3], 4]]]) == [[1], [2,3], 4]
print('PASSED')

print('Testing unlist_recursive on input [[[[1]]]]...')
assert unlist_recursive([[[[1]]]]) == 1
print('PASSED')