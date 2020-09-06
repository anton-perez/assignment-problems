def even_odd_tuples(numbers):
  return [(n, 'even') if n%2 == 0 else (n, "odd") for n in numbers]


def even_odd_dict(numbers):
  return {n:"even" if n%2 == 0 else "odd" for n in numbers}

e_o_list =  [(1,'odd'),(2,'even'),(3,'odd'),(5,'odd'),(8,'even'),(11,'odd')]

e_o_dict = {
    1:'odd',
    2:'even',
    3:'odd',
    5:'odd',
    8:'even',
    11:'odd'
}

print("testing even_odd_tuples on input [1,2,3,5,8,11]...")
assert even_odd_tuples([1,2,3,5,8,11]) == e_o_list, "{} should be {}".format(even_odd_tuples([1,2,3,5,8,11]), e_o_list)
print('PASSED')

print("testing even_odd_dict on input [1,2,3,5,8,11]...")
assert even_odd_dict([1,2,3,5,8,11]) == e_o_dict, "{} should be {}".format(even_odd_dict([1,2,3,5,8,11]), e_o_dict)
print('PASSED')
