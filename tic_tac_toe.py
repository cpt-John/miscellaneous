from os import system

mat = [['-' for i in range(3)] for j in range(3)]
player = 1
moves = 0


def validate(x, y, matrix):
    if x < 0 or x > 2:
        return False
    if y < 0 or y > 2:
        return False
    if matrix[y][x] != '-':
        return False
    return True


def result(m, x, y, char):
    # diagonal1
    d1 = m[0][0]+m[1][1]+m[2][2]
    # diagonal2
    d2 = m[0][2]+m[1][1]+m[2][0]
    # vertical
    v = m[0][x]+m[1][x]+m[2][x]
    # horizontal
    h = m[y][2]+m[y][1]+m[y][0]
    r = char*3
    if d1 == r or d2 == r or v == r or h == r:
        return True
    return False


def prntconsole(matrix):
    # use clear screen command for ur os this is for windows
    system('cls')
    for l in matrix:
        print('\n   ')
        for e in l:
            print(e, end='  ')
    print('\n   ')


prntconsole(mat)
while True:
    print('player', player)
    y = int(input("eneter cell row  "))-1
    x = int(input("eneter cell col  "))-1
    if validate(x, y, mat):
        car = 'x' if player == 1 else 'o'
        mat[y][x] = car
        moves += 1
        prntconsole(mat)
        if result(mat, x, y, car):
            print(f'player {player} wins')
            break
        if moves == 9:
            print('gmae is draw')
            break
        player = 2 if player == 1 else 1
    else:
        print("you can't do this")
