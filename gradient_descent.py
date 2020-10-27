import math


def estimate_derivative(f, c, delta):
  return (f(c + delta/2) - f(c - delta/2))/delta


def gradient_descent(f,x0,alpha=0.01,delta=0.0001,iterations=10000):
  x = x0
  for i in range(iterations):
    x = x - alpha*estimate_derivative(f,x,delta)
  return x


def f(x):
  return x**2+2*x+1

def g(x):
  return (x**2 + math.cos(x))/ (math.e**(math.sin(x))) 

min_f = round(gradient_descent(f,0),8)
min_g = round(gradient_descent(g,0),8)
print((min_f, f(min_f)))
print((min_g, g(min_g)))