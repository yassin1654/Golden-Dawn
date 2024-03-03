import pygame
from sys import exit
pygame.init()

# Game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Health Bar')

font = pygame.font.Font("../FONTS/Seagram tfb.ttf", 50)
text_surface = font.render("0", True, (0, 0, 0))

bar = pygame.image.load("../UI/Buttons/Button_Hover_3Slides.png")
bar = pygame.transform.smoothscale(bar, (400, 100))

coins = pygame.image.load("../UI/G_Idle.png")

class HealthBar:
  def __init__(self, x, y, w, h, max_hp):
    self.x = x
    self.y = y
    self.w = w
    self.h = h
    self.hp = max_hp
    self.max_hp = max_hp

  def draw(self, surface):
    # Calculate health ratio
    ratio = self.hp / self.max_hp
    screen.blit(bar, (205,180))
    screen.blit(coins, (205,145))


health_bar = HealthBar(250, 200, 300, 40, 100)

while True:
  screen.fill("indigo")


  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()

  health_bar.hp = 50
  health_bar.draw(screen)
  screen.blit(text_surface, (400, 185))
  pygame.display.update()