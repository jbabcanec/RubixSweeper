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
size = 6 
mines = 4
rubix = Rubix(size=size, mines=mines)

# Main game loop
running = True
while running:
    screen.fill(BLACK)  # Clear the screen

    front_face_minesweeper = rubix.faces['front']
    game_over = front_face_minesweeper.game_over 
    game_win = front_face_minesweeper.check_win()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Mouse click events
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            grid_x, grid_y = (mouse_x - 100) // CUBE_SIZE, (mouse_y - 100) // CUBE_SIZE

            # Check if the click is inside the grid
            if 0 <= grid_x < size and 0 <= grid_y < size:
                if event.button == 1:  # Left click to reveal
                    rubix.reveal_cell('front', grid_x, grid_y)
                elif event.button == 3:  # Right click to flag
                    rubix.flag_cell('front', grid_x, grid_y)
                    print(f"After flag_cell call, flagged status: {rubix.get_flagged('front')}")

    # Dynamic Grid Drawing
    x, y = 100, 100
    front_face = rubix.get_face('front')
    front_revealed = rubix.get_revealed('front')
    front_flagged = rubix.get_flagged('front')

    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, WHITE, (x + i * CUBE_SIZE, y + j * CUBE_SIZE, CUBE_SIZE, CUBE_SIZE), 1)
            
            # If cell is revealed, fill it with a light gray color
            if front_revealed[i][j]:
                pygame.draw.rect(screen, (200, 200, 200), (x + i * CUBE_SIZE + 1, y + j * CUBE_SIZE + 1, CUBE_SIZE - 1, CUBE_SIZE - 1))
                
                # Draw the number or mine
                font = pygame.font.SysFont(None, 36)
                text_surface = font.render(str(front_face[i][j]), True, GREEN)
                screen.blit(text_surface, (x + i * CUBE_SIZE + 15, y + j * CUBE_SIZE + 15))

            # If cell is flagged, draw a red X
            elif front_flagged[i][j]:
                pygame.draw.line(screen, RED, (x + i * CUBE_SIZE + 10, y + j * CUBE_SIZE + 10), (x + i * CUBE_SIZE + 40, y + j * CUBE_SIZE + 40), 3)
                pygame.draw.line(screen, RED, (x + i * CUBE_SIZE + 40, y + j * CUBE_SIZE + 10), (x + i * CUBE_SIZE + 10, y + j * CUBE_SIZE + 40), 3)

    if game_over:
        font = pygame.font.SysFont(None, 48)
        lose_surface = font.render("You Lose", True, RED)
        screen.blit(lose_surface, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25))

        pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 130, 50))
        reset_surface = font.render("Reset", True, BLACK)
        screen.blit(reset_surface, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 60))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (SCREEN_WIDTH // 2 - 50 <= mouse_x <= SCREEN_WIDTH // 2 + 50) and (SCREEN_HEIGHT // 2 + 50 <= mouse_y <= SCREEN_HEIGHT // 2 + 100):
            if event.type == pygame.MOUSEBUTTONDOWN:
                rubix = Rubix(size=size, mines=mines)

    elif game_win:  # New block for game win
        font = pygame.font.SysFont(None, 48)
        win_surface = font.render("You Win", True, GREEN)
        screen.blit(win_surface, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 25))

        pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 50, 130, 50))
        reset_surface = font.render("Reset", True, BLACK)
        screen.blit(reset_surface, (SCREEN_WIDTH // 2 - 30, SCREEN_HEIGHT // 2 + 60))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (SCREEN_WIDTH // 2 - 50 <= mouse_x <= SCREEN_WIDTH // 2 + 50) and (SCREEN_HEIGHT // 2 + 50 <= mouse_y <= SCREEN_HEIGHT // 2 + 100):
            if event.type == pygame.MOUSEBUTTONDOWN:
                rubix = Rubix(size=size, mines=mines)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

