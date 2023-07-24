from color import Color

# Define the size of the framebuffer
FRAMEBUFFER_WIDTH = 120  # Ajusta este valor para tener más células en la pantalla
FRAMEBUFFER_HEIGHT = 120  # Ajusta este valor para tener más células en la pantalla

# Declare the framebuffer as a global variable
framebuffer = [[Color(0, 0, 0) for _ in range(FRAMEBUFFER_WIDTH)] for _ in range(FRAMEBUFFER_HEIGHT)]

def clear():
    for y in range(FRAMEBUFFER_HEIGHT):
        for x in range(FRAMEBUFFER_WIDTH):
            framebuffer[y][x] = Color(0, 0, 0)

def point(x, y):
    if 0 <= x < FRAMEBUFFER_WIDTH and 0 <= y < FRAMEBUFFER_HEIGHT:
        framebuffer[y][x] = Color(255, 255, 255)
