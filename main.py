import pygame
import random
import sys
from framebuffer import FRAMEBUFFER_WIDTH, FRAMEBUFFER_HEIGHT, Color, framebuffer, point
from render import renderBuffer
CELL_SIZE = 4

WINDOW_WIDTH, WINDOW_HEIGHT = FRAMEBUFFER_WIDTH * CELL_SIZE, FRAMEBUFFER_HEIGHT * CELL_SIZE

def initialize_game():
    # Your initial pattern here
    for y in range(FRAMEBUFFER_HEIGHT):
        for x in range(FRAMEBUFFER_WIDTH):
            # Randomly set cells as alive (white) or dead (black)
            if random.random() < 0.3:
                point(x, y)

def update_game():
    new_framebuffer = [[Color(0, 0, 0) for _ in range(FRAMEBUFFER_WIDTH)] for _ in range(FRAMEBUFFER_HEIGHT)]

    for y in range(FRAMEBUFFER_HEIGHT):
        for x in range(FRAMEBUFFER_WIDTH):
            live_neighbors = count_live_neighbors(x, y)

            if framebuffer[y][x].r == 255:  # Cell is alive
                if live_neighbors < 2 or live_neighbors > 3:
                    # Cell dies due to underpopulation or overpopulation
                    new_framebuffer[y][x] = Color(0, 0, 0)
                else:
                    # Cell survives
                    new_framebuffer[y][x] = Color(255, 255, 255)
            else:  # Cell is dead
                if live_neighbors == 3:
                    # Cell comes to life due to reproduction
                    new_framebuffer[y][x] = Color(255, 255, 255)

    # Update the framebuffer
    for y in range(FRAMEBUFFER_HEIGHT):
        for x in range(FRAMEBUFFER_WIDTH):
            framebuffer[y][x] = new_framebuffer[y][x]

def count_live_neighbors(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue

            neighbor_x = x + i
            neighbor_y = y + j

            if 0 <= neighbor_x < FRAMEBUFFER_WIDTH and 0 <= neighbor_y < FRAMEBUFFER_HEIGHT:
                if framebuffer[neighbor_y][neighbor_x].r == 255:
                    count += 1

    return count

def main():
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Conway's Game of Life")

    initialize_game()

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_game()
        renderBuffer(screen)

        pygame.display.flip()

        # Delay to limit the frame rate
        clock.tick(1000)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
