class HashTable:
  def __init__(self, num_buckets):
    self.num_buckets = num_buckets
    self.buckets = [[] for _ in range(num_buckets)]
    self.letters = 'abcdefghijklmnopqrstuvwxyz'

  def hash_function(self, string):
    sum = 0
    for char in string:
      sum += self.letters.index(char)
    return sum % self.num_buckets
  
  def insert(self, key, value):
    bucket_index = self.hash_function(key)
    self.buckets[bucket_index].append((key, value))
  
  def find(self, key):
    bucket_index = self.hash_function(key)
    for tup in self.buckets[bucket_index]:
      if tup[0] == key:
        return tup[1]


ht = HashTable(num_buckets = 3)
print('Testing attribute buckets...')
assert ht.buckets == [[], [], []]
print('PASSED')

print('Testing method hash_function...')
assert ht.hash_function('cabbage') == 2 
print('PASSED')

print('Testing method insert...')
ht.insert('cabbage', 5)
assert ht.buckets == [[], [], [('cabbage',5)]]

ht.insert('cab', 20)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5)]]

ht.insert('c', 17)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17)]]

ht.insert('ac', 21)
assert ht.buckets == [[('cab', 20)], [], [('cabbage',5), ('c',17), ('ac', 21)]]
print('PASSED')

print('Testing method find...')
assert ht.find('cabbage') == 5
assert ht.find('cab') == 20
assert ht.find('c') == 17
assert ht.find('ac') == 21
print('PASSED')

# arr = [[], [], [], [], []]
# letters = 'abcdefghijklmnopqrstuvwxyz'  

# def hash_function(string):
#   sum = 0
#   for char in string:
#     sum += letters.index(char)
#   return sum%5

# def insert(arr, key, value):
#   bucket_index = hash_function(key)
#   arr[bucket_index].append((key, value))

# def find(arr, key):
#   bucket_index = hash_function(key)
#   for tup in arr[bucket_index]:
#     if tup[0] == key:
#       return tup[1]


# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# for i, char in enumerate(alphabet):
#     key = 'someletters'+char
#     value = [i, i**2, i**3]
#     insert(arr, key, value)

# print('Testing find...')
# for i, char in enumerate(alphabet):
#     key = 'someletters'+char
#     output_value = find(arr, key)
#     desired_value = [i, i**2, i**3]
#     assert output_value == desired_value
# print('PASSED')