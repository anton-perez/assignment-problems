import matplotlib.pyplot as plt
import sys
sys.path.append('Assignment 7')
from monte_carlo_coin_flips import probability
from monte_carlo_coin_flips import monte_carlo_probability


plt.style.use('bmh')
plt.plot([i for i in range(9)],[probability(i, 8) for i in range(9)],linewidth=2.5)
plt.plot([i for i in range(9)],[monte_carlo_probability(i, 8, 1000) for i in range(9)],linewidth=0.75)
plt.plot([i for i in range(9)],[monte_carlo_probability(i, 8, 1000) for i in range(9)],linewidth=0.75)
plt.plot([i for i in range(9)],[monte_carlo_probability(i, 8, 1000) for i in range(9)],linewidth=0.75)
plt.plot([i for i in range(9)],[monte_carlo_probability(i, 8, 1000) for i in range(9)],linewidth=0.75)
plt.plot([i for i in range(9)],[monte_carlo_probability(i, 8, 1000) for i in range(9)],linewidth=0.75)
plt.legend(['True','MC 1','MC 2','MC 3','MC 4','MC 5'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('True Distribution vs Monte Carlo Simulations for 8 Coin Flips')
plt.savefig('plot.png')