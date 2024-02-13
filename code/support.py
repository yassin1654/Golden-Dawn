import time, pygame.display, pygame.font
from settings import tile_size
from sys import setrecursionlimit
from csv import reader

setrecursionlimit(80000)
sub_str = ""
def write(text: str,font: pygame.font.Font, letter_index: int = 0):
    global sub_str
    screen = pygame.display.get_surface()
    if letter_index < len(text):
        sub_str += text[letter_index]
        text_surf = font.render(sub_str, False, "black")
        screen.blit(text_surf, (20, 20))
        pygame.display.update()
        time.sleep(0.07)
        write(text,font, letter_index + 1)
    else:
        print("\nEnd of the story.")
        sub_str = ""


def read_csv_file(path):
    blueprint = []
    with open(path) as map:
        layout = reader(map, delimiter=",")
        for row in layout:
            blueprint.append(list(row))
    return blueprint


def cut_graphics(path,tile_size = tile_size):
    image = pygame.image.load(path)
    cut_num_x = int(image.get_width() / tile_size)
    cut_num_y = int(image.get_height() / tile_size)

    tiles = []
    for row in range(cut_num_y):
        for col in range(cut_num_x):
            x = col * tile_size
            y = row * tile_size
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(image, (0,0), pygame.Rect(x,y,tile_size, tile_size))
            tiles.append(new_surf)
    return tiles
