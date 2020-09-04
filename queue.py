class Queue:
  def __init__(self):
    self.data = []

  def enqueue(self, new_element):
    self.data.append(new_element)

  def dequeue(self):
    self.data = self.data[1:]

  def peek(self):
    return self.data[0]


q = Queue()
print('testing q.data...')
assert q.data == []
print('PASSED')

q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print('testing q.enqueue...')
assert q.data == ['a', 'b', 'c']
print('PASSED')

q.dequeue()
print('testing q.dequeue...')
assert q.data == ['b', 'c']
print('PASSED')

print('testing q.peek...')
assert q.peek() == 'b'
print('PASSED')

print('testing q.data...')
assert q.data == ['b', 'c']
print('PASSED')
