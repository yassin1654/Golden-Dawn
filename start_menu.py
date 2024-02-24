import pygame
import sys

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (196, 164, 132)

# Define frame rate, width, and height
screen_width = 500
screen_height = 600
fps = 60

# Set up the display
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Golden Dawn")
clock = pygame.time.Clock()

# Add audio
pygame.mixer.music.load('audios/Oriental.wav')
pygame.mixer.music.play(-1)
def draw_cursor():
    custom_cursor = pygame.image.load('pointers/01.png')
    pygame.mouse.set_visible(False)
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(custom_cursor, mouse_pos)


def draw_button(surface, image_path, x, y, width, height, text, font_size=25, text_color=BLACK):
    button_image = pygame.image.load(image_path)
    button_image = pygame.transform.scale(button_image, (width, height))
    surface.blit(button_image, (x, y))

    font = pygame.font.Font("fonts/PixelifySans-Regular.ttf", font_size)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2.5))
    surface.blit(text_surface, text_rect)

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font("fonts/Seagram tfb.ttf", size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def main_menu():
    while True:
        # Add background
        background = pygame.image.load('photos/photo_4.png')
        background = pygame.transform.smoothscale(background, [screen_width, screen_height])
        screen.blit(background, (0,0))

        # Add banners
        name_banner = pygame.image.load('banners/banner (horizontal).png')
        name_banner = pygame.transform.smoothscale(name_banner, (500, 200))
        screen.blit(name_banner, (10, 50))

        draw_text(screen, "Golden Dawn", 45, screen.get_width() // 1.92, screen.get_height() // 4)

        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3, screen.get_height() // 2, 200,
                    50, "START")
        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3, screen.get_height() // 2 + 70,
                    200, 50, "OPTIONS")
        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3,
                    screen.get_height() // 2 + 140, 200, 50, "EXIT")
        draw_cursor()

        clock.tick(fps)
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
                    elif screen.get_height() // 2 + 70 <= mouse_pos[1] <= screen.get_height() // 2 + 120:
                        options_menu()
                    elif screen.get_height() // 2 + 140 <= mouse_pos[1] <= screen.get_height() // 2 + 190:
                        pygame.quit()
                        sys.exit()


def start_menu():
    while True:
        screen.fill(LIGHT_BROWN)
        draw_text(screen, "You're in the Start Menu", 40, screen.get_width() // 2, screen.get_height() // 4)

        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3, screen.get_height() // 2 + 70,
                    200, 50, "Back")
        draw_cursor()

        clock.tick(fps)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if screen.get_width() // 3 <= mouse_pos[0] <= screen.get_width() // 3 + 200:
                    if screen.get_height() // 2 + 70 <= mouse_pos[1] <= screen.get_height() // 2 + 120:
                        main_menu()


def options_menu():
    while True:
        screen.fill(LIGHT_BROWN)
        draw_text(screen, "Options Menu", 40, screen.get_width() // 2, screen.get_height() // 4)

        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3, screen.get_height() // 2, 200,
                    50, "HOW TO PLAY")
        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3, screen.get_height() // 2 + 70,
                    200, 50, "NEW GAME")
        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3,
                    screen.get_height() // 2 + 140, 200, 50, "SETTINGS")
        draw_button(screen, 'buttons/Button_Hover_3Slides.png', screen.get_width() // 3,
                    screen.get_height() // 2 + 210, 200, 50, "BACK")
        draw_cursor()

        clock.tick(fps)
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
                    elif screen.get_height() // 2 + 70 <= mouse_pos[1] <= screen.get_height() // 2 + 120:
                        # Action for "New Game"
                        pass
                    elif screen.get_height() // 2 + 140 <= mouse_pos[1] <= screen.get_height() // 2 + 190:
                        # Action for "Settings"
                        pass
                    elif screen.get_height() // 2 + 210 <= mouse_pos[1] <= screen.get_height() // 2 + 260:
                        main_menu()


main_menu()