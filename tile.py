import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        if isinstance(size, int):
            self.size = (size,size)
        if isinstance(size, tuple):
            self.size = size
        self.pos = pos
        self.image = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft = pos)
    def get_pos(self):
        return self.pos
class Static_Tile(Tile):
    def __init__(self, pos, size, surface):
        super().__init__(pos, size)
        self.surface = surface.convert_alpha()
        self.image.blit(self.surface, (0, 0))