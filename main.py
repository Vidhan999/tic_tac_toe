def display(board):
    print(board[1] + '|' +board[2] + '|'+ board[3])
    print(board[4] + '|' +board[5] + '|'+ board[6])
    print(board[7] + '|' +board[8] + '|'+ board[9])

a= ['oo','X','O','X','O','X','O','X','O','X']

def value_in():
    marker = ""
    while not (marker == 'X' or marker == 'O'):
        marker = input(" Pick from X OR O: ").upper()

    if marker == 'X':
            return ('X','O')
    else:
            return ('O','X')


def pos(board,marker,position):
    board[position] = marker


def win(board,choice):
    return(board[1] == board[2] == board[3] ==choice) or (board[4] == board[5] == board[6] == choice) or(board[7] == board[8] == board[9] == choice) or(board[1] == board[4] == board[7] == choice) or(board[2] == board[5] == board[8] == choice) or(board[3] == board[6] == board[9] == choice) or(board[1] == board[5] == board[9] == choice) or(board[3] == board[5] == board[7] == choice)


import random
def choose():
    flip= random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"


def space_board(board,position):
    return board[position]==' '

def full_board(board):
    for i in range(1,10):
        if space_board(board,i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_board(board,position):
        position = int(input("Enter the position between 1 to 9: "))
    return position

def replay():
    choice = input("Keep playing yes or no: ")
    return choice=='yes'

print("Lets start the game")
while True:
    the_board =[' ']*10
    Player1_marker, Player2_marker = value_in()
    turn =choose()
    print(turn +' Will go first')
    play_game= input("Ready to play, y or n ")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    while game_on:
        if turn == 'Player 1':
            display(the_board)
            position =player_choice(the_board)
            pos(the_board,Player1_marker,position)
            if win(the_board,Player1_marker):
                display(the_board)
                print("Player 1 has won ")
                game_on = False
            else:
                if full_board(the_board):
                    display(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    print("Player 2 turn")
                    turn = 'Player 2'
        else:
            display(the_board)
            position = player_choice(the_board)
            pos(the_board,Player2_marker,position,)
            if win(the_board, Player2_marker):
                print("Player 2 has won")
                game_on = False
            else:
                if full_board(the_board)==True:
                    display(the_board)
                    print('Tie Game')
                    game_on = False
                else:
                    print("Player 1 turn")
                    turn = 'Player 1'
    if not replay():
        break