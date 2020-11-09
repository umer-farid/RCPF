from colorama import Fore
class Maze:
    def createMaze():
        """
        Simple Maze
        "O" is the starting point (Rabbit)
        "X" is the destination (Carrot)
        
        """
        maze = []
        maze.append(["#","#", "#", "#", "#", "O","#"])
        maze.append(["#"," ", " ", " ", "#", " ","#"])
        maze.append(["#"," ", "#", " ", "#", " ","#"])
        maze.append(["#"," ", "#", " ", " ", " ","#"])
        maze.append(["#"," ", "#", "#", "#", " ","#"])
        maze.append(["#","X", " ", " ", "#", " ","#"])
        maze.append(["#","#", "#", "#", "#", "#","#"])
    
        return maze
    
    def createMaze1():
        """
        Complex Maze, it takes 5 mints to find the shortest path in my system.
        Depends upon your system specs.
        
        """
        maze = []
        maze.append(["O"," ", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
        maze.append(["#"," ", "#", " ", "#", " ", " ", " ", "#", " ", "#"])
        maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#", " ", "#"])
        maze.append(["#"," ", " ", " ", " ", " ", "#", " ", " ", " ", "#"])
        maze.append(["#"," ", "#", " ", "#", "#", "#", "#", "#", " ", "#"])
        maze.append(["#"," ", "#", " ", "#", " ", " ", "X", " ", " ", "#"])
        maze.append(["#"," ", "#", " ", "#", "#", "#", " ", "#", " ", "#"])
        maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#", " ", "#"])
        maze.append(["#"," ", "#", " ", " ", " ", "#", " ", " ", " ", "#"])
        maze.append(["#"," ", "#", "#", "#", " ", "#", " ", "#", "#", "#"])
        maze.append(["#"," ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
        maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    
    
        return maze
        
    
    def printMaze(maze, path=""):
        """
        It prints the whole structure of the maze when the shortest path calculated!
        param: maze object that creates the maze
        param: path left, right, up, down
        """
        for x, pos in enumerate(maze[0]):
            if pos == "O":
                start = x
    
        i = start
        j = 0
        pos = set()
        for move in path:
            if move == "L":
                i -= 1
    
            elif move == "R":
                i += 1
    
            elif move == "U":
                j -= 1
    
            elif move == "D":
                j += 1
            pos.add((j, i))
        
        for j, row in enumerate(maze):
            for i, col in enumerate(row):
                if (j, i) in pos:
                    print(Fore.GREEN + "+ " + Fore.RESET, end="")
                else:
                    print(col + " ", end="")
            print()
            
    
    
    def valid(maze, moves):
        """
        It validate moves and check the surroundings if any obstacle exist or not
        param: maze it create the maze
        param: moves it validate moves, obstacales "#"
        """
        for x, pos in enumerate(maze[0]):
            if pos == "O":
                start = x
    
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
    
            elif move == "R":
                i += 1
    
            elif move == "U":
                j -= 1
    
            elif move == "D":
                j += 1
    
            if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
                return False
            elif (maze[j][i] == "#"):
                return False
    
        return True
    
    
    def findEnd(maze, moves):
        """
        Find the carrot.  If found then it prints out the maze with moves(L, R, U, D)
        
        """
        for x, pos in enumerate(maze[0]):
            if pos == "O":
                start = x
    
        i = start
        j = 0
        for move in moves:
            if move == "L":
                i -= 1
    
            elif move == "R":
                i += 1
    
            elif move == "U":
                j -= 1
    
            elif move == "D":
                j += 1
        
        if maze[j][i] == "X":
            Maze.printMaze(maze, moves)
            print(Fore.RED + "Moves: " + Fore.GREEN + moves + Fore.RESET)
            return True
        return False

