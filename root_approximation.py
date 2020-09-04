def update_bounds(bounds):
  midpoint = (bounds[0]+bounds[1])/2
  if midpoint**2 < 2:
    new_bounds = [midpoint, bounds[1]]
  else:
    new_bounds = [bounds[0], midpoint]
  return new_bounds


def estimate_root(precision):
  bounds = [1,2]
  while abs(bounds[1]-bounds[0]) > precision:
    bounds = update_bounds(bounds)
  return (bounds[0]+bounds[1])/2

print('testing update_bounds on input [1, 2]...')
assert update_bounds([1,2]) == [1, 1.5]
print('PASSED')

print('testing update_bounds on input [1, 1.5]...')
assert update_bounds([1,1.5]) == [1.25, 1.5]
print('PASSED')

print('testing estimate_root on input 0.1...')
assert estimate_root(0.1) == 1.40625
print('PASSED')
