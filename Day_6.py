source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_6/input.txt"
# Part one
number = 7
# Part two
# number = 14
with open(source) as f:
    line = f.read().splitlines()[0]
    for i in range (0, len(line)):
        list = []
        flag = True
        for j in range(i ,i+number):
            if j < len(line):
                list.append(line[j])

        for j in range(number):
            if list.count(list[j]) != 1:
                flag = False
                break
            
        if flag == True:
            break

print(i+number)
