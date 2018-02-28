def getInformation(st):
    index = 0
    L = []
    while len(L) < 4:
        num = 0
        while st[index] != " " and st[index] != "\n":
            num = num * 10 + int(st[index])
            index += 1
        L.append(num)
        index += 1
    return L[0],L[1],L[2],L[3]

F = open("example.in","r")
s = F.read()
F.close()
print(s);
print(getInformation(s))

nbRow, nbColumn, minimum, maximum = getInformation(s)
