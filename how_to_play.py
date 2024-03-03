import pygame
from sys import exit



class How:
    def __init__(self):
        pygame.init()

        # Define colors
        white = (255, 255, 255)

        # Add music
        pygame.mixer.music.load("../music/main menu/Oriental.wav")
        pygame.mixer.music.play(-1)

        # Make screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("GOLDEN DAWN")

        # Add background
        self.bg = pygame.image.load('../Backgrounds/background.png')
        self.bg = pygame.transform.smoothscale(self.bg, (self.screen.get_width(), self.screen.get_height()))

        # Make font
        self.font = pygame.font.Font('../fonts/Seagram tfb.ttf', 40)

        # Define the lines of text
        self.text_lines = [
            "Weapons: You have all the weapons on the down side of the screen.",
            "You can drag them with your mouse to anywhere on the map.",
            "During the game you will learn how to train a dragon and many other things."
        ]

        # Render each line of text individually
        self.text_surfaces = [self.font.render(line, True, white) for line in self.text_lines]

        # Calculate the total height of all lines
        self.total_height = sum(surface.get_height() for surface in self.text_surfaces)

        # Calculate the starting y-coordinate for the first line
        self.y = (self.screen.get_height() - self.total_height) // 2
    def run(self):
        # Blit background
        self.screen.blit(self.bg, (0, 0))

        # Blit each line onto the screen
        for text_surface in self.text_surfaces:
            self.screen.blit(text_surface, ((self.screen.get_width() - text_surface.get_width()) // 2, self.y))
            self.y += text_surface.get_height()  # Update y-coordinate for the next line

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.clock.tick(60)
            pygame.display.update()

how = How()
how.run()