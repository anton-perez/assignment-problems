import matplotlib.pyplot as plt


def collatz_iterations(number):
  n = number
  iterations = 0
  while n != 1:
    if n%2 == 0:
      n *= 1/2
    else:
      n = 3*n+1
    iterations +=1
  return iterations

print("Testing collatz_iterations on input 13...")
assert collatz_iterations(13) == 9
print("PASSED")
    
max_num = 1
max = collatz_iterations(max_num)
for i in range(1,1001):
  if collatz_iterations(i) > max:
    max_num = i
    max = collatz_iterations(i)

print(max_num)

plt.style.use('bmh')
x_coords = [i for i in range(1,1001)]
y_coords = [collatz_iterations(i) for i in range(1,1001)]
plt.plot(x_coords, y_coords)
plt.xlabel('Input Number')
plt.ylabel('Iterations')
plt.title('Collatz Iterations plot')
plt.savefig('plot.png')
