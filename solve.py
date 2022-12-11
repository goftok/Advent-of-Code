source = r"/Users/Helloworld/Desktop/input.txt"

worm_length = 10
tail_set1 = set()
tail_set2 = set()

position_list1 = [[0,0], [0,0]]
position_list2 = [[0,0] for i in range(worm_length)]


def solve1(dir, list_h, list_t, task2 = False):

    xh, yh = list_h[0], list_h[1]
    xt, yt = list_t[0], list_t[1]

    if task2 == False:
        if dir == "R":
           xh += 1 
        elif dir == "L":
           xh -= 1 
        elif dir == "U":
           yh += 1 
        elif dir == "D":
           yh -= 1 

    list_h[0] = xh
    list_h[1] = yh

    if xh == xt and yh == yt:
        return
    elif (yh == yt and abs(xh-xt) == 1) or (xh == xt and abs(yh-yt) == 1):
        return
    elif abs(xh-xt) == 1 and abs(yh-yt) == 1:
        return
    elif (abs(xh-xt) == 2 and yh == yt) or (xh == xt and abs(yh-yt) == 2):
        
        if yh == yt:
            if xh-xt > 0:
                xt += 1
            else:
                xt -= 1
        else:
            if yh-yt > 0:
                yt += 1
            else:
                yt -= 1
    else:

        if yh-yt > 0:
            yt += 1
        else:
            yt -= 1

        if xh-xt > 0:
            xt += 1
        else:
            xt -= 1

    list_t[0] = xt
    list_t[1] = yt


def to_ind(list):

    xt, yt = list[0], list[1]
    return "(" + str(xt) + "," + str(yt) + ")"


with open(source) as f:

    file = f.read().splitlines()
    for row in file:
        dir, number = row.split(" ")
        number = int(number)

        # Part one
        for i in range(number):
            solve1(dir, position_list1[0], position_list1[1])
            tail_set1.add(to_ind(position_list1[1]))

        # Part two 
        for i in range(number):
            for j in range(worm_length - 1):
                if j == 0:
                    solve1(dir, position_list2[j], position_list2[j+1])
                else:
                    solve1(dir, position_list2[j], position_list2[j+1], task2 = True)
                    if j == 8:
                        tail_set2.add(to_ind(position_list2[9]))

# Part one
print(len(tail_set1))
# Part two
print(len(tail_set2))
