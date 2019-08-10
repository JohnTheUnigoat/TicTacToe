cell_states = {
    0: ' ',
    1: 'X',
    2: 'O'
}

field = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

player_1 = True


def print_field():
    print('    |  1  |  2  |  3  |')
    print(' ___|_____|_____|_____|')

    for i in range(3):
        print('    |     |     |     |')
        print(
            ' ' + str(i + 1) + '  |  ' + cell_states[field[i][0]] + '  |' +
            '  ' + cell_states[field[i][1]] + '  |' +
            '  ' + cell_states[field[i][2]] + '  |'
        )
        print(' ___|_____|_____|_____|')


def make_move():
    global player_1

    if player_1:
        print('Player 1', end='')
    else:
        print('Player 2', end='')

    print(', make a move!')
    while True:
        try:
            x, y = map(int, input('Enter the coordinates: ').split())
        except ValueError:
            print('Please enter two numbers separated with a space!')
            continue

        if not 0 < x < 4 or not 0 < y < 4:
            print('Make sure each coordinate is between 1 and 3!')
        else:
            break

    x -= 1
    y -= 1

    if field[y][x] != 0:
        return False

    if player_1:
        field[y][x] = 1
    else:
        field[y][x] = 2

    player_1 = not player_1
    return True


def win():
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] != 0:
            return True
        if field[0][1] == field[1][i] == field[2][i] != 0:
            return True

    if field[0][0] == field[1][1] == field[2][2] != 0:
        return True
    if field[2][0] == field[1][1] == field[0][2] != 0:
        return True

    return False


while not win():
    print_field()

    move_successful = False
    while not move_successful:
        move_successful = make_move()

print_field()

if player_1:
    print('Player 2', end='')
else:
    print('Player 1', end='')

print(' wins!')

input('Press Enter to exit...')

# This commit is just to test the author name and email
