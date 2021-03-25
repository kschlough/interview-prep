# find path between nodes in adjacency matrix - path of 1s
# keep visiting nodes connected to current one being inspected - track back once no new nodes to visit
# use stack to keep track of path traveled to current node

# complexity: lookup can be done in O(1) constant time, but space taken up is O(v^2) where v = vertices
#         1  2  3  4  5
# mat =  1 [[1, 1, 0, 0, 0],
#        2 [0, 1, 1, 1, 1],
#        3 [1, 0, 0, 1, 1],
#        4 [0, 0, 0, 0, 1],
#        5 [1, 0, 1, 0, 1]]

# dfs
def dfs_is_path(matrix):
    
    def dfs_path(i, j, matrix, visited):

        node = matrix[i][j]
        if visited[node] == True:
            return
        
        visited[node] = True
        # visit surrounding nodes
        next_nodes = get_next(i, j, matrix)
        print("index", i, j)
        print("current node", node)
        for next in next_nodes:
            print(next)
        #     if node == 1:
   
        # if node == 1:

        # elif node == 0:
            # visit surrounding nodes
            # if first surrounding is no, try 2nd
            # if 2nd is no, return False
            
    def get_next(i, j, matrix):
        next = []
        if i + 1 < len(matrix) - 1:
            next.append([i + 1, j])
        if j + 1 < len(matrix[i]) - 1:
            next.append([i, j + 1])
        
        return next


    visited = [[False for row in matrix] for col in matrix]
    # print(visited)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            dfs_path(i, j, matrix, visited)
    # call the function

    



    

    
    
    
    

mat =  [[1, 1, 0, 0, 0],
       [0, 1, 1, 1, 1],
       [1, 0, 0, 1, 1],
       [0, 0, 0, 0, 1],
       [1, 0, 1, 0, 1]]
print(dfs_is_path(mat))