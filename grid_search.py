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

def grid_search(objective_function, grid_lines):
  points = cartesian_product(grid_lines)
  min_point = points[0]
  min_value = objective_function(*min_point)
  for point in points:
    value = objective_function(*point)
    if value < min_value:
      min_value = value
      min_point = point
  
  return min_point


def two_variable_function(x, y):
        return (x-1)**2 + (y-1)**3

x_lines = [0, 0.25, 0.75]
y_lines = [0.9, 1, 1.1, 1.2]
grid_lines = [x_lines, y_lines]
print('Testing grid_search...')
assert grid_search(two_variable_function, grid_lines) == [0.75, 0.9]
print('PASSED')