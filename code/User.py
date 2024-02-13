import pygame
from settings import screen_width, screen_height

class User(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../UI/pointers/01.png")
        pygame.mouse.set_pos((screen_width / 2, screen_height / 2))
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = self.pos)
        self.mouse_button_clicked = False
        self.mouse_click_time = 0


    def player_inputs(self):
        keys = pygame.mouse.get_pressed(3)
        if keys[0] and not self.mouse_button_clicked:
            self.mouse_button_clicked = True
            self.mouse_click_time = pygame.time.get_ticks()


        if keys[2] and not self.mouse_button_clicked:
            self.mouse_button_clicked = True
            self.mouse_click_time = pygame.time.get_ticks()

    def mouse_cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.mouse_button_clicked:
            if current_time - self.mouse_click_time >= 500: self.mouse_button_clicked = False


    def adjust_placement(self):
        self.pos = pygame.mouse.get_pos()
        self.rect = self.image.get_rect(center = self.pos)


    def update(self):
        self.player_inputs()
        self.adjust_placement()
        self.mouse_cooldown()
