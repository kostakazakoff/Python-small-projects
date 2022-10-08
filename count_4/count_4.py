from collections import deque
import time
import os


def in_gamepad(coin_r, coin_c):
    global ROWS, COLS
    if 0 <= coin_c < COLS and 0 <= coin_r < ROWS:
        return True
    return False


def player_win():
    global gamepad, EMPTY_SPACE, row, player_col_choice, player_coin

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
    for sub_directions in directions:
        coins = 0
        for direction in sub_directions:
            r, c = row, player_col_choice
            for _ in range(3):
                r, c = r + direction[0], c + direction[1]
                if not in_gamepad(r, c) or gamepad[r][c] != player_coin:
                    break
                coins += 1
            if coins == 3:
                return True
    return False


def drop_coin():
    global gamepad, ROWS, player_coin, player_col_choice, EMPTY_SPACE

    for r in range(ROWS):
        if r == ROWS - 1 or gamepad[r + 1][player_col_choice] != EMPTY_SPACE:
            gamepad[r][player_col_choice] = player_coin
            return r


def player_choice():
    global player_1_coin, player_2_coin, player_one_name, player_two_name
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"It's a simple game.\nDrop your coins into the columns.\nIf you have a line of 4 coins (in row, column or diagonal), you win the game.\nHave a fun :)\n")
    
    player_one_name = input('Player one, enter your name: ')
    player_two_name = input('Player two, enter your name: ')

    while True:
        player_1_coin = input(f'{player_one_name}, choose your coin symbol (O or X): ').upper()
        if player_1_coin not in 'XO':
            continue
        break

    player_2_coin = 'O' if player_1_coin == 'X' else 'X'
    print(f'{player_two_name}, you will play with {player_2_coin}')


# ------------------------------------------------------------------------------

ROWS, COLS = 6, 7
EMPTY_SPACE = ' '
gamepad = [[EMPTY_SPACE] * COLS for _ in range(ROWS)]

player_choice()
player_turn = deque([[player_one_name, player_1_coin], [player_two_name, player_2_coin]])

# -------------------------------------------------------------------------------

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    [print(f'| {" | ".join(r)} |') for r in gamepad]
    player, player_coin = player_turn[0]

    try:
        player_col_choice = int(input(f'\nChoose a column (between 1 and 7): ')) - 1
    except ValueError:
        print('Enter a valid number')
        time.sleep(2)
        continue

    if not 0 <= player_col_choice < 7:
        print('Enter a number between 1 and 7')
        time.sleep(2)
        continue

    if gamepad[0][player_col_choice] != EMPTY_SPACE:
        continue

    row = drop_coin()

    if player_win():
        os.system('cls' if os.name == 'nt' else 'clear')
        [print(f'| {" | ".join(r)} |') for r in gamepad]
        print(f"\nThe winner is {player}!")
        break

    player_turn.append(player_turn.popleft())

else:
    print(f'\nRemi')



