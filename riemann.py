import math
import matplotlib.pyplot as plt

def standard_normal_dist(t):
    return (1/(2*math.pi)**0.5)*math.e**(-(t**2)/2)

def calc_standard_normal_probability(a,b,n,rule):
  step = (b-a)/n

  if rule == 'left endpoint':
    riemann = 0
    x = a
    for _ in range(n):
      riemann += step*standard_normal_dist(x)
      x += step
    return riemann

  elif rule == 'right endpoint':
    riemann = 0
    x = a + step
    for _ in range(n):
      riemann += step*standard_normal_dist(x)
      x += step
    return riemann

  elif rule == 'midpoint':
    riemann = 0
    x = a + step/2
    for _ in range(n):
      riemann += step*standard_normal_dist(x)
      x += step
    return riemann

  elif rule == 'trapezoidal':
    x = a
    riemann = 0.5*step*standard_normal_dist(a)
    for _ in range(n-1):
      x += step
      riemann += step*standard_normal_dist(x)
    x += step
    riemann += 0.5*step*standard_normal_dist(x)
    return riemann

  elif rule == 'simpson':
    x = a
    riemann = step*standard_normal_dist(a)/3
    for i in range(n-1):
      x += step
      riemann += 2*((i+1)%2 + 1)*step*standard_normal_dist(x)/3
    x += step
    riemann += step*standard_normal_dist(x)/3
    return riemann

# print('Interval [-1,1]:',calc_standard_normal_probability(-1,1))
# print('Interval [-2,2]:',calc_standard_normal_probability(-2,2))
# print('Interval [-3,3]:',calc_standard_normal_probability(-3,3))

plt.style.use('bmh')
plt.plot(
  [i for i in range(2,101,2)],
  [calc_standard_normal_probability(0,1,i,'left endpoint') for i in range(2,101,2)],linewidth=0.75, label='left')
plt.plot(
  [i for i in range(2,101,2)],
  [calc_standard_normal_probability(0,1,i,'right endpoint') for i in range(2,101,2)],linewidth=0.75, label='right')
plt.plot(
  [i for i in range(2,101,2)],
  [calc_standard_normal_probability(0,1,i,'midpoint') for i in range(2,101,2)],linewidth=0.75, label='midpoint')
plt.plot(
  [i for i in range(2,101,2)],
  [calc_standard_normal_probability(0,1,i,'trapezoidal') for i in range(2,101,2)],linewidth=0.75, label='trapezoidal')
plt.plot(
  [i for i in range(2,101,2)],
  [calc_standard_normal_probability(0,1,i,'simpson') for i in range(2,101,2)],linewidth=0.75, label='simpson')
plt.legend()
plt.xlabel('Number of Subintervals')
plt.ylabel('Estimated Value')
plt.savefig('riemann.png')
