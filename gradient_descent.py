import math


def estimate_derivative(f, c, delta):
  return (f(c + delta/2) - f(c - delta/2))/delta

def estimate_partial_derivative(f, point, delta, variable):
  if variable == "x":
    return (f(point[0] + delta/2, point[1]) - f(point[0] - delta/2, point[1]))/delta
  elif variable == "y":
    return (f(point[0], point[1] + delta/2) - f(point[0], point[1] - delta/2))/delta

# def gradient_descent(f,x0,alpha=0.01,delta=0.0001,iterations=10000):
#   x = x0
#   for i in range(iterations):
#     x = x - alpha*estimate_derivative(f,x,delta)
#   return x

def gradient_descent(f,initial_point,alpha=0.01,delta=0.0001,iterations=10000):
  x = initial_point[0]
  y = initial_point[1]
  for i in range(iterations):
    temp_x = x
    temp_y = y
    x -= alpha*estimate_partial_derivative(f,(temp_x,temp_y),delta,'x')
    y -= alpha*estimate_partial_derivative(f,(temp_x,temp_y),delta,'y')
  return (x,y)


# def f(x):
#   return x**2+2*x+1

# def g(x):
#   return (x**2 + math.cos(x))/ (math.e**(math.sin(x))) 

# min_f = round(gradient_descent(f,0),8)
# min_g = round(gradient_descent(g,0),8)
# print((min_f, f(min_f)))
# print((min_g, g(min_g)))

def f(x,y):
  return 1 + y**2 + x**2

def g(x,y):
  return 1 + x**2 + 2*x + y**2 - 9*y

print(gradient_descent(f,(1,2)))
print(gradient_descent(g,(0,0)))