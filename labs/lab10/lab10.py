"""
Name: <Aidan Riordan>
<lab10>.py
"""
def build_board():
    position_list = [1,2,3,4,5,6,7,8,9]
    return position_list
def display_Board(position_list):
    counter = 0
    for i in range (1,4):
        print("|", end = "")
        for j in range(1,4):
            print(position_list[counter], end = "|")
            counter = counter + 1
        print(end = "\n")
        if i <3:
            print("-"*10, end="\n")


def place_spot(position_list, spot, marker):
    position_list[spot] = marker

def legal_spot(position_list, spot):
    if ((position_list[spot] =="x" or position_list[spot] == "o") or (spot+1<1 or spot+1>9)):
        return False
    else:
        return True

def game_winner(position_list):
    winCon = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    for condition in winCon:
        counter = 0
        for spot in condition:
            if position_list[spot-1] == "x":
                counter = counter + 1
            if counter ==3:
                return "x wins"
    for condition in winCon:
        counter = 0
        for spot in condition:
            if position_list[spot-1] == "o":
                counter = counter + 1
            if counter == 3:
                return "o wins"

def game_Over(position_list, turn_count):
    if ((game_winner(position_list) == "x wins") or (game_winner(position_list) =="o wins") or (turn_count>9)):
        return True
    else:
        return False

def Play_Game():
    position_list = build_board()
    display_Board(position_list)
    # to change y and x players
    p = 1
    turn_count = 1
    game_over = False
    while game_over != True:
        #only re display the board after the first loop
        if p > 1:
            display_Board(position_list)
            #every turn swap to y and x
        if p %2 == 0:
            spot = eval(input("Player x move 1-9"))-1
            marker = "x"
        else:
            spot = eval(input("Player o move 1-9"))-1
            marker = "o"
        #check if the move was legal
        if legal_spot(position_list, spot) == False:
            print("that is an illegal move. next turn")
        else:
            place_spot(position_list, spot, marker)
            turn_count = turn_count + 1
        if game_winner(position_list) == "x wins" or game_winner(position_list) == "o wins":
            print(game_winner(position_list))
            display_Board(position_list)
            break

        game_over = game_Over(position_list, turn_count)

        p = p + 1
    #display board
    #while game not over:
    #if legal place mark
    #increase turn couunt
    #checkk for wins
    #repeat for "x" or "o"




def main():
    # add other function calls here
    Play_Game()
    pass


main()


#list as parameter?? return what tictactoe