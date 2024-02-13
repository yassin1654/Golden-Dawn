import pygame
from support import cut_graphics
class Solider(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = cut_graphics("../characters/03Knight.png", 48)
        self.current_animation = 0
        self.image = self.animations[self.current_animation]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.current_animation += 0.2
        if self.current_animation >= len(self.animations) - 1: self.current_animation = 0
        self.image = self.animations[int(self.current_animation)]
    def update(self):
        self.animate()