class Stack:
  def __init__(self):
    self.data = []

  def push(self, new_data):
    self.data.append(new_data)
  
  def pop(self):
    self.data.remove(self.data[len(self.data)-1])

  def peek(self):
    return self.data[len(self.data)-1]

s = Stack()

print("testing s.data...")
assert s.data == []
print('PASSED')

s.push('a')
s.push('b')
s.push('c')

print("testing s.push...")
assert s.data == ['a', 'b', 'c']
print('PASSED')

s.pop()

print("testing s.pop...")
assert s.data == ['a', 'b']
print('PASSED')

print("testing s.peek...")
assert s.peek() == 'b'
print('PASSED')

print("testing s.data...")
assert s.data == ['a', 'b']
print('PASSED')
