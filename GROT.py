import copy


def grot(matrix):
    coordinates = []
    most_moves = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x, y = j, i
            moves = 0
            copy_mx = copy.deepcopy(matrix)
            prev = ''
            while len(copy_mx) > y > -1 and len(copy_mx[y]) > x > -1:
                if copy_mx[y][x] == 'u':
                    moves += 1
                    copy_mx[y][x] = ''
                    y -= 1
                    prev = 'u'
                elif copy_mx[y][x] == 'd':
                    moves += 1
                    copy_mx[y][x] = ''
                    y += 1
                    prev = 'd'
                elif copy_mx[y][x] == 'r':
                    moves += 1
                    copy_mx[y][x] = ''
                    x += 1
                    prev = 'r'
                elif copy_mx[y][x] == 'l':
                    moves += 1
                    copy_mx[y][x] = ''
                    x -= 1
                    prev = 'l'
                elif prev == 'd':
                    y += 1
                elif prev == 'r':
                    x += 1
                elif prev == 'l':
                    x -= 1
                else:
                    y -= 1
            if moves > most_moves:
                most_moves = moves
                coordinates = [i, j]
    return coordinates
