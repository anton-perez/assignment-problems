def rows(arr):
  return arr

def cols(arr):
  return [[arr[i][j] for i in range(3)] for j in range(3)]

def diags(arr):
  diag = [arr[i][i] for i in range(3)]
  anti_diag = [arr[i][2-i] for i in range(3)]
  return [diag, anti_diag] 

def is_valid(arr):
  for diag in diags(arr):
    if None in diag:
      continue
    elif sum(diag) != 15:
      return False
  
  for row in rows(arr):
    if None in row:
      continue
    elif sum(row) != 15:
      return False

  for col in cols(arr):
    if None in col:
      continue
    elif sum(col) != 15:
      return False
  return True

arr1 = [[1,2,None], [None,3,None], [None,None,None]]
assert is_valid(arr1)

arr2 = [[1,2,None], [None,3,None], [None,None,4]] 
assert is_valid(arr2) is False   

arr3 = [[1,2,None], [None,3,None], [5,6,4]] 
assert is_valid(arr3) is False

arr4 = [[None,None,None], [None,3,None], [5,6,4]] 
assert is_valid(arr4) 

def elem_list(arr):
  return [arr[i][j] for i in range(3) for j in range(3)] 


arr = [[None for _ in range(3)]for _ in range(3)]
for num1 in range(1,10):
  if None not in elem_list(arr) and is_valid(arr):
    break
  arr = [[num1, None, None], [None, None, None], [None, None, None]]
  if not is_valid(arr):
    continue

  for num2 in range(1,10): 
    if None not in elem_list(arr) and is_valid(arr):
      break
    if num2 not in [num1]:
      arr = [[num1, num2, None], [None, None, None],[None, None, None]]
    else:
      continue
    if not is_valid(arr):
      continue

    for num3 in range(1,10): 
      if None not in elem_list(arr) and is_valid(arr):
        break
      if num3 not in [num1, num2]:
        arr = [[num1, num2, num3], [None, None, None],[None, None, None]]
      else:
        continue
      if not is_valid(arr):
        continue

      for num4 in range(1,10): 
        if None not in elem_list(arr) and is_valid(arr):
          break
        if num4 not in [num1, num2, num3]:
          arr = [[num1, num2, num3], [num4, None, None],[None, None, None]]
        else:
          continue
        if not is_valid(arr):
          continue

        for num5 in range(1,10): 
          if None not in elem_list(arr) and is_valid(arr):
            break
          if num5 not in [num1, num2, num3, num4]:
            arr = [[num1, num2, num3], [num4, num5, None],[None, None, None]]
          else:
            continue
          if not is_valid(arr):
            continue

          for num6 in range(1,10): 
            if None not in elem_list(arr) and is_valid(arr):
              break
            if num6 not in [num1, num2, num3, num4, num5]:
              arr = [[num1, num2, num3], [num4, num5, num6], [None, None, None]]
            else:
              continue
            if not is_valid(arr):
              continue
            
            for num7 in range(1,10): 
              if None not in elem_list(arr) and is_valid(arr):
                break
              if num7 not in [num1, num2, num3, num4, num5, num6]:
                arr = [[num1, num2, num3], [num4, num5, num6], [num7, None, None]]
              else:
                continue
              if not is_valid(arr):
                continue

              for num8 in range(1,10): 
                if None not in elem_list(arr) and is_valid(arr):
                  break
                if num8 not in [num1, num2, num3, num4, num5, num6, num7]:
                  arr = [[num1, num2, num3], [num4, num5, num6], [num7, num8, None]]
                else:
                  continue
                if not is_valid(arr):
                  continue

                for num9 in range(1,10): 
                  if None not in elem_list(arr) and is_valid(arr):
                    break
                  if num9 not in [num1, num2, num3, num4, num5, num6, num7, num8]:
                    arr = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
                  else:
                    continue
                  if not is_valid(arr):
                    continue
print(arr)