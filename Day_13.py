import numpy as np
import re

source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_13/input.txt"

class test:

    def __init__(self):
        self.not_correct = False
        self.correct = False
        self.indices_list = list()
        self.indeces_dict =  dict()
        self.main()
        self.part_two()
        self.solve()


    def check_two_lists(self, first_list, second_list):
        if self.not_correct == True:
            return
        if self.correct == True:
            return

        for i in range(len(first_list)):

            if self.not_correct == True:
                return
            if self.correct == True:
                return
            if i >= len(second_list):
                self.not_correct = True
                return

            else:
                if (type(first_list[i]) == list and type(second_list[i]) == list):
                    self.check_two_lists(first_list[i], second_list[i])

                elif(type(first_list[i]) == list and type(second_list[i]) != list):
                    self.check_two_lists(first_list[i], [second_list[i]])

                elif(type(first_list[i]) != list and type(second_list[i]) == list):
                    self.check_two_lists([first_list[i]], second_list[i])

                else:
                    if first_list[i] > second_list[i]:
                        self.not_correct = True
                        return
                    elif first_list[i] < second_list[i]:
                        self.correct = True
                        return

        for i in range(len(second_list)):
            if self.not_correct == True:
                return
            if self.correct == True:
                return
            if i >= len(first_list):
                self.correct = True
                return


    def part_two(self):
        self.indeces_dict[len(self.indeces_dict)] = [[2]]
        self.indeces_dict[len(self.indeces_dict)] = [[6]]

        for i in range(len(self.indeces_dict)):
            for j in range(0, len(self.indeces_dict) - i - 1):
                self.check_two_lists(self.indeces_dict[j], self.indeces_dict[j+1])
                if self.not_correct == True:
                    temp = self.indeces_dict[j]
                    self.indeces_dict[j] = self.indeces_dict[j+1]
                    self.indeces_dict[j+1] = temp

                self.not_correct = False
                self.correct = False


    def main(self):
        with open(source) as f:
            pair = 1

            for line in f:
                first_list = eval(line)
                line = f.readline()
                second_list = eval(line)
                self.check_two_lists(first_list, second_list)
                f.readline()

                if self.correct == True:
                    self.indices_list.append(pair)
                self.indeces_dict[2* pair - 2] = first_list
                self.indeces_dict[2* pair - 1] = second_list
                pair += 1

                self.not_correct = False
                self.correct = False


    def solve(self):
        ## Part one
        print(sum(self.indices_list))
        
        ## Part two
        f = 0
        s = 0
        for key in self.indeces_dict:
            if self.indeces_dict[key] == [[2]]:
                f = key + 1
            elif self.indeces_dict[key] == [[6]]:
                s = key + 1
        print(f*s)

test()





                
    
    
