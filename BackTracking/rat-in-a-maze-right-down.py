N = 3
maze = [[0,1,1],
        [0,0,0],
        [0,1,0]]
        
solution = [[0,0,0],
            [0,0,0],
            [0,0,0]]
            
            
def findSolution(x, y, solution):
    if x == N - 1 and y == N -1 and maze[x][y] == 0:
        solution[x][y] = 1
        return True
        
    if x < 0 or y < 0 or x >= N or y >= N or maze[x][y] == 1:
        return False
        
    solution[x][y] = 1
    
    if findSolution(x+1, y, solution):
        return True
        
    if findSolution(x, y+1, solution):
        return True
    
    solution[x][y] = 0
    
    
    
if findSolution(0,0,solution):
    for i in solution:
        print(i)
else:
    print("No path exists")   