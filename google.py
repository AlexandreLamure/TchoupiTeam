def getinformation(tab):
    tabnew = []
    index = 0
    length = len(tab)
    while index < length and tab[index] != "\n":
        number = 0
        while index < length and tab[index] not in ("\n", " "):
            number = number * 10 + int(tab[index])
            index += 1
        tabnew.append(number)
        index += 1
    return tabnew[0], tabnew[1], tabnew[2], tabnew[3]


def inmatrix(tabs, nbraw, nbcolumn):
    i = 0
    j = 0
    length = len(tabs)
    matrix = []
    while i < nbraw:
        j = 0
        tab = []
        while j < nbColumn:
            tab.append(tabs[i][j])
            j += 1
        matrix.append(tab)
        i += 1
    return matrix


def twodivisor(nb):
    index = 1
    tab = []
    while index <= nb:
        if nb % index == 0:
            tab.append((index, nb // index))
        index += 1
    return tab


def initmatrix(nbraw, nbcolumn, value):
    matrix = []
    for i in range(nbraw):
        tab = []
        for j in range(nbcolumn):
            tab.append(value)
        matrix.append(tab)
    return matrix


class Part:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1


def nboccu(matrix, value):
    nb = 0
    for i in matrix:
        for j in i:
            if j == value:
                nb += 1
    return nb


def nbeach_tm(matrix, part):
    nb_t = 0
    nb_m = 0
    for i in range(part.y0, part.y1+1):
        for j in range(part.x0, part.x1+1):
            if matrix[i][j] == "T":
                nb_t += 1
            else:
                nb_m += 1
    return min(nb_t, nb_m)


def nextpoint(realasematrix, value):
    for j in range(len(realasematrix[0])):
        for i in range(len(realasematrix)):
            if realasematrix[i][j] == value:
                return j, i


def validPoint(x, y, nbraw, nbcolumn):
    if x < 0 or x > nbcolumn or y < 0 or y > nbraw:
        return False
    else:
        return True


def validPart(realasematrix, part, value):
    if (validPoint(part.x0, part.y0, len(realasematrix), len(realasematrix[0])) and
            validPoint(part.x1, part.y1, len(realasematrix), len(realasematrix[0]))):
        for i in range(part.y0, part.y1):
            for j in range(part.x0, part.x1):
                if realasematrix[i][j] != value:
                    return False
        return True
    else:
        return False


def copymatrix(realasematrix):
    matrix = []
    for i in realasematrix:
        tab = []
        for j in i:
            tab.append(j)
        matrix.append(tab)
    return matrix


def updatematrix(realasematrix, part, value):
    matrix = copymatrix(realasematrix)
    for i in range(part.y0, part.y1 +1):
        for j in range(part.x0, part.x1 +1):
            matrix[i][j] = value
    return matrix


def recu(matrix, realasematrix, tabpart, nbeach, nbMax):
    if nboccu(realasematrix, 0) < nbMax:
        return tabpart
    else:
        for i in twodivisor(nbMax):
            a, b = i
            x0, y0 = nextpoint(realasematrix, 0)
            part = Part(x0, y0, x0 + a - 1, y0 + b - 1)
            if validPart(realasematrix, part, 0) and nbeach_tm(matrix, part) >= nbeach:
                tabpart.append(Part(x0, y0, x0 + a - 1, y0 + b - 1))
                for u in tabpart[len(tabpart)-1:]:
                    print("x0 = " + str(u.x0) + " / y0 = " + str(u.y0) + " / x1 = " + str(u.x1) + " / y1 = " + str(u.y1))
                return recu(matrix, updatematrix(realasematrix, part, 1), tabpart, nbeach, nbMax)
        return False



f = open("small.in", 'r')
lines = f.readlines()
nbRaw, nbColumn, nbEach, nbMax = getinformation(lines[0])
print(getinformation(lines[0]))
Matrix = inmatrix(lines[1:], nbRaw, nbColumn)



tab = (recu(Matrix, initmatrix(nbRaw, nbColumn, 0), [], nbEach, nbMax))

 #for u in tab:
  #  print("x0 = " + str(u.x0) + " / y0 = " + str(u.y0) + " / x1 = " + str(u.x1) + " / y1 = " + str(u.y1))
