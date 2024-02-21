import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
LIGHT_BLUE = (173, 216, 230)
BLACK = (0, 0, 0)
LIGHT_BROWN = (196, 164, 132)

# Set up the display
screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption("Golden Dawn")

# Set the font
font = pygame.font.Font("fonts/rainyhearts.ttf", 30)
def draw_cursor():
    custom_cursor = pygame.image.load('pointers/01.png')
    pygame.mouse.set_visible(False)
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(custom_cursor, mouse_pos)
# Function to create buttons
def draw_button(surface, color, x, y, width, height, text):
    pygame.draw.rect(surface, color, (x, y, width, height))
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    surface.blit(text_surface, text_rect)

# Function to display text
def draw_text(surface, text, size, x, y):
    font = pygame.font.Font("fonts/Seagram tfb.ttf", size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

# Main menu screen
def main_menu():
    while True:
        screen.fill(LIGHT_BROWN)

        draw_text(screen, "Golden Dawn", 50, screen.get_width() // 2, screen.get_height() // 4)
        
        # Draw buttons
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2, 200, 50, "START")
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2 + 70, 200, 50, "OPTIONS")
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2 + 140, 200, 50, "EXIT")
        draw_cursor()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if screen.get_width() // 3 <= mouse_pos[0] <= screen.get_width() // 3 + 200:
                    if screen.get_height() // 2 <= mouse_pos[1] <= screen.get_height() // 2 + 50:
                        start_menu()
                    elif screen.get_height() // 2 + 70 <= mouse_pos[1] <= screen.get_height() // 2 + 70 + 50:
                        options_menu()
                    elif screen.get_height() // 2 + 140 <= mouse_pos[1] <= screen.get_height() // 2 + 140 + 50:
                        pygame.quit()
                        sys.exit()

# Start menu screen
def start_menu():
    while True:
        screen.fill(LIGHT_BLUE)
        draw_text(screen, "You're in the Start Menu", 40, screen.get_width() // 2, screen.get_height() // 4)

        # Draw back button
        draw_button(screen, WHITE, screen.get_width() // 2 - 100, screen.get_height() // 2, 200, 50, "Back")
        draw_cursor()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if screen.get_width() // 2 - 100 <= mouse_pos[0] <= screen.get_width() // 2 - 100 + 200:
                    if screen.get_height() // 2 <= mouse_pos[1] <= screen.get_height() // 2 + 50:
                        main_menu()

# Options menu screen
def options_menu():
    while True:
        screen.fill(LIGHT_BLUE)
        draw_text(screen, "Options Menu", 40, screen.get_width() // 2, screen.get_height() // 4)
        
        # Draw buttons
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2, 200, 50, "How to Play")
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2 + 70, 200, 50, "New Game")
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2 + 140, 200, 50, "Settings")
        draw_button(screen, WHITE, screen.get_width() // 3, screen.get_height() // 2 + 210, 200, 50, "Back")
        draw_cursor()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if screen.get_width() // 3 <= mouse_pos[0] <= screen.get_width() // 3 + 200:
                    if screen.get_height() // 2 <= mouse_pos[1] <= screen.get_height() // 2 + 50:
                        # Action for "How to Play"
                        pass
                    elif screen.get_height() // 2 + 70 <= mouse_pos[1] <= screen.get_height() // 2 + 70 + 50:
                        # Action for "New Game"
                        pass
                    elif screen.get_height() // 2 + 140 <= mouse_pos[1] <= screen.get_height() // 2 + 140 + 50:
                        # Action for "Settings"
                        pass
                    elif screen.get_height() // 2 + 210 <= mouse_pos[1] <= screen.get_height() // 2 + 210 + 50:
                        main_menu()

# Run the main menu loop
main_menu()