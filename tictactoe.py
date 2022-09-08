import os

MAX_GAME_CYCLE = 5
WIN_CONDITION = ["O WINS","X WINS","DRAW"]
LOCATION = {1:"00",2:"01",3:"02",4:"10",5:"11",6:"12",7:"20",8:"21",9:"22"}
# print(WIN_CONDITION[winner])
xgroup = [1,-2,3,-4,5,6]

x_new = [x for x in xgroup if x<1]
print(x_new)

def layout():
    global winner,counter

    print("  ",game[0][0]," | ",game[0][1]," | ",game[0][2],"  ",sep='')
    print("-------------")
    print("  ",game[1][0]," | ",game[1][1]," | ",game[1][2],"  ",sep='')
    print("-------------")
    print("  ",game[2][0]," | ",game[2][1]," | ",game[2][2],"  ",sep='')

    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] == 'o':
            winner = 0
            counter = MAX_GAME_CYCLE
            break
        elif game[0][i] == game[1][i] == game[2][i] == 'o':
            winner = 0
            counter = MAX_GAME_CYCLE
            break
        elif game[i][0] == game[i][1] == game[i][2] == 'x':
            winner = 1
            counter = MAX_GAME_CYCLE
            break
        elif game[0][i] == game[1][i] == game[2][i] == 'x':
            winner = 1
            counter = MAX_GAME_CYCLE
            break
        
        if i == 0:
            if game[i][i] == game[i+1][i+1] == game[i+2][i+2] == 'o':
                winner = 0
                counter = MAX_GAME_CYCLE
                break
            elif game[i][2-i] == game[i+1][1-i] == game[i+2][0-i] == 'o':
                winner = 0
                counter = MAX_GAME_CYCLE
                break
            elif game[i][i] == game[i+1][i+1] == game[i+2][i+2] == 'x':
                winner = 1
                counter = MAX_GAME_CYCLE
                break
            elif game[i][2-i] == game[i+1][1-i] == game[i+2][0-i] == 'x':
                winner = 1
                counter = MAX_GAME_CYCLE
                break
        
counter = 0
winner = 2

game=[['1','2','3'],['4','5','6'],['7','8','9']]

layout()

while counter < MAX_GAME_CYCLE:

    pos_x = int(input("enter position for x : "))
    game[int(LOCATION[pos_x][0])][int(LOCATION[pos_x][1])]='x' 

    os.system('cls||clear')

    layout()

    if counter == MAX_GAME_CYCLE or counter == 4:
        break

    pos_o = int(input("enter position for o : "))
    game[int(LOCATION[pos_o][0])][int(LOCATION[pos_o][1])]='o'

    os.system('cls||clear')

    layout()

    counter +=1
    

print(WIN_CONDITION[winner])
