import math
import sys
sys.path.append('Assignment 7')
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability

def kl_divergence(p, q):
  sum = 0
  for index in range(len(p)):
    if p[index] != 0 and q[index] !=0:
      sum += p[index]*math.log(p[index]/q[index])
  return round(sum, 11)

p = [0.2, 0.5, 0, 0.3]
q = [0.1, 0.8, 0.1, 0]

print('Testing kl_divergence...')
assert kl_divergence(p,q) == -0.09637237851 
print('PASSED')

q = [probability(i, 8) for i in range(9)]

print('Computing KL Divergence for MC Simulations...')
p = [monte_carlo_probability(i, 8, 100) for i in range(9)]
print('100 samples --> KL Divergence =', kl_divergence(p,q))
p = [monte_carlo_probability(i, 8, 1000) for i in range(9)]
print('1000 samples --> KL Divergence =', kl_divergence(p,q))
p = [monte_carlo_probability(i, 8, 10000) for i in range(9)]
print('10000 samples --> KL Divergence =', kl_divergence(p,q))

# As the number of samples increases, the KL divergence approaches 0 because the approximate probability tends to approach the true distribution the more samples there are.