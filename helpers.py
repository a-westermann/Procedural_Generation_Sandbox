

def get_neighbors(noise, y, x, diagonals: bool) ->  dict[tuple[int, int], str]:
    neighbors = dict()
    for y2 in range(-1, 2):
        for x2 in range(-1, 2):
            if not diagonals and abs(y2) + abs(x2) > 1:
                continue
            if y2 == x2 == 0:
                continue
            py = y + y2
            px = x + x2
            if 0 <= py < len(noise) and 0 <= px < len(noise[0]):
                neighbors[(py, px)] = noise[py][px]
    return neighbors


def print_grid(grid, name):
    image = open(name, 'w')
    for column in grid:
        image.write(''.join(column) + '\n')
