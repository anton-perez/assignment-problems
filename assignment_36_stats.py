sum = 0
for k in range(68,100000):
  sum += 1/k**4

print(sum)
#sum = 1.083726e-6
#c =  922742.5
prob = 0
k = 68
while prob <= 0.95:
  prob += 922742.5/k**4
  k += 1
print(k-1)
#k = 52