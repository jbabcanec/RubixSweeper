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
RED = (255, 0, 0)

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
    screen.fill(BLACK)  # Clear the screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            grid_x, grid_y = (mouse_x - 100) // CUBE_SIZE, (mouse_y - 100) // CUBE_SIZE

            # Check if the click is inside the grid
            if 0 <= grid_x < size and 0 <= grid_y < size:
                if event.button == 1:  # Left click to reveal
                    rubix.reveal_cell('front', grid_x, grid_y)
                elif event.button == 3:  # Right click to flag
                    rubix.flag_cell('front', grid_x, grid_y)  # flag_cell method needs to be implemented in Rubix
                    print(f"After flag_cell call, flagged status: {rubix.get_flagged('front')}")

    
    # Dynamic Grid Drawing
    x, y = 100, 100  # Starting position for drawing the "front" face
    front_face = rubix.get_face('front')
    front_revealed = rubix.get_revealed('front')
    front_flagged = rubix.get_flagged('front')

    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, WHITE, (x + i * CUBE_SIZE, y + j * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), 1)
            
            if front_revealed[i][j]:  # Check if this cell is revealed
                font = pygame.font.SysFont(None, 36)
                text_surface = font.render(str(front_face[i][j]), True, GREEN)
                screen.blit(text_surface, (x + i * CUBE_SIZE + 15, y + j * CUBE_SIZE + 15))
            
            elif front_flagged[i][j]:  # Check if this cell is flagged
                pygame.draw.line(screen, RED, (x + i * CUBE_SIZE + 10, y + j * CUBE_SIZE + 10), (x + i * CUBE_SIZE + 40, y + j * CUBE_SIZE + 40), 3)
                pygame.draw.line(screen, RED, (x + i * CUBE_SIZE + 40, y + j * CUBE_SIZE + 10), (x + i * CUBE_SIZE + 10, y + j * CUBE_SIZE + 40), 3)

        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
