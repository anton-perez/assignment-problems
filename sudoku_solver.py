import math

def rows(square):
  return square

def cols(square):
  return [[square[i][j] for i in range(6)] for j in range(6)]

def sextants(square):
  return [[square[math.floor(i/3) + 2*(math.floor(j/2))][i%3+j%2] for i in range(6)] for j in range(6)]

def is_valid(square):
  for sextant in sextants(square):
    if None in sextant:
      continue
    elif set(sextant) != set([i+1 for i in range(6)]):
      return False
  
  for row in rows(square):
    if None in row:
      continue
    elif set(row) != set([i+1 for i in range(6)]):
      return False

  for col in cols(square):
    if None in col:
      continue
    elif set(col) != set([i+1 for i in range(6)]):
      return False
  return True

def arr_to_square(arr):
  side_length = int(len(arr) ** 0.5)
  return [arr[i:i+side_length] for i in range(0, len(arr), side_length)]

def square_to_arr(square):
  return [square[i][j] for i in range(6) for j in range(6)] 



def solve_sudoku(square):
  # n = get_magic_const(size)
  arr = square_to_arr(square)
  filled_indices = [i for i in range(len(arr)) if arr[i] != None]
  increase_index = True

  current_index = 0
  while None in arr or not is_valid(arr_to_square(arr)):
    if current_index in filled_indices:
      if increase_index:
        current_index += 1
      else:
        current_index -= 1
      continue

    if arr[current_index] == None:
      arr[current_index] = 0
    arr[current_index] += 1
      
    if arr[current_index] >= len(square)+1:
      arr[current_index] = None
      current_index -= 1
      increase_index = False
      continue

    if is_valid(arr_to_square(arr)):
      current_index += 1
      increase_index = True

  return arr_to_square(arr)


def print_sudoku(square):
  print('---------------------')

  for row in square:
    string = '|'
    for i in range(len(row)):
      string += ' ' + str(row[i]) + ' '
      if (i+1)%3 == 0:
        string += '|' 
    print(string)
    if square.index(row)%2 == 1:
      print('---------------------')


sudoku = [[None, None, 4,    None, None, None],
          [None, None, None, 2,    3,    None],
          [3,    None, None, None, 6,    None],
          [None, 6,    None, None, None, 2],
          [None, 2,    1,    None, None, None],
          [None, None, None, 5,    None, None]]
print(solve_sudoku(sudoku))
print_sudoku(solve_sudoku(sudoku))