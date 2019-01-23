import copy


def grot(matrix):
    coordinates = []
    most_moves = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            x, y = i, j
            moves = 0
            copy_mx = copy.deepcopy(matrix)
            prev = ''
            while len(copy_mx) > x > -1 and len(copy_mx[x]) > y > -1:
                if copy_mx[x][y] == 'u':
                    moves += 1
                    copy_mx[x][y] = ''
                    x -= 1
                    prev = 'u'
                elif copy_mx[x][y] == 'd':
                    moves += 1
                    copy_mx[x][y] = ''
                    x += 1
                    prev = 'd'
                elif copy_mx[x][y] == 'r':
                    moves += 1
                    copy_mx[x][y] = ''
                    y += 1
                    prev = 'r'
                elif copy_mx[x][y] == 'l':
                    moves += 1
                    copy_mx[x][y] = ''
                    y -= 1
                    prev = 'l'
                elif prev == 'd':
                    x += 1
                elif prev == 'r':
                    y += 1
                elif prev == 'l':
                    y -= 1
                else:
                    x -= 1
            if moves > most_moves:
                most_moves = moves
                coordinates = [i, j]
    return coordinates
