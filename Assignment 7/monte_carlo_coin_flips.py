import random

def factorial(n):
  if n <= 1:
    return 1
  return n*factorial(n-1)


def probability(num_heads, num_flips):
  total_outcomes = 2**num_flips
  favored_outcomes = factorial(num_flips)/(factorial(num_flips-num_heads)*factorial(num_heads))
  return favored_outcomes/total_outcomes


def monte_carlo_probability(num_heads, num_flips, num_samples):
  favored_outcomes = 0
  for time in range(num_samples):
    heads = 0
    for flip in range(num_flips):
      heads += round(random.random())
    if heads == num_heads:
      favored_outcomes += 1

  return favored_outcomes/num_samples

print('testing probability on inputs 5, 8....')
assert probability(5,8) == 0.21875
print('PASSED')

print("probability result", probability(5,8))
for i in range(5):
  print("monte_carlo_probability result", monte_carlo_probability(5,8, 1000))
  