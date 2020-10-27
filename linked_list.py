class Node:
  def __init__(self, data, next):
    self.data = data
    self.next = next
    self.index = 0


class LinkedList:
  def __init__(self, head):
    self.head = Node(head, None)
  
  def print_data(self):
    current_node = self.head
    while current_node.next != None:
      print(current_node.data)
      current_node = current_node.next
    print(current_node.data)

  def length(self):
    current_node = self.head
    node_counter = 1
    while current_node.next != None:
      node_counter +=1
      current_node = current_node.next
    return node_counter

  def append(self, data):
    current_node = self.head
    i = 1
    while current_node.next != None:
      current_node = current_node.next
      i += 1
    current_node.next = Node(data, None)
    current_node.next.index = i 
  
  def push(self, data):
    prev_head = self.head
    self.head = Node(data, prev_head)
    self.head.index = 0
    current_node = self.head
    while current_node.next != None:
      current_node.next.index += 1
      current_node = current_node.next
  
  def get_node(self, index):
    current_node = self.head
    while current_node.index != index:
      current_node = current_node.next
    return current_node

  def delete(self, index):
    prev_node = self.get_node(index-1)
    next_node = self.get_node(index+1)
    prev_node.next = next_node
    current_node = prev_node
    while current_node.next != None:
      current_node.next.index -= 1
      current_node = current_node.next
    
  def insert(self, new_data, index):
    prev_node = self.get_node(index-1)
    next_node = self.get_node(index)
    insert_node = Node(new_data, next_node)
    insert_node.index = index
    prev_node.next = insert_node
    current_node = insert_node
    while current_node.next != None:
      current_node.next.index += 1
      current_node = current_node.next



A = Node(4, None)
print('Testing attribute data...')
assert A.data == 4
print('PASSED')

print('Testing attribute next...')
assert A.next == None
print('PASSED')

B = Node(8, None)
A.next = B
print('Testing attribute data...')
assert A.next.data == 8
print('PASSED')

linked_list = LinkedList(4)
print('Testing attribute head...')
assert linked_list.head.data == 4
print('PASSED')

linked_list.append(8)
print('Testing method "append"...')
assert linked_list.head.next.data == 8
print('PASSED')

linked_list.append(9)

print('Testing method "print_data"...')
linked_list.print_data()

print('Testing method "list_length"...')
assert linked_list.length() == 3
print('PASSED')

linked_list = LinkedList('b')
linked_list.append('e')
linked_list.append('f')
linked_list.push('a')

assert linked_list.length() == 4

print('Testing attribute "index"...')
assert linked_list.head.index == 0
assert linked_list.head.next.index == 1
assert linked_list.head.next.next.index == 2
assert linked_list.head.next.next.next.index == 3
print('PASSED')

print('Testing method "get_node"...')
assert linked_list.get_node(0).data == 'a'
assert linked_list.get_node(1).data == 'b'
assert linked_list.get_node(2).data == 'e'
assert linked_list.get_node(3).data == 'f'
print('PASSED')

linked_list = LinkedList('a')
linked_list.append('b')
linked_list.append('c')
linked_list.append('d')
linked_list.append('e')
assert linked_list.length() == 5

linked_list.print_data()

print('Testing method "get_node"...')
assert linked_list.get_node(2).data == 'c'
print('PASSED')

print('Testing method "delete"...')
linked_list.delete(2)
assert linked_list.length() == 4
assert linked_list.get_node(2).data == 'd'
linked_list.print_data()
print('PASSED')

print('Testing method "insert"...')
linked_list.insert('f', 2)
assert linked_list.length() == 5
assert linked_list.get_node(2).data == 'f'
linked_list.print_data()
print('PASSED')