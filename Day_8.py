source = r"/Users/Helloworld/Desktop/Advent-of-Code/Day_8/input.txt"

def to_id(r, c):
    return "(" + str(r) + ',' + str(c) + ")"

result_list = []
tree_set = set()

with open(source) as f:
    file = f.read().splitlines()
    size = len(file) - 1

    # Part one
    for r, row in enumerate(file):
        frst = -1

        for c, char in enumerate(row):
            if int(char) > frst:
                tree_set.add(to_id(r, c))
                frst = int(char)

        new_row = row[::-1]
        frst = -1

        for c, char in enumerate(new_row):
            if int(char) > frst:
                tree_set.add(to_id(r, 98 - c))
                frst = int(char)

    for i in range(0, size):
        row = ''

        for rw in file:
            row += rw[i]

        frst = -1
        
        for r, char in enumerate(row):
            if int(char) > frst:
                tree_set.add(to_id(r, i))
                frst = int(char)

        new_row = row[::-1]
        frst = -1

        for r, char in enumerate(new_row):
            if int(char) > frst:
                tree_set.add(to_id(98 - r, i))
                frst = int(char)
    # Part two
    for i in range(size):
        for j in range(size):

            our = int(file[i][j])
            left_r = file[i][0:j]
            left_r = left_r[::-1]
            rigth_r = file[i][j+1:size]
            new_row = ''

            for k in range(0, size):
                new_row += file[k][j]
            upper_c = new_row[0:i]
            upper_c = upper_c[::-1]
            down_c = new_row[i+1:size]
            str_list = [left_r, rigth_r, upper_c, down_c]
            list = []

            for sublist in str_list:
                counter = 0

                for char in sublist:
                    if int(char) < our:
                        counter += 1
                    else:
                        counter += 1
                        break

                list.append(counter)
            res = 1

            for el in list:
                res = el * res
            result_list.append(res)


# Part one
print(len(tree_set))

# Part two
print(max(result_list))
