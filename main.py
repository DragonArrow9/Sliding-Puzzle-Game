import random

finished_tiles = [
    ['1 ', '2 ', '3 ', '4 '],
    ['5 ', '6 ', '7 ', '8 '],
    ['9 ', '10', '11', '12'],
    ['13', '14', '15', '  ']
]

tiles = [
    ['7 ', '2 ', '5 ', '  '],
    ['9 ', '3 ', '4 ', '13'],
    ['1 ', '15', '11', '6 '],
    ['10', '8 ', '12', '14']
]

r = random.SystemRandom()
r.shuffle(tiles)

def draw_board(tiles):
    print()
    print(f'+---+---+---+---+')
    print(f'| {tiles[0][0]}| {tiles[0][1]}| {tiles[0][2]}| {tiles[0][3]}|')
    print(f'+---+---+---+---+')
    print(f'| {tiles[1][0]}| {tiles[1][1]}| {tiles[1][2]}| {tiles[1][3]}|')
    print(f'+---+---+---+---+')
    print(f'| {tiles[2][0]}| {tiles[2][1]}| {tiles[2][2]}| {tiles[2][3]}|')
    print(f'+---+---+---+---+')
    print(f'| {tiles[3][0]}| {tiles[3][1]}| {tiles[3][2]}| {tiles[3][3]}|')
    print(f'+---+---+---+---+')
    print()

draw_board(tiles)

def move(direction, tiles, selected_tile):
    if direction == 'w':
        if tiles[selected_tile[0] - 1][selected_tile[1]] == '  ':
            tiles[selected_tile[0] - 1][selected_tile[1]] = tiles[selected_tile[0]][selected_tile[1]]
            tiles[selected_tile[0]][selected_tile[1]] = '  '
            draw_board(tiles)
        else:
            print('Error')
    
    if direction == 'a':
        if tiles[selected_tile[0]][selected_tile[1] - 1] == '  ':
            tiles[selected_tile[0]][selected_tile[1] - 1] = tiles[selected_tile[0]][selected_tile[1]]
            tiles[selected_tile[0]][selected_tile[1]] = '  '
            draw_board(tiles)
        else:
            print('Error')

    if direction == 's':
        if tiles[selected_tile[0] + 1][selected_tile[1]] == '  ':
            tiles[selected_tile[0] + 1][selected_tile[1]] = tiles[selected_tile[0]][selected_tile[1]]
            tiles[selected_tile[0]][selected_tile[1]] = '  '
            draw_board(tiles)
        else:
            print('Error')

    if direction == 'd':
        if tiles[selected_tile[0]][selected_tile[1] + 1] == '  ':
            tiles[selected_tile[0]][selected_tile[1] + 1] = tiles[selected_tile[0]][selected_tile[1]]
            tiles[selected_tile[0]][selected_tile[1]] = '  '
            draw_board(tiles)
        else:
            print('Error')


run = True
while run:
    selected_tile = tiles[0][0]
    input_tile = input('Which tile: ')
    for row in range(len(tiles)):
        for column in range(len(tiles[row])):
            if int(input_tile) < 10:
                if input_tile + ' ' == tiles[row][column]:
                    selected_tile = (row, column)
            else:
                if input_tile == tiles[row][column]:
                    selected_tile = (row, column)

    input_direction = input('Which direction (w, a, s, d): ')
    move(input_direction, tiles, selected_tile)

    if tiles == finished_tiles:
        print('You finished the puzzle!')
        print()
        run = False
        input = ('Press any key to exit. ')