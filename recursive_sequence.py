def first_n_terms(n):
  terms = []
  curr_term = 5
  for i in range(n):
    terms.append(curr_term)
    curr_term = 3*curr_term - 4
  return terms


def nth_term(n):
  if n == 1:
    return 5
  return 3*nth_term(n-1) - 4

print("testing first_n_terms on input 10...")
assert first_n_terms(10) == [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051], "first_n_terms(10) should equal [5, 11, 29, 83, 245, 731, 2189, 6563, 19685, 59051]"
print("PASSED")

print("testing nth_term on input 10...")
assert nth_term(10) == 59051, "nth_term(10) should equal 59051"
print("PASSED")
