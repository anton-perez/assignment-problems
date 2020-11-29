def cartesian_product(arrays):
  points = [[]]
  for arr in arrays:
    new_points = []
    for point_index in range(len(points)):
      base_point = points[point_index]
      for i in range(len(arr)):
        new_points.append(base_point+[arr[i]])
    points = new_points
  return points


print('Testing cartesian_product...')
assert cartesian_product([['a'], [1,2,3], ['Y','Z']]) == [['a',1,'Y'], ['a',1,'Z'], ['a',2,'Y'], ['a',2,'Z'], ['a',3,'Y'], ['a',3,'Z']]
print('PASSED')