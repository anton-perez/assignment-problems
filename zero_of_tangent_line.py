def estimate_derivative(f, c, delta):
  return (f(c + delta/2) - f(c - delta/2))/delta


def zero_of_tangent_line(f, c, delta):
  m = estimate_derivative(f, c, delta)
  return -f(c)/m + c


def estimate_solution(f, init_guess, delta, precision):
  estimate = zero_of_tangent_line(f, init_guess, delta)
  prev_estimate = zero_of_tangent_line(f, init_guess, delta) + precision
  while abs(estimate - prev_estimate) >= precision:
    prev_estimate = estimate
    estimate = zero_of_tangent_line(f, estimate, delta)
  return estimate


def f(x):
  return x**3 + x - 1

print('Testing zero_of_tangent_line...')
assert round(zero_of_tangent_line(f, 0.5, 0.001), 6) == 0.714286, zero_of_tangent_line(f, 0.5, 0.001)
print('PASSED')

print('Testing estimate_solution...')
assert round(estimate_solution(f, 0.5, 0.001, 0.01), 6) == 0.682328
print('PASSED')
