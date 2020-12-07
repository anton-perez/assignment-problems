def get_children(node, edges):
  children = []
  for edge in edges:
    if edge[0] == node:
      children.append(edge[1])
  return children

def get_parents(node, edges):
  parents = []
  for edge in edges:
    if edge[1] == node:
      parents.append(edge[0])
  return parents

def get_root(edges):
  for edge in edges:
    grandparent = get_parents(edge[0], edges)
    if grandparent == []:
      return [edge[0]]


edges = [('a','c'), ('e','g'), ('e','i'), ('e','a'), ('d','b'), ('a','d'), ('d','f'), ('f','h'), ('d','j'), ('d','k')]

print('Testing get_children...')
assert get_children('e', edges) == ['g', 'i', 'a']  
assert get_children('c', edges) == []
assert get_children('f', edges) == ['h']
print('PASSED')

print('Testing get_parents...')
assert get_parents('e', edges) == []
assert get_parents('c', edges) == ['a']
assert get_parents('f', edges) == ['d']
print('PASSED')

print('Testing get_root...')
assert get_root(edges) == ['e']
print('PASSED')