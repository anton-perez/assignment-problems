sum = 0
for k in range(25,100000):
  sum += 1/k**5

print(sum)
#sum = 6.9290476e-7
#c = 1443199.784
prob = 0
k = 25
while prob < 0.95:
  prob += 1443199.784/k**5
  k += 1
print(k-1)
#k = 52
