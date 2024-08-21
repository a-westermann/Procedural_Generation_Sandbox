import random
import main
import helpers


def alg1(noise: [[str]], path_length: int) -> [[str]]:
    # pick a random point, find a path of desired length
    # returns the list of points along the path
    while True:
        py = random.randrange(0, len(noise))
        px = random.randrange(0, len(noise[0]))
        if noise[py][px] == main.on:
            continue
        print(f'Beginning path from {py}, {px}')
        path = []
        while len(path) < path_length:
            path.append((py, px))
            neighbors = helpers.get_neighbors(noise, py, px, False)
            off_neighbors = [n for n in neighbors if neighbors[n] == main.off and n not in path]
            if len(off_neighbors) == 0:
                break
            (py, px) = off_neighbors[random.randrange(0, len(off_neighbors))]

        if len(path) >= path_length:
            break  # found a path

    for (py, px) in path:
        noise[py][px] = 'O'
    return noise
