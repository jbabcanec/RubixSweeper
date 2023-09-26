import pygame
from rubix import Rubix
from build import exported_settings

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CUBE_SIZE = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rubix Minesweeper")
clock = pygame.time.Clock()

# Initialize a Rubix instance with dimensions
size = 3  # For a 3x3 face
mines = 4  # Number of mines on each face
rubix = Rubix(size=size, mines=mines)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dynamic Grid Drawing
    x, y = 100, 100  # Starting position for drawing the "front" face
    front_face = rubix.get_face('front')
    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, WHITE, (x + i * CUBE_SIZE, y + j * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), 1)
            font = pygame.font.SysFont(None, 36)
            text_surface = font.render(str(front_face[i][j]), True, GREEN)
            screen.blit(text_surface, (x + i * CUBE_SIZE + 15, y + j * CUBE_SIZE + 15))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
