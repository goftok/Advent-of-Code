source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_1/input.txt"

with open (source) as f:
    list = []
    s = 0
    for line in f.read().splitlines():
        if line == '':
            list.append(s)
            s = 0
        else:
            s = s + int(line)
    list.sort(reverse=True)
    ### Part one
    print (list[0])
    ### Part two
    print(list[0] + list[1] + list[2])