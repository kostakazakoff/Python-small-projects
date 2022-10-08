from collections import deque
import os


def valid_position(r, c):
    if 0 <= r < 3 and 0 <= c < 3:
        return True
    return False


def start():
    player_one = input('Player one: ')
    player_two = input('Player two: ')

    while True:
        player_one_symbol = input(f'{player_one}, enter your symbol (X or O): ').upper()
        if player_one_symbol not in 'XO':
            print(f'{player_one} please, select a valid option')
            continue
        break

    player_two_symbol = 'X' if player_one_symbol == 'O' else 'O'

    players.append([player_one, player_one_symbol])
    players.append([player_two, player_two_symbol])


def print_game(begin=False):
    global gamepad

    if begin:
        print('This is the numeration of the board:')
        [print(f'| {" | ".join(r)} |') for r in gamepad]
        gamepad = [['_'] * 3 for _ in range(3)]
        print(f'{players[0][0]} starts first!')

    else:
        [print(f'| {" | ".join(r)} |') for r in gamepad]


def choose_position():
    while True:
        try:
            position = int(input(f'{players[0][0]}, choose a free position (1 - 9): ')) - 1
        except ValueError:
            print(f'{players[0][0]}, choose a number between 1 and 9')
            continue
        
        row = position // 3
        col = position % 3
        
        if not valid_position(row, col) or gamepad[row][col] in ('X', 'O'):
            continue

        pos_row, pos_col = position // 3, position % 3
        gamepad[pos_row][pos_col] = players[0][1]
        break

    return pos_row, pos_col


def check_for_line(win=False, equality=False):
    directions = (
        ((1, 0),
        (-1, 0)),
        ((0, 1),
        (0, -1)),
        ((-1, -1),
        (1, 1)),
        ((-1, 1),
        (1, -1))
    )
    for subdirections in directions:
        line = 0
        for side in (subdirections[0], subdirections[1]):
            r, c = player_row, player_col
            
            for _ in range(2):
                r, c = r + side[0], c + side[1]
                if not valid_position(r, c) or gamepad[r][c] != players[0][1]:
                    break                
                line += 1

            if line == 2:
                print(f'{players[0][0]} won!')
                win = True

    full_pad = all([all([col in 'XO' for col in row]) for row in gamepad])
    equality = full_pad and not win
    if equality:
        print('Draw!')

    return win, equality


players = deque()
gamepad = [[str(r), str(r + 1), str(r + 2)] for r in range(1, 10, 3)]
begin = True
player_wins, draw = False, False

os.system('cls' if os.name == 'nt' else 'clear')
start()
os.system('cls' if os.name == 'nt' else 'clear')

print_game(True)
while not player_wins and not draw:
    player_row, player_col = choose_position()
    os.system('cls' if os.name == 'nt' else 'clear')
    print_game()
    player_wins, draw = check_for_line()
    players.append(players.popleft())
