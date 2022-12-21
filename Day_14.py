import numpy as np
import re

source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_14/input.txt"

class test:

    def __init__(self):
        self.indices_set = set()
        self.maximum_y = 0
        self.result = 0
        self.main()
        self.count_sand()
        self.solve()

    def to_index(self, x, y):
        return "("+str(x)+","+str(y)+")"

    def get_indices_set(self, indices_list):
        prev_x, prev_y = -1, -1
        for coord in indices_list:
            x, y = coord.split(",")
            x, y = int(x), int(y)

            if x == prev_x:
                if y > prev_y:
                    for y1 in range(prev_y, y +1, 1):
                        self.indices_set.add(self.to_index(x, y1))
                else:
                    for y1 in range(prev_y, y - 1, -1):
                        self.indices_set.add(self.to_index(x, y1))

            elif y == prev_y:
                if x > prev_x:
                    for x1 in range(prev_x, x + 1, 1):
                        self.indices_set.add(self.to_index(x1, y))
                else:
                    for x1 in range(prev_x, x -1, -1):
                        self.indices_set.add(self.to_index(x1, y))

            if y > self.maximum_y:
                self.maximum_y = y

            prev_x = x
            prev_y = y

    
    def count_sand(self):

        ## Part two
        self.maximum_y += 2

        #################
        
        flag = True
        while (True):
            c_x, c_y = 500, 0
            while(True):
                if c_y == self.maximum_y - 1:
                    self.indices_set.add(self.to_index(c_x, c_y))
                    self.result += 1
                    break

                ## Part one

                ## elif c_y > self.maximum_y:
                ##     flag = False
                ##     break

                #################
                elif self.to_index(c_x, c_y+1) not in self.indices_set:
                    c_y += 1
                elif self.to_index(c_x - 1, c_y + 1) not in self.indices_set:
                    c_x -= 1
                    c_y += 1
                elif self.to_index(c_x + 1, c_y + 1) not in self.indices_set:
                    c_x += 1
                    c_y += 1
                else:
                    self.indices_set.add(self.to_index(c_x, c_y))

                    ## Part two

                    if c_y == 0:
                        flag = False

                    #################
                        
                    self.result += 1
                    break
            
            if flag == False:
                break


    def main(self):
        with open(source) as f:
            for line in f:
                match = re.findall("\d+,\d+", line)
                self.get_indices_set(match)


    def solve(self):
        print(self.result)
        
test()





                
    
    