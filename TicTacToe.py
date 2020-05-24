win_comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]]
coordinates= [['1', '3'],  ['2', '3'], ['3', '3'], ['1', '2'], ['2', '2'], ['3', '2'], ['1', '1'], ['2', '1'], ['3', '1']]
x_comb, o_comb = [], []
digits = '0123456789'
player_moves = True
moves = ' ' * 9
def table():
    print("---------")
    print('| {} {} {} |'.format(moves[0], moves[1], moves[2]))
    print('| {} {} {} |'.format(moves[3], moves[4], moves[5]))
    print('| {} {} {} |'.format(moves[6], moves[7], moves[8]))
    print("---------")

def find_combs():
    global moves, x_comb, o_comb
    for i in range(moves.count('X')):
        x_comb.append(moves.find('X'))
        moves = moves.replace('X', '!', 1)
        
    for i in range(moves.count('O')):
        o_comb.append(moves.find('O'))
        moves = moves.replace('O', '?', 1)  

def winx():
    global x_comb, win_comb
    for i in range(8):
        if win_comb[i][0] in x_comb and win_comb[i][1] in x_comb and win_comb[i][2] in x_comb:
            return True 

def wino():
    global o_comb, win_comb
    for i in range(8):
        if win_comb[i][0] in o_comb and win_comb[i][1] in o_comb and win_comb[i][2] in o_comb:
            return True  

table()
while True:
    player = input("Enter the coordinates: ").split()
    if player[0] not in digits or player[1] not in digits:
        print("You should enter numbers!")
        continue
    elif player not in coordinates:
        print('Coordinates should be from 1 to 3!')
        continue
    elif moves[coordinates.index(player)] != ' ':
        print('This cell is occupied! Choose another one!')
        continue
    else:
        position = coordinates.index(player)
        if player_moves == True:
            moves = moves[:position] + 'X' + moves[position+1:]
            player_moves = False
        else:
            moves = moves[:position] + 'O' + moves[position+1:]
            player_moves = True
        table() 
        find_combs()
        moves = moves.replace('!', 'X')
        moves = moves.replace('?', 'O')
        if winx() == True:
            print('X wins')
            break
        elif wino() == True:
            print('O wins')
            break
        elif ' ' not in moves:
            print('Draw')
            break   
        x_comb, o_comb = [], []   