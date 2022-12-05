source = r"/Users/Helloworld/Desktop/input.txt"

with open(source) as f:
    counter = 0
    counter2 = 0
    for line in f.read().splitlines():
        list = []
        f, s = line.split(',')
        sm1, la1 = f.split('-')
        sm2, la2 = s.split('-')
        sm1 = int(sm1)
        sm2 = int(sm2)
        la1 = int(la1)
        la2 = int(la2)
        if (((sm1 <= sm2) and (la1 >= la2)) or ((sm2 <= sm1) and (la2 >= la1))):
            counter = counter + 1
        for i in range (sm1, la1+1):
            list.append(i)
        for i in range(sm2, la2+1):
            if i in list:
                counter2 = counter2 + 1
                break
    ## Part one
    print(counter)
    ## Part two
    print(counter2)
