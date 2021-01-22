input_string = '"alpha","beta","gamma","delta"\n1,2,3,4\n5.0,6.0,7.0,8.0'
rows = input_string.split('\n')
string_lists = [x.split(',') for x in rows]

arr = []
for string_list in string_lists:
  new_value_list = []
  for string in string_list:
    if string[0]=='"' and string[-1]=='"':
      string = string[1:-1]
    elif '.' in string:
      string = float(string)
    else:
      string = int(string)
    new_value_list.append(string)
  arr.append(new_value_list)
print(arr)
