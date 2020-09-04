letters = " abcdefghijklmnopqrstuvwxyz"


def encode(string, a, b):
  return [a*letters.index(char)+b for char in string]


def decode(numbers, a, b):
  string = ""
  for num in numbers:
    index = (num-b)/a
    if index in range(0, 27) and index - int(index) == 0:
      string += letters[int(index)]
    else:
      return False
  return string

print("testing encode on input 'a cat'...")
assert encode('a cat', 2, 3) == [5, 3, 9, 5, 43], "{} should be {}".format(encode('a cat', 2, 3), [5, 3, 9, 5, 43])
print("PASSED")

print("testing decode on input [5, 3, 9, 5, 43]...")
assert decode([5, 3, 9, 5, 43], 2, 3) == 'a cat', "{} should be {}".format(decode([5, 3, 9, 5, 43], 2, 3),'a cat')
print("PASSED")

print("testing decode on input [1, 3, 9, 5, 43]...")
assert decode([1, 3, 9, 5, 43], 2, 3) is False, "{} should be {}".format(decode([1, 3, 9, 5, 43], 2, 3),'a cat')
print("PASSED")

print("testing decode on input [5, 3, 9, 5, 44]...")
assert decode([5, 3, 9, 5, 44], 2, 3) is False, "{} should be {}".format(decode([5, 3, 9, 5, 44], 2, 3),'a cat')
print("PASSED")

encoded_message = [377,
 717,
 71,
 513,
 105,
 921,
 581,
 547,
 547,
 105,
 377,
 717,
 241,
 71,
 105,
 547,
 71,
 377,
 547,
 717,
 751,
 683,
 785,
 513,
 241,
 547,
 751]

for a in range(1,101):
  for b in range(0,101):
    if decode(encoded_message,a,b) is not False:
      print(decode(encoded_message,a,b), a, b)

