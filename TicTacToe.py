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
    for i in range(3):
        print('     |     |')
        print(
            '  ' + cell_states[field[i][0]] + '  |' +
            '  ' + cell_states[field[i][1]] + '  |' +
            '  ' + cell_states[field[i][2]]
        )
        if i == 2:
            print('     |     |')
        else:
            print('_____|_____|_____')


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

    if field[x][y] != 0:
        return False

    if player_1:
        field[x][y] = 1
    else:
        field[x][y] = 2

    player_1 = not player_1
    return True


make_move()
print_field()

input()
