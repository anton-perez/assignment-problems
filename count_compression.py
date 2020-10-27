def count_compression(string):
  compressed_list = []
  current_char = string[0]
  counter = 0
  for index in range(1, len(string)+1):
    if index < len(string) and string[index] == current_char:
      counter += 1
    else:
      counter += 1
      compressed_list.append((current_char, counter))
      counter = 0
      if index < len(string):
        current_char = string[index]
  return compressed_list


def count_decompression(compressed_string):
  decompressed_string = ""
  for tuple in compressed_string:
    for iteration in range(tuple[1]):
      decompressed_string += str(tuple[0])
  return decompressed_string


print('Testing count_compression...')
assert count_compression('aaabbcaaaa') == [('a',3), ('b',2), ('c',1), ('a',4)]
assert count_compression('22344444') == [('2',2), ('3',1), ('4',5)]
print('PASSED')

print('Testing count_decompression...')
assert count_decompression([('a',3), ('b',2), ('c',1), ('a',4)]) == 'aaabbcaaaa'
assert count_decompression([(2,2), (3,1), (4,5)]) == '22344444'
print('PASSED')