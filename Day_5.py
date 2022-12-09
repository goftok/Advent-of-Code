source = r"/Users/Helloworld/Desktop/input.txt"

with open(source) as f:
    dict = {}
    file = f.read()
    
    for line in file.splitlines():
        if '1' and '2' in line:
            number_line = line
            
            for i in range(0, len(line)-2, 4):
                dict[int(line[i+1])] = []
                
            break
            
    for line in file.splitlines():
        if line == number_line:
            break
            
        ind = 1
        
        for i in range(0, len(line), 4):
            if line[i+1] != ' ':
                dict[ind].append(line[i+1])
                
            ind = ind + 1
            
    for line in file.splitlines():
        if 'move' not in line:
            continue
            
        ind = line.find("move") + 5
        move_ind = line[ind]
        
        if ind + 1 != ' ':
            move_ind = line[ind: ind+2]
            
        move_ind = int(move_ind)
        from_ind = int(line[line.find("from") + 5])
        to_ind = int(line[line.find("to") + 3])
        
        for i in range(move_ind-1, -1, -1):
            ## Part one

            ## dict[to_ind].insert(0, dict[from_ind][0])
            ## dict[from_ind].pop(0)

            ## Part two

            dict[to_ind].insert(0, dict[from_ind][i])
            dict[from_ind].pop(i)
            
    for i in range (1, len(dict)+1):
        print(dict[i][0], end = "")
