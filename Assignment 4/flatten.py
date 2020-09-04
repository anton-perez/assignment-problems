def flatten(nested_dict):
  flat_dict = {}
  for key in nested_dict:
    for subkey in nested_dict[key]:
      flat_dict[key + "_" + subkey] = nested_dict[key][subkey]

  return flat_dict

colors = {
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

flat_colors = {
  'animal_bumblebee': ['yellow', 'black'],
  'animal_elephant': ['gray'],
  'animal_fox': ['orange', 'white'],
  'food_apple': ['red', 'green', 'yellow'],
  'food_cheese': ['white', 'orange']
}

print('testing flatten on input colors...')
assert flatten(colors) == flat_colors, "{} should be equal to {}".format(flatten(colors), flat_colors)
print('PASSED')
