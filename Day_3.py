source = r"/Users/Helloworld/Desktop/input.txt"

with open (source) as f:
    s1 = 0
    s2 = 0
    temp = f.read().splitlines()
    it = iter(temp)
    for x, y, z in zip(it, it, it):
        for element in x:
            if element in y and element in z:
                x = x.replace(element, '')
                y = y.replace(element, '')
                z = z.replace(element, '')
                number = ord(element)-96
                if number > 0:
                    s1 += number
                else:
                    number = ord(element) - 64 + 26
                    s1 += number
    for line in temp:
        f = line[:int(len(line)/2)]
        s = line[int(len(line)/2):]
        for element in f:
            if element in s:
                s = s.replace(element, '')
                f = f.replace(element, '')
                number = ord(element) - 96
                if number > 0:
                    s2 += number
                else:
                    number = ord(element) - 64 + 26
                    s2 += number
    # Part one
    print(s1)
    #Part two
    print(s2)
