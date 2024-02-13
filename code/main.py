import pygame
from sys import exit
from settings import *
from User import User
from level import Level
from characters import Solider


# game setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Golden Dawn")
game_logo = pygame.image.load("../logos and graphics/golden dawn.png")
pygame.display.set_icon(game_logo)
clock = pygame.time.Clock()
user = User()
user_group = pygame.sprite.GroupSingle(user)
pygame.mouse.set_visible(0)
font = pygame.font.Font("../PixelifySans-Regular.ttf", 30)
level = Level()
solider_group = pygame.sprite.Group()
solider_group.add(Solider((40, 60)))
# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("white")
    level.run()
    user.update()
    solider_group.update()
    user_group.draw(screen)
    solider_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
