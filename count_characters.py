def count_characters(input_string):
  lowercase_str = list(input_string.lower())
  
  return {char: lowercase_str.count(char) for char in lowercase_str}

print("testing count_characters on input 'A cat!!!'...")
assert count_characters('A cat!!!') == {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3},"count_characters('A cat!!!') should equal {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}"
print("PASSED")
