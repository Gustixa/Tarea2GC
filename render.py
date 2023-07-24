import pygame
import numpy as np
from framebuffer import framebuffer, FRAMEBUFFER_WIDTH, FRAMEBUFFER_HEIGHT

def renderBuffer(renderer):
    frame_array = np.zeros((FRAMEBUFFER_HEIGHT, FRAMEBUFFER_WIDTH, 3), dtype=np.uint8)
    for y in range(FRAMEBUFFER_HEIGHT):
        for x in range(FRAMEBUFFER_WIDTH):
            frame_array[y, x] = (framebuffer[y][x].r, framebuffer[y][x].g, framebuffer[y][x].b)

    surface = pygame.surfarray.make_surface(frame_array)
    surface = pygame.transform.scale(surface, (FRAMEBUFFER_WIDTH * 5, FRAMEBUFFER_HEIGHT * 5))

    renderer.blit(surface, (0, 0))

def render():
    pass
