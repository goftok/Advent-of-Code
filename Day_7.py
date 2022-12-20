source = r"/Users/Helloworld/Desktop/input.txt"
import pandas as pd

index = 0
df = pd.read_csv(source, encoding = 'unicode_escape')
list = []
mini_list = []
all2 = 0
for index, row in df.iterrows():
    row = row["$ cd /"]

    if "$ cd" in row and "cd .." not in row:
        cd = row.split("cd ")[1]
        if mini_list != []:
            list.append(mini_list)
            mini_list = []
        mini_list.append(cd)
    elif "$" not in row:
        if "dir" in row:
            dir = row.split(" ")[1]
            mini_list.append(dir)
        else:
            nbr = row.split(" ")[0]
            all2 += int(nbr)
            mini_list.append(int(nbr))
    elif "cd .." in row:
        if mini_list != []:
            list.append(mini_list)
            mini_list = []
        list.append([".."])

list.append(mini_list)
res = 0

while(True):
    ind = list.index([".."])
    dir = list[ind-1][0]
    del list[ind-1][0]
    su = sum(list[ind-1])
    if su >= 1111105 and su <=1200000:
        print(su)
        res += su
    for i in range(1, len(list[ind-2])):
        if list[ind-2][i] == dir:
            ind_el = i
            break
    list[ind-2][ind_el] = su
    list.remove(list[ind])
    list.remove(list[ind-1])
    if [".."] not in list:
        break
all = 0
for sublist in list:
    su = 0
    for el in sublist:
        if type(el) == str:
            continue
        else:
            all += el
            su += el
            sublist[sublist.index(el)] = 0
    sublist.append(su)

print(all)
print(70000000 - all2)
print(70000000 - all2 - 30000000)

