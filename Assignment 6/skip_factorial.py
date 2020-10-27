def skip_factorial_nonrecursive(n):
  final_num = 1
  for num in range(n,0,-2):
    final_num *= num
  return final_num


def skip_factorial_recursive(n):
  if n <= 1:
    return 1
  return n*skip_factorial_recursive(n-2)


print('testing skip_factorial_nonrecursive on input 6...')
assert skip_factorial_nonrecursive(6) == 48
print('PASSED')

print('testing skip_factorial_nonrecursive on input 7...')
assert skip_factorial_nonrecursive(7) == 105
print('PASSED')

print('testing skip_factorial_recursive on input 6...')
assert skip_factorial_recursive(6) == 48
print('PASSED')

print('testing skip_factorial_recursive on input 7...')
assert skip_factorial_recursive(7) == 105
print('PASSED')