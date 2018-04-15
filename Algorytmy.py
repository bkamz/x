from time import clock
import random

#GENEROWANIE DANYCH
data = []
for value in range(10000,100001,10000):
    data.append(random.sample(range(1, value + 1), value))

A = []
B = []

#PRZESZUKIWANIE TABLICY PO INDEKSACH
def arraysearch(scan, array):
    i = 0
    while scan != array[i]:
        i += 1
    return i


def quickSortMiddle(data):
    # quick z pivotem na środku
    less = []
    greater = []
    if len(data) < 2:
        return data
    else:
        pivot = data[len(data) // 2]

        for value in data[:data.index(pivot)]:
            if value <= pivot:
                less.append(value)
            else:
                greater.append(value)

        for value in data[data.index(pivot) + 1:]:
            if value <= pivot:
                less.append(value)
            else:
                greater.append(value)

        return quickSortMiddle(less) + [pivot] + quickSortMiddle(greater)


#KOPIOWANIE I SORTOWANIE TABLICY
def coppyArray(array_to_copy):
    B = [0]*len(array_to_copy)
    for n in range(len(array_to_copy)):
        B[n] = array_to_copy[n]
    quickSortMiddle(B)
    return B


#PRZESZUKIWANIE BINARNE
def binarySearch(scan, array):
    left = 0
    right = len(array)
    middle = right // 2
    while scan != array[middle]:
        middle = (left + right) // 2
        if scan > array[middle]:
            left = middle
        elif scan < array[middle]:
            right = middle
    return middle


# LISTA

class Lista:
    class Element:
        def __init__(self, initdata):
            self.data = initdata
            self.next = None

        def getData(self):
            return self.data

        def getNext(self):
            return self.next

        def setNext(self, nextelement):
            self.next = nextelement

    def __init__(self):
        self.head = None
        self.last = None

    def addelement(self, new):
        temp = self.Element(new)
        if self.head == None:
            self.head = temp
            self.last = temp
        else:
            temp2 = self.last
            self.last = temp
            temp2.setNext(temp)

    def search(self, scan):
        x = self.head
        i = 0
        while True:
            if x.getData() == scan:
                return
                # return i
            else:
                x = x.getNext()
                # i += 1


#DRZEWO PRZESZUKIWAŃ BINARNYCH
class Node:
        def __init__(self, initdata):
            self.data = initdata
            self.left = None
            self.right = None
        def goRight(self):
            return self.right
        def goLeft(self):
            return self.left
class Bst:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node
        else:
            current = self.root
            while 1 == 1:
                if data <= current.data:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                else:
                    if current.right != None:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break

    def search(self, scan):
        x = self.root
        while True:
            if x.data == scan:
                return
            elif scan > x.data:
                x = x.right
            elif scan < x.data:
                x = x.left

#TWORZENIE TABLICY DO ZRÓWNOWAŻONEGO DRZEWA

c = []
def middleTabToTree(arr, left, right):
    if right >= left:
        middle = (left + right) // 2
        C.append(arr[middle])
        middleTabToTree(arr, left, middle - 1)
        middleTabToTree(arr, middle + 1, right)


# WYKRESIKI
CB = []
SsB = []
SbB = []
CL = []
SL = []
STR = []
STB = []
CTB = []
CTR = []
hTR = []
hTB = []


def fillData(wykres, typ):
    czas = []
    ilosc = []

    for i in range(len(wykres)):
        czas.append(wykres[i][0])
        ilosc.append(wykres[i][1])
    plt.plot(ilosc, czas, typ)


#MIERZENIE CZASU KOPIOWANIA TABLICY
for partdata in data:
    start = clock()
    coppyArray(partdata*1)
    time = clock() - start
    print("CB\t{}\t{}".format(time,len(partdata)))
    CB.append([time, len(partdata)])
print("-------------------------------------")
print(CB)
print("-------------------------------------")



#MIERZENIE CZASU TWORZENIA LISTY

for partdata in data:
    L = Lista()
    elapsed_time = 0
    for i in range(len(partdata)):
        start = clock()
        L.addelement(partdata[i])
        time = clock() - start
        elapsed_time += time
    time = clock() - start
    print("CL\t{}\t{}".format(elapsed_time,len(partdata)))
    CL.append([elapsed_time, len(partdata)])
print("-------------------------------------")
print(CL)
print("-------------------------------------")

#CZAS TWORZENIA DRZEWA
for partdata in data:
    X = Bst()
    elapsed_time = 0
    for i in range(len(partdata)):
        start = clock()
        X.insert(partdata[i])
        time = clock() - start
        elapsed_time += time
    print("CTR\t{}\t{}".format(elapsed_time, len(partdata)))
    CTR.append([elapsed_time, len(partdata)])
print("-------------------------------------")
print(CTR)
print("-------------------------------------")


#CZAS TWORZENIA DRZEWA ZRÓWNOWAŻONEGO

for partdata in data:
    BTree = Bst()
    C = []
    newTab = middleTabToTree(sorted(partdata), 0, len(partdata) - 1)
    elapsed_time = 0
    for i in range(len(C)):
        start = clock()
        BTree.insert(C[i])
        time = clock() - start
        elapsed_time += time
    print("CTB\t{}\t{}".format(elapsed_time,len(partdata)))
    CTB.append([elapsed_time, len(partdata)])
print("-------------------------------------")
print(CTB)
print("-------------------------------------")


#MIERZENIE CZASU PRZESZUKIWANIA W LIŚCIE
for partdata in data:
    L = Lista()
    for i in range(len(partdata)):
        L.addelement(partdata[i])
    start = clock()
    for i in range(len(partdata)):
        L.search(partdata[i])
    time = clock() - start
    print("SL\t{}\t{}".format(time,len(partdata)))
    SL.append([time, len(partdata)])
print("-------------------------------------")
print(SL)
print("-------------------------------------")


#MIERZENIE CZASU PRZESZUKIWANIA POŁÓWKOWEGO
for partdata in data:
    sortedpartdata = sorted(partdata)
    start = clock()
    for i in range(len(partdata)):
        binarySearch(partdata[i], sortedpartdata)
    time = clock() - start
    print("SbB\t{}\t{}".format(time,len(partdata)))
    SbB.append([time, len(partdata)])
print("-------------------------------------")
print(SbB)
print("-------------------------------------")


#MIERZENIE CZASU PRZESZUKIWANIA W DRZEWIE BINARNYM
for partdata in data:
    Timetree = Bst()
    for i in range(len(partdata)):
        Timetree.insert(partdata[i])
    elapsed_time = 0
    for i in range(len(partdata)):
        start = clock()
        Timetree.search(partdata[i])
        time = clock() - start
        elapsed_time += time
    print("STB\t{}\t{}".format(elapsed_time,len(partdata)))
    STR.append([elapsed_time, len(partdata)])
print("-------------------------------------")
print(STR)
print("-------------------------------------")


#MIERZENIE CZASU PRZESZUKIWANIA W DRZEWIE ZRÓWNOWAŻONYM
for partdata in data:
    BTree = Bst()
    C = []
    newTab = middleTabToTree(sorted(partdata), 0, len(partdata) - 1)
    for i in range(len(partdata)):
        BTree.insert(partdata[i])
    elapsed_time = 0
    for i in range(len(partdata)):
        start = clock()
        X.search(partdata[i])
        time = clock() - start
        elapsed_time += time
    print("STR\t{}\t{}".format(elapsed_time,len(partdata)))
    STB.append([elapsed_time, len(partdata)])
print("-------------------------------------")
print(STB)
print("-------------------------------------")


# wysokość drzewa

class BstWithHeight:
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        node = Node(data)
        if self.root == None:
            self.root = node

        else:
            current = self.root
            while 1 == 1:
                if data <= current.data:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = Node(data)
                        break
                else:
                    if current.right != None:
                        current = current.right
                    else:
                        current.right = Node(data)
                        break

    def search(self, scan):
        x = self.root
        while True:
            if x.data == scan:
                return
            elif scan > x.data:
                x = x.right
            elif scan < x.data:
                x = x.left

    def height(self):
        return (height(self.root))


def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))


for partdata in data:
    SearchHTR = BstWithHeight()
    for i in range(len(partdata)):
        SearchHTR.insert(partdata[i])
    x = SearchHTR.height()
    hTR.append([x, len(partdata)])
    print("hTR\t{}\t{}".format(x, len(partdata)))

print("-------------------------")
print(hTR)
print("-------------------------------------")

for partdata in data:
    SearchHTB = BstWithHeight()
    C = []
    newTab = middleTabToTree(sorted(partdata), 0, len(partdata) - 1)
    for i in range(len(partdata)):
        SearchHTB.insert(C[i])
    x = (SearchHTB.height())
    hTB.append([x, len(partdata)])
    print("hTB\t{}\t{}".format(x, len(partdata)))

print("-------------------------------------")
print(hTB)
print("-------------------------------------")