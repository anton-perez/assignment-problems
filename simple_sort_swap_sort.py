def simple_sort(num_list):
  sorted_list = []
  times = len(num_list)
  for time in range(times):
    min = num_list[0]
    for num in num_list:
      if num < min:
        min = num
    sorted_list.append(min)
    num_list.remove(min)
  return sorted_list


def swap_sort(num_list):
  swaps = 0
  for i in range(0, len(num_list)):
    if i+1 < len(num_list) and num_list[i] > num_list[i+1]:
      temp = num_list[i+1]
      num_list[i+1] = num_list[i]
      num_list[i] = temp
      swaps +=1
  if swaps == 0:
    return num_list 
  return swap_sort(num_list)

print('testing simple_sort on input [5,8,2,2,4,3,0,2,-5,3.14,2]...')
assert simple_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8]
print('PASSED')

print('testing swap_sort on input [5,8,2,2,4,3,0,2,-5,3.14,2]...')
assert swap_sort([5,8,2,2,4,3,0,2,-5,3.14,2]) == [-5,0,2,2,2,2,3,3.14,4,5,8]
print('PASSED')
