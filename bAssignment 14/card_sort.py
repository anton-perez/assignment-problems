def insert_element(element, sorted_list):
  for index in range(len(sorted_list)):
    if sorted_list[index] > element:
      return sorted_list[:index] + [element] + sorted_list[index:]
  return sorted_list + [element]

def card_sort(num_list):
  sorted_list = [num_list[0]]
  for index in range(1, len(num_list)):
    sorted_list = insert_element(num_list[index], sorted_list)
  return sorted_list

print('Testing card_sort on input [12, 11, 13, 5, 6]...')
assert card_sort([12, 11, 13, 5, 6]) == [5, 6, 11, 12, 13]
print('PASSED')

print('Testing card_sort on input [5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]...')
assert card_sort([5, 7, 3, 5, 1, 3, -1, 1, -3, -1, -3, -1]) == [-3, -3, -1, -1, -1, 1, 1, 3, 3, 5, 5, 7]
print('PASSED')