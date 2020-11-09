# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 07:12:03 2020

@author: Umer
"""
#Importing another file i've created named maze.py
#from the maze.py file import Maze class
from maze import Maze 

#Built-in modules
import queue, time, math

class astar(Maze):

    def main():
        """
        BFS uses queue data structure
        Queue implementation here
        Queue is First in First out data structure
        
        """
        #starting time
        
        t0 = time.time()
        
        
        nums = queue.Queue()
        nums.put("")
        add = ""
        maze = Maze.createMaze()
        
        while not Maze.findEnd(maze, add):
            add = nums.get()
            #print(add)
            for j in ["L", "R", "U", "D"]:
                put = add + j
        
                if Maze.valid(maze, put):
                    nums.put(put)
                    
        #Ending time
        
        t1 = time.time()
        
        #Ending time - starting time = time Elapsed
        
        total = t1-t0
        
        #Conversion of secs into mints
        
        mins = 0
        if total >=  60:
            mins = total // 60
            print("Time Elapsed: %s minute" % mins)
        else:
            print("Time Elapsed: %s second" % math.ceil(total))
            
e = astar
e.main()
        
# #if main() exist then call it
# if __name__=="__main__":
#     main()
        