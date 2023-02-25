
def Board(x,z):
    zero = "X" if x[0] else ("Z" if z[0] else 0)
    one = "X" if x[1] else ("Z" if z[1] else 1)
    two = "X" if x[2] else ("Z" if z[2] else 2)
    three = "X" if x[3] else ("Z" if z[3] else 3)
    four = "X" if x[4] else ("Z" if z[4] else 4)
    five = "X" if x[5] else ("Z" if z[5] else 5)
    six = "X" if x[6] else ("Z" if z[6] else 6)
    seven = "X" if x[7] else ("Z" if z[7] else 7)
    eight = "X" if x[8] else ("Z" if z[8] else 8)
    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")
    print("--|---|---")

def checkwin(x,z):
    wins = [[0,1,2],
           [3,4,5],
           [6,7,8],
           [0,3,6],
           [1,4,7],
           [2,5,8],
           [0,4,8],
           [2,4,6]]
    for i in wins:
        if x[i[0]]+ x[i[1]] + x[i[2]] == 3:
            print("X has won!!")
            return 1
        elif z[i[0]]+ z[i[1]] + z[i[2]] == 3:
            print("Z has won!!")
            return 0
    return -1
    

if __name__ == "__main__":
    x,z = [],[]
    for i in range(9):
        x.append(0)
        z.append(0)
    print("welcome to Tic Tac Toe game")
    turn = 1  #1 for X otherwise 0 for Z
    
    
    while True:
        Board(x,z)
        if turn == 1:
            print("X's chance")
            val = int(input("Enter the place where you want to tick your position"))
            x[val] = 1
        else:
            print("Z's chance")
            val = int(input("Enter the place where you want to tick your position"))
            z[val] = 1
        cwin = checkwin(x,z)
        if cwin!=-1:
            print("Match is over")
            break
        turn = 1-turn




    
