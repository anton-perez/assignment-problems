def convert_to_base_10(binary_num):
  binary_str = str(binary_num)[::-1]
  decimal_num = 0
  for bit_index in range(len(binary_str)):
    decimal_num += int(binary_str[bit_index])*(2**bit_index)

  return decimal_num

print("testing convert_to_base_10 on input 10011...")
assert convert_to_base_10(10011) == 19, "convert_to_base_10(10011) should equal 19"
print("PASSED")
