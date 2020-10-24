#Set up field
width = int(input("Breite des Spielfeldes eingeben: "))
height = int(input("Höhe des Spielfeldes eingeben: "))

field = [[-1 for y in range(height)] for x in range(width)]

#Set up game
player1Turn = True

def wipe():

    global width
    global height
    global field

    width = 0
    height = 0
    field = 0

    width = int(input("Breite des Spielfeldes eingeben: "))
    height = int(input("Höhe des Spielfeldes eingeben: "))

    field = [[-1 for y in range(height)] for x in range(width)]


def drop(player1Turn,w,h,f):

    x = int(input("Spalte eingeben: "))-1
    while x > w-1:
        x = int(input("Spalte eingeben: "))-1
        print("Die Eingebene Zahl ist zu groß.")
    y = h-1

    while f[x][y] != -1:
        if(y >= 1):
            y -= 1
        else:
            return(player1Turn)
    f[x][y] = int(player1Turn)

    check(player1Turn,width,height,field)

    player1Turn = not player1Turn
    return(player1Turn)

def check(player1Turn,w,h,f):
    #Check vertical
    _streakVertical = 0

    for _x in range(w):
        for _y in range(h):
            if(f[_x][_y] == int(player1Turn)):

                _streakVertical += 1

            else:
                _streakVertical = 0
        #if _streakVertical >= 4, 4 in a row = win
        if(_streakVertical >= 4):
            print("Player "+str(int(player1Turn))+" you're winner")
            # Wipe the board and restart game
            wipe()
    #Check Hor

    _streakHorizontal = 0

    for _y in range(h):
        for _x in range(w):
            if(f[_x][_y] == int(player1Turn)):

                _streakHorizontal += 1

            else:
                _streakHorizontal = 0
        #if _streakVertical >= 4, 4 in a row = win
        if(_streakHorizontal >= 4):
            print("Player "+str(int(player1Turn))+" you're winner")
            # Wipe the board and restart game
            wipe()


def printField(w,h):
    global field


    string = " "

    for countY in range(h):
        for countX in range(w):
            string += "|" + str(field[countX][countY])
        print(string)
        string = " "







    print(string)


while(True):

    player1Turn = drop(player1Turn,width,height,field)
    printField(width,height)
