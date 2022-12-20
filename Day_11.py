source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_11/input.txt"

Monkey_dict = {}
inspected_items = {}

def Monkey_func2(monkey, item):

    inspected_items[monkey] += 1
    if monkey == 0:
        item = 19 * item
        if item % 17 == 0:
            monkey = 2
        else:
            monkey = 7
    elif monkey == 1:
        item = 2 + item
        if item % 19 == 0:
            monkey = 7
        else:
            monkey = 0
    elif monkey == 2:
        item = 7 + item
        if item % 7 == 0:
            monkey = 4
        else:
            monkey = 3
    elif monkey == 3:
        item = 1 + item
        if item % 11 == 0:
            monkey = 6
        else:
            monkey = 4
    elif monkey == 4:
        item = 5 * item
        if item % 13 == 0:
            monkey = 6
        else:
            monkey = 5
    elif monkey == 5:
        item = 5 + item
        if item % 3 == 0:
            monkey = 1
        else:
            monkey = 0
    elif monkey == 6:
        item = item * item
        if item % 5 == 0:
            monkey = 5
        else:
            monkey = 1
    elif monkey == 7:
        item = item + 3
        if item % 2 == 0:
            monkey = 2
        else:
            monkey = 3

    ## Part one
    ## item /= 3

    ## Part two
    item %= 17*19*7*11*13*3*5*2

    return monkey, item


with open(source) as f:
    file = f.read().splitlines()
    monkey = -1

    for row in file:
        if "Monkey" in row:
            m_n = row.split(" ")[1]
            monkey = int(m_n[0])
            Monkey_dict[monkey] = []
            inspected_items[monkey] = 0
        elif "Starting items" in row:
            items = row.split(" ")
            for el in items:
                if "," in el:
                    sub_el = el[0:el.index(',')]
                    Monkey_dict[monkey].append(int(sub_el))
            Monkey_dict[monkey].append(int(items[-1]))

    ## Part one
    ## for i in range(20):

    ## Part two
    for i in range(10000):
        for monkey in Monkey_dict:
            for i in range(len(Monkey_dict[monkey])):
                item = Monkey_dict[monkey][0]
                Monkey_dict[monkey].pop(0)
                new_monkey, item = Monkey_func2(monkey, item)
                Monkey_dict[new_monkey].append(item)
    
    print(inspected_items)
    print(156713*164077)
