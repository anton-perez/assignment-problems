import math


def estimate_derivative(f, c, delta):
  return (f(c + delta/2) - f(c - delta/2))/delta

def estimate_partial_derivative(f, point, delta, variable):
  if variable == "x":
    return (f(point[0] + delta/2, point[1]) - f(point[0] - delta/2, point[1]))/delta
  elif variable == "y":
    return (f(point[0], point[1] + delta/2) - f(point[0], point[1] - delta/2))/delta

def gradient_descent(f,initial_point,alpha=0.01,delta=0.0001,iterations=10000):
  x = initial_point[0]
  y = initial_point[1]
  for i in range(iterations):
    temp_x = x
    temp_y = y
    x -= alpha*estimate_partial_derivative(f,(temp_x,temp_y),delta,'x')
    y -= alpha*estimate_partial_derivative(f,(temp_x,temp_y),delta,'y')
  return (x,y)

def f(x,y):
  return 1 + y**2 + x**2

def g(x,y):
  return 1 + x**2 + 2*x + y**2 - 9*y

min_f = gradient_descent(f,(1,2))
min_g = gradient_descent(g, (0,0))

print(min_f, f(min_f[0], min_f[1]))
print(min_g, g(min_g[0], min_g[1]))

#the minimum of f(x,y) = 1 + x^2 + y^2 is 1, and it occurs at the point (0,0)
#f(x) = 1 + x^2 + 2x + y^2 - 9y
#     = (x + 1)^2 + (y - 4.5) - 20.25
# the minimum is -20.25, and it occurs at (-1, 4.5)