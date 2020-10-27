def tally_sort(num_list):
  minimum = num_list[0]
  for n in num_list:
    if n<minimum:
      minimum = n

  temp_list = [num-minimum for num in num_list]

  maximum = temp_list[0]
  for m in temp_list:
    if m>maximum:
      maximum = m

  tallys = [0 for i in range(maximum+1)]
  for index in temp_list:
    tallys[index] +=1
    
  sorted_list = []
  for nums in range(len(tallys)):
    for num_times in range(tallys[nums]):
      sorted_list.append(nums+minimum)
  return sorted_list

print('Testing tally_sort on input [2, 2, 3, 3, 5, 6, 8]...')
assert tally_sort([2, 5, 2, 3, 8, 6, 3]) == [2, 2, 3, 3, 5, 6, 8]
print('PASSED')