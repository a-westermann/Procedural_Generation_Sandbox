import random
import algs
import helpers

width = 100
height = 100
on = '#'
off = ' '
noise_density = 0.5

noise = []

if __name__ == '__main__':
    for y in range(height):
        noise.append([])
        for x in range(width):
            noise[-1] += on if random.random() > noise_density else off

    helpers.print_grid(noise, 'noise.txt')

    proc_gen = algs.alg1(noise, 20)
    helpers.print_grid(proc_gen, 'proc.txt')

