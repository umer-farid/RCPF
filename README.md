# Rabbit Carrot Path Finding

    Developer: Umer Farid
    
    Algorithm: BFS

    Data Structure: Queue

    Code Editor: Spyder


# How to run?

    cmd windows: python solve.py

    Or Run solve.py in your code editor

You can also change the maze from simple to complex structure

# Maze.createMaze()

    O represents the starting point of Rabbit 

    X represents the carrot and that is the destination point

    We've to calculate the shortest path from start to destination\
    
# Maze.printMaze(maze, path="")

    It prints the whole structure of the maze when the shortest path calculated!
    
    param: maze object that creates the maze
    
    param: path left, right, up, down
    
# Maze.valid(maze, moves):
        
    It validate moves and check the surroundings if any obstacle exist or not
    
    param: maze it create the maze
    
    param: moves it validate moves, obstacales "#"

# Maze.findEnd(maze, moves):
       
    Find the carrot.  If found then it prints out the maze with moves(L, R, U, D)
    
# astar.main():

    BFS uses queue data structure
    
    Queue implementation here
    
    Queue is First in First out data structure
        
       
