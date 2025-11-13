board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currntplayer = "X"
winner = None
gameRunning = True


# printing the game board
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input
def playerinput(board):
    inp = int(input("enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp - 1] == "-":
        board[inp - 1] = currntplayer
    else:
        print("Oops player is already in that spot!")


# check for win or tie 
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
   
def checkvertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    

def checkdiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
        
        
def checktie(board):
    global gameRunning
    if "-" not in board:
        printboard(board)
        print("It is a tie!")
        gameRunning = False

def checkwin():
    global gameRunning
    if checkhorizontal(board) or checkvertical(board) or checkdiagonal(board):
        print(f"The winner is {winner}!")
        gameRunning = False

# switch the player
def switchplayer():
    global currntplayer
    if currntplayer == "X":
        currntplayer = "O"
    else:
        currntplayer = "X"


# commented
def computer(board):
    while currntplayer == "O":
        import random
        inp = random.randint(0,8)
        if board[inp] == "-":
            board[inp] = "O"
            switchplayer()

# check for win or tie again

while gameRunning:
    printboard(board)
    playerinput(board)
    checkwin()
    checktie(board)
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)