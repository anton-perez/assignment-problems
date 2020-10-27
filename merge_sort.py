def merge(x,y):
  merged_list = []
  long_list = x if len(x) > len(y) else y
  short_list = y if len(x) > len(y) else x
  long_index = 0
  for index in range(len(short_list)):
    while long_index < len(long_list) and long_list[long_index] < short_list[index]:
      merged_list.append(long_list[long_index])
      long_index +=1 
    merged_list.append(short_list[index])

  for remaining_index in range(long_index, len(long_list)):
    merged_list.append(long_list[remaining_index])

  return merged_list


def merge_sort(input_list):
  if len(input_list)>1:
    first_half = input_list[:round(len(input_list)/2)]
    last_half = input_list[round(len(input_list)/2):]
    sorted_first_half = merge_sort(first_half)
    sorted_last_half = merge_sort(last_half)
    return merge(sorted_first_half, sorted_last_half)
  else:
    return input_list

print('Testing merge...')
assert merge([-2,1,4,4,4,5,7],[-1,6,6]) == [-2,-1,1,4,4,4,5,6,6,7]
print('PASSED')

print('Testing merge_sort...')
assert merge_sort([4,8,7,7,4,2,3,1]) == [1,2,3,4,4,7,7,8]
print('PASSED')