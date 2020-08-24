letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def convert_to_numbers(input_string):
    output_nums = []
    for char in input_string:
        output_nums.append(letters.index(char))

    return output_nums


def convert_to_letters(input_list):
    output_str = ""
    for num in input_list:
        output_str += letters[num]

    return output_str

print("testing convert_to_numbers on input 'a cat'...")
assert convert_to_numbers("a cat") == [1, 0, 3, 1, 20], "convert_to_numbers('a cat') should equal [1,0,3,1,20]"
print("PASSED")

print("testing convert_to_letters on input [1,0,3,1,20]...")
assert convert_to_letters([1, 0, 3, 1, 20]) == "a cat", "convert_to_letters([1,0,3,1,20]) should equal 'a cat'"
print("PASSED")
