import pygame
from csv import reader


def read_csv_file(path):
    blueprint = []
    with open(path) as map:
        layout = reader(map, delimiter=",")
        for row in layout:
            blueprint.append(list(row))
    return blueprint


def cut_graphics(path,tile_size):
    image = pygame.image.load(path).convert_alpha()
    cut_num_x = int(image.get_width() / tile_size[0])
    cut_num_y = int(image.get_height() / tile_size[1])

    tiles = []
    for row in range(cut_num_y):
        for col in range(cut_num_x):
            x = col * tile_size[0]
            y = row * tile_size[1]
            new_surf = pygame.Surface((tile_size[0], tile_size[1]), pygame.SRCALPHA)
            new_surf.blit(image, (0,0), pygame.Rect(x,y,tile_size[0], tile_size[1]))
            tiles.append(new_surf)
    return tiles
