def identity_matrix_elements(n): 
  return [[1 if row_index == col_index else 0 for col_index in range(n)] for row_index in range(n)]


def counting_across_rows_matrix_elements(m,n):
  return [[col_index + n*row_index + 1 for col_index in range(n)] for row_index in range(m)]

print('testing identity_matrix_elements on input 4...')
assert identity_matrix_elements(4) == [[1, 0, 0, 0],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]]
print('PASSED')

print('testing counting_across_rows_matrix_elements on inputs 3, 4...')
assert counting_across_rows_matrix_elements(3,4) == [[1, 2, 3, 4],
                                                     [5, 6, 7, 8],
                                                     [9, 10, 11, 12]]
print('PASSED')