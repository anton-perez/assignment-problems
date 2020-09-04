import math


def convert_to_base_2(decimal_num):
  num_of_bits = math.floor(math.log(decimal_num, 2))+1
  bit_str = ""
  remaining = decimal_num
  for place in range(num_of_bits, 0, -1):
    if remaining - 2**(place-1) >= 0:
      bit_str += "1"
      remaining -= 2**(place-1)
    else:
      bit_str +="0"

  return int(bit_str)

print("testing convert_to_base_2 on input 19...")
assert convert_to_base_2(19) == 10011, "convert_to_base_2(10011) should equal 19"
print("PASSED")
