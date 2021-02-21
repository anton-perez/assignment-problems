arr = [[], [], [], [], []]
letters = 'abcdefghijklmnopqrstuvwxyz'  

def hash_function(string):
  sum = 0
  for char in string:
    sum += letters.index(char)
  return sum%5

def insert(arr, key, value):
  bucket_index = hash_function(key)
  arr[bucket_index].append((key, value))

def find(arr, key):
  bucket_index = hash_function(key)
  for tup in arr[bucket_index]:
    if tup[0] == key:
      return tup[1]


alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    value = [i, i**2, i**3]
    insert(arr, key, value)

print('Testing find...')
for i, char in enumerate(alphabet):
    key = 'someletters'+char
    output_value = find(arr, key)
    desired_value = [i, i**2, i**3]
    assert output_value == desired_value
print('PASSED')