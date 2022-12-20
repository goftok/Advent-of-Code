source = r"/Users/Helloworld/Desktop/input.txt"

cycle_list = []
for i in range (20, 221, 40):
    cycle_list.append(i)

end_list = []
for i in range (0, 241, 40):
    end_list.append(i)

signal_strengths = []
image_list = []
image = ''

def find_cycle(cycle, value):
    for el in cycle_list:
        if el == cycle:
            print(el, value)
            signal_strengths.append(el*value)
            break

def draw_pixel(cycle, value):
    global image
    global cur_cucle
    position = cycle - 1 - cur_cucle
    if position in [value-1, value, value+1]:
        image += '#'
    else:
        image += '.'
    for el in end_list:
        if el == cycle:
            cur_cucle = el
            image_list.append(image)
            image = ''
            break

with open(source) as f:
    value = 1
    cycle = 0
    cur_cucle = 0

    file = f.read().splitlines()
    for row in file:
        if "addx" in row:
            number = row.split(" ")[1]
            number = int(number)
            cycle += 1
            find_cycle(cycle, value)
            draw_pixel(cycle, value)
            cycle += 1
            find_cycle(cycle, value)
            draw_pixel(cycle, value)
            value += number
        else:
            cycle += 1
            find_cycle(cycle, value)
            draw_pixel(cycle, value)


## Part one
## print(sum(signal_strengths))

## Part two
for el in image_list:
    print(el)