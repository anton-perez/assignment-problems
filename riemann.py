import math

def calc_standard_normal_probability(a,b):
  riemann = 0
  for x in range(1000*a, 1001*b):
    riemann += (0.001/(2*math.pi)**0.5)*math.e**(-((x/1000)**2)/2)
  return riemann

print('Interval [-1,1]:',calc_standard_normal_probability(-1,1))
print('Interval [-2,2]:',calc_standard_normal_probability(-2,2))
print('Interval [-3,3]:',calc_standard_normal_probability(-3,3))
