import math


def is_prime(n):
  prime_boolean = True
  for m in range(2, math.floor(n/2)):
    if n % m == 0:
      prime_boolean = False

  return prime_boolean

print("testing is_prime on input 59...")
assert is_prime(59) is True, "is_prime(59) should equal True"
print("PASSED")

print("testing is_prime on input 51...")
assert is_prime(51) is False, "is_prime(51) should equal False"
print("PASSED")
