import matplotlib.pyplot as plt

def sample_heads_probability(sample_list, num_heads):
  sample_counter = 0
  for sample in sample_list:
    heads = 0
    for flip in sample:
      if flip == "H":
        heads += 1
    
    if heads == num_heads:
      sample_counter += 1
  return sample_counter/len(sample_list)
  
coin_1 = ['TTH', 'HHT', 'HTH', 'TTH', 'HTH',
          'TTH', 'TTH', 'TTH', 'THT', 'TTH',
          'HTH', 'HTH', 'TTT', 'HTH', 'HTH',
          'TTH', 'HTH', 'TTT', 'TTT', 'TTT',
          'HTT', 'THT', 'HHT', 'HTH', 'TTH']
coin_2 = ['HTH', 'HTH', 'HTT', 'THH', 'HHH',
          'THH', 'HHH', 'HHH', 'HTT', 'TTH',
          'TTH', 'HHT', 'TTH', 'HTH', 'HHT',
          'THT', 'THH', 'THT', 'TTH', 'TTT',
          'HHT', 'THH', 'THT', 'THT', 'TTT']
coin_3 = ['HHH', 'THT', 'HHT', 'HHT', 'HTH',
          'HHT', 'HHT', 'HHH', 'TTT', 'THH',
          'HHH', 'HHH', 'TTH', 'THH', 'THH',
          'TTH', 'HTT', 'TTH', 'HTT', 'HHT',
          'TTH', 'HTH', 'THT', 'THT', 'HTH']

plt.style.use('bmh')
plt.plot([i for i in range(4)],[sample_heads_probability(coin_1, i) for i in range(4)],linewidth=0.75)
plt.plot([i for i in range(4)],[sample_heads_probability(coin_2, i) for i in range(4)],linewidth=0.75)
plt.plot([i for i in range(4)],[sample_heads_probability(coin_3, i) for i in range(4)],linewidth=0.75)
plt.legend(['Coin 1','Coin 2', 'Coin 3'])
plt.xlabel('Number of Heads')
plt.ylabel('Probability')
plt.title('Detecting Biased coins')
plt.savefig('biased.png')

#Coin 3 looks biased towards heads because its peak lies to the right of the center (i.e. where the peak of the true distribution should be). Coin 1 looks biased towards tails because its peak lies to the left of the center, and coin 2 looks fair because its peak is in the center. 