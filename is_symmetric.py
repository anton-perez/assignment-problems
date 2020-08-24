def is_symmetric(input_string):
    backwards_string = input_string[::-1]
    is_palindrome = False

    if backwards_string == input_string:
        is_palindrome = True
    else:
        is_palindrome = False

    return palindrome

print("testing is_symmetric on input 'racecar'...")
assert is_symmetric("racecar") is True, "is_symmetric('racecar') should be True"
print("PASSED")

print("testing is_symmetric on input 'batman'...")
assert is_symmetric("batman") is False, "is_symmetric('batman') should be False"
print("PASSED")
