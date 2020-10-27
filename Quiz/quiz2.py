print([[1 if col_index ==row_index or row_index-1 == col_index else 0 for col_index in range(4) ] for row_index in range(4)])
print([i for i in range(1,1001) if '3' in str(i)])
print([[(4-row_index)*2 -(col_index + 2*(row_index)) for col_index in range(4)] for row_index in range(2)])