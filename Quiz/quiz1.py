def nth_term(n):
  if n == 1:
    return 0
  if n == 2:
    return 3
  return nth_term(n-1) - 2*nth_term(n-2)

print(nth_term(5))

def separate_into_words(input_string):
  string_list = input_string.split(" ")
  return string_list

print(separate_into_words("look the dog ran fast"))

def reverse_word_order(input_string):
  reverse_word_list = separate_into_words(input_string)[::-1]
  output_string = ''
  for word in reverse_word_list:
    output_string += word + ' '
  return output_string[:-1]

print(reverse_word_order("look the dog ran fast"))

class Student:
  def __init__(self, name, grade):
    self.name = name
    self.grade = grade
  
  def greeting(self):
    return "I'm {} and I'm in grade {}".format(self.name, self.grade)
  
s = Student("Rylh 'Jarug", 198)

print(s.name)
print(s.grade)
print(s.greeting())


