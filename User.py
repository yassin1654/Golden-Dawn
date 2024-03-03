import pygame
from settings import screen_width, screen_height


class User(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.selection_box = pygame.image.load("../UI/Pointers/02.png")
        self.pointer = pygame.image.load("../UI/pointers/01.png")
        self.image = self.pointer
        pygame.mouse.set_pos((screen_width / 2, screen_height / 2))
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = self.pos)
        self.mouse_button_clicked = False
        self.mouse_click_time = 0
        self.coins = 0

    def mouse_cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.mouse_button_clicked:
            if current_time - self.mouse_click_time >= 500: self.mouse_button_clicked = False

    def adjust_placement(self):
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = self.pos)


    def update(self):
        self.adjust_placement()
        self.mouse_cooldown()