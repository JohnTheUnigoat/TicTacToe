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


print_field()

input()
