def bisection_search(entry, sorted_list):
  low = 0
  high = len(sorted_list)-1
  midpoint = round((high+low)/2)

  while sorted_list[midpoint] != entry:
    midpoint = round((high+low)/2)
    if sorted_list[midpoint] < entry:
      low = midpoint + 1
    if sorted_list[midpoint] > entry:
      high = midpoint - 1

  return midpoint

print('Testing bisection_search...')
assert bisection_search(14, [2, 3, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16]) == 9
assert bisection_search(21, [5, 7, 9, 20, 21, 22, 23]) == 4
print('PASSED')

