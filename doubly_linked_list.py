class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
    self.index = 0


class DoublyLinkedList:
  def __init__(self, head):
    self.head = Node(head)
  
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
    current_node.next = Node(data)
    current_node.next.prev = current_node
    current_node.next.index = i 
  
  def push(self, data):
    prev_head = self.head
    self.head = Node(data)
    self.head.next = prev_head
    prev_head.prev = self.head
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
    next_node.prev = prev_node
    current_node = prev_node
    while current_node.next != None:
      current_node.next.index -= 1
      current_node = current_node.next
    
  def insert(self, new_data, index):
    prev_node = self.get_node(index-1)
    next_node = self.get_node(index)
    insert_node = Node(new_data)
    insert_node.next = next_node
    insert_node.prev = prev_node
    insert_node.index = index
    prev_node.next = insert_node
    next_node.prev = insert_node
    current_node = insert_node
    while current_node.next != None:
      current_node.next.index += 1
      current_node = current_node.next

doubly_linked_list = DoublyLinkedList('a')
doubly_linked_list.append('c')
doubly_linked_list.append('d')
doubly_linked_list.append('e')
doubly_linked_list.insert('b',1)
doubly_linked_list.delete(3)

#Note: at this point, the list looks like this:
#a <--> b <--> c <--> e

current_node = doubly_linked_list.get_node(3)
node_values = [current_node.data]
for _ in range(3):
  current_node = current_node.prev
  node_values.append(current_node.data)
  
print('Testing attribute prev...')
assert node_values == ['e', 'c', 'b', 'a']
print('PASSED')