import pygame
from sys import exit
from settings import *
from level import Level


class Main:
    def __init__(self):
        # game setup
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Golden Dawn")
        game_logo = pygame.image.load("../logos and graphics/golden dawn.png")
        pygame.display.set_icon(game_logo)
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(0)
        self.level = Level()
    def run(self):
        # game loop
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.screen.fill("white")
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)
main = Main()
main.run()