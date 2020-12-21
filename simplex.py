#import numpy as np

def main():
    print("Welcome to Python program for Simplex Method. Please enter your standard LP problem (minimization is assumed).")
    m = int(input("Number of equations: "))
    n = int(input("Number of variables: "))

    c = runList(input("Cost coeff (c): ").split(" "))
    # A = input("Matrix: ").split(";")
    A = list(map(lambda x: runList(x.split(" ")), input("Matrix: ").split(";")))
    b = runList(input("Constraint coeff (b): ").split(" "))

    # Simplex tableau
    tab = constructTab(A, b, c, m, n)

    print(tab)
    
    for k in range(3):
    # while(not(isOptimal(tab))):
        for j in range(len(tab)):
            if tab[0][j] > 0 and allNeg(tab, j):
                print("-Inf")
                break

        postIndices = []
        for j in range(len(tab[0])-1):
            if tab[0][j] > 0:
                postIndices.append(j)
        col = blandChooseCol(tab, postIndices)
        row = findMin(tab, col)
        print(row, col)
        
        tab = ERO(tab, row, col)

        print(tab)

    print(tab[0][-1])

def runList(li):
    newList = []
    for l in li:
        if l.find("/") == -1:
            try:
                newList.append(float(l))
            except:
                if l == "M": newList.append(float(100000))
                continue
        else:
            newList.append(int(l[:l.find("/")])/int(l[l.find("/")+1:]))
    return newList
    # return li

def constructTab(A, b, c, m, n):
    tab = [[0 for i in range(n+1)] for j in range(m+1)]
    # print(tab)

    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if i == 0 and j != len(tab[i])-1:
                tab[i][j] = c[j]
            elif i == 0 and j == len(tab[i])-1:
                continue
            else:
                if j == len(tab[i])-1:
                    tab[i][j] = b[i-1]
                else:
                    tab[i][j] = A[i-1][j]
    
    return tab

def isOptimal(tab):
    for i in range(len(tab[0])-1):
        if i > 0: return False
    return True

def allNeg(tab, j):
    for i in range(1, len(tab[0])):
        if tab[i][j] > 0:
            return False
    return True

def blandChooseCol(tab, postIndices):
    return min(postIndices)

def dantzigChooseCol(tab, postIndices):
    values = []
    for i in range(postIndices):
        values.append(tab[i])
    return min(values)

def findMin(tab, col):
    values = []
    indices = []
    for i in range(1, len(tab)):
        if tab[i][col] > 0:
            values.append(tab[i][-1]/tab[i][col])
            indices.append(i)
    return indices[values.index(min(values))]

def ERO(tab, row, col):
    tab[row] = list(map(lambda x: x / tab[row][col], tab[row]))
    
    for i in range(len(tab)):
        if i == row: continue
        else:
            tab[i] = list(map(lambda x: x - x * tab[row][col], tab[row]))

    return tab

if __name__ == "__main__":
    main()