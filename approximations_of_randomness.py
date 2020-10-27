import math


def factorial(n):
  if n <= 1:
    return 1
  return n*factorial(n-1)


def distribution_finder(sample_string):
  sample_list = sample_string.split(' ')
  distribution_list = [0 for i in range(len(sample_list[0])+1)]
  for sample in sample_list:
    head_counter = 0
    for flip in sample:
      if flip == 'H':
        head_counter += 1
    distribution_list[head_counter] += 1/len(sample_list)

  return distribution_list


def probability(num_heads, num_flips):
  total_outcomes = 2**num_flips
  favored_outcomes = factorial(num_flips)/(factorial(num_flips-num_heads)*factorial(num_heads))
  return favored_outcomes/total_outcomes


def kl_divergence(p, q):
  sum = 0
  for index in range(len(p)):
    if p[index] != 0 and q[index] !=0:
      sum += p[index]*math.log(p[index]/q[index])
  return sum

flips = {
    'Justin S': 'HTTH HHTT TTHH TTTH HHTH TTHT HHHH THHT THTT HTHH TTTT HTHT TTHH THTH HTTH HHTH HHHT TTTH HTTH HTHT',
    'Nathan R': 'HTTH HHTH HTTT HTHH HTTH HHHH TTHH TTHT THTT HTHT HHTH TTTT THHT HTTH HTHH THHH HTTH THTT HHHT HTHH',
    'Justin H': 'HHHT HHTH HHTT THHT HTTT HTTT HHHT HTTT TTTT HTHT THHH TTHT TTHH HTHT TTTT HHHH THHH THTH HHHH THHT',
    'Nathan A': 'HTTH HHHH THHH TTTH HTTT THTT HTHT THHT HTTH TTTT HHHH TTHH HHTH TTTH HHHH THTT HTHT TTTT HHTT HHTT',
    'Cayden': 'HTHT HHTT HTTH THTH THHT TTHH HHHH TTTH HHHT HTTT TTHT HHTH HTHH THTT HHHH THTT HTTT HTHH TTTT HTTH',
    'Maia': 'HTHH THTH HTTH TTTT TTHT HHHH HHTT THHH TTHH HHTH THHT HHHH THTT HHTH HTHT TTHH TTHH HHHH TTTT HHHT',
    'Spencer': 'HHHT HTTH HTTT HTHH THTT TTHT TTTT HTTH HHTH TTHT TTHH HTHT THHT TTHT THTT THTH HTTH THHT TTTH HHHH',
    'Charlie': 'HHHH HHHT HHTT HTTT TTTT TTTH TTHH THHH THTH HTHT HHTH HTHH TTHT THTT THTH TTHT HTHT THHT HTTH THTH',
    'Anton': 'HHTH THTH TTTT HTTH THTT TTTH THHH TTHH THHT HHHH TTHT HTTT THTH HHHT HHTH HHHH TTTH HTHT TTTT HHTT',
    'William': 'THTT HHHT HTTH THHT THTH HHHT TTTH HHTH THTH HTHT HHHT TTHT HHHT THTT HHTT TTHH HHTH TTTT THTH TTHT'
}
true_dist = [probability(i, 4) for i in range(5)]

kl_divs = [(key, kl_divergence(distribution_finder(flips[key]), true_dist)) for key in flips] 

sorted_kl_divs = []
for i in range(len(kl_divs)):
  min_tup = kl_divs[0]
  minimum = min_tup[1]
  for tup in kl_divs:
    if tup[1] < minimum:
      minimum = tup[1]
      min_tup = tup
  sorted_kl_divs.append(min_tup)
  kl_divs.remove(min_tup)


for divs in sorted_kl_divs:
  print(divs[0] + ':' + str(divs[1]))

#Chalie's approximation was the closest.