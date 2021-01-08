import random as rand

def random_draw(distribution):
  c_dist = []
  accumulation = 0
  for prob in distribution:
    accumulation += prob
    c_dist.append(accumulation)

  random_num = rand.random()

  for index in range(len(c_dist)):
    if random_num < c_dist[index]:
      return index

print([0.5, 0.5])
print('Expected Value: 0.5')
sum = 0
for _ in range(1000):
  sum += random_draw([0.5,0.5])
print('Average Value:', sum/1000)

print([0.25, 0.25, 0.5])
print('Expected Value: 1.25')
sum = 0
for _ in range(1000):
  sum += random_draw([0.25, 0.25, 0.5])
print('Average Value:', sum/1000)
  
print([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])
print('Expected Value: 2.8')
sum = 0
for _ in range(1000):
  sum += random_draw([0.05, 0.2, 0.15, 0.3, 0.1, 0.2])
print('Average Value:', sum/1000)

  