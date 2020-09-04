def make_nested(flat_dict):
  nested_dict = {}
  for key in flat_dict:
    nest_keys = key.split("_")
    if nest_keys[0] not in nested_dict:
      nested_dict[nest_keys[0]] = {}
    nested_dict[nest_keys[0]][nest_keys[1]] = flat_dict.get(key)

  return nested_dict

colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}

nested_colors = {
  'animal': {
    'bumblebee': ['yellow', 'black'],
    'elephant': ['gray'],
    'fox': ['orange', 'white']
  },
  'food': {
    'apple': ['red', 'green', 'yellow'],
    'cheese': ['white', 'orange']
  }
}

print('testing make_nested on input colors...')
assert make_nested(colors) == nested_colors, "{} should be equal to {}".format(make_nested(colors), nested_colors)
print('PASSED')
