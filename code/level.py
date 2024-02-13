import pygame
from settings import tile_size
from tile import Static_Tile
from support import read_csv_file, cut_graphics
from game_data import first_map_data

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.obstacle_sprites = pygame.sprite.Group()
        # self.read_data()

    # def read_data(self):
    #     water_csv = read_csv_file(first_map_data["water"])
    #     water = cut_graphics("../map/Tilesets/Terrain/Water/Water.png")
    #     self.water_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(water_csv):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.water_group.add(Static_Tile((x, y), tile_size, water[int(val)]))
    #     sand_csv = read_csv_file(first_map_data["sand"])
    #     sand = cut_graphics("../map/Tilesets/Terrain/Ground/Tilemap_Flat.png")
    #     self.sand_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(sand_csv):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.sand_group.add(Static_Tile((x, y), tile_size, sand[int(val)]))
    #     elevation_csv = read_csv_file(first_map_data["elevation"])
    #     elevation = cut_graphics("../map/Tilesets/Terrain/Ground/Tilemap_Elevation.png")
    #     self.elevation_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(elevation_csv):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.elevation_group.add(Static_Tile((x, y), tile_size, elevation[int(val)]))
    #     grass_csv = read_csv_file(first_map_data["grass"])
    #     grass = cut_graphics("../map/Tilesets/Terrain/Ground/Tilemap_Flat.png")
    #     self.grass_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(grass_csv):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.grass_group.add(Static_Tile((x, y), tile_size, grass[int(val)]))
    #     mountains_1 = read_csv_file(first_map_data["mountains 1"])
    #     self.mountains_1_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_1):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_1_group.add(Static_Tile((x, y), tile_size, elevation[int(val)]))
    #     mountains_floors_1 = read_csv_file(first_map_data["mountains floors 1"])
    #     self.mountains_floors_1_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_floors_1):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_floors_1_group.add(Static_Tile((x, y), tile_size, grass[int(val)]))
    #     mountains_2 = read_csv_file(first_map_data["mountains 2"])
    #     self.mountains_2_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_2):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_2_group.add(Static_Tile((x, y), tile_size, elevation[int(val)]))
    #     mountains_floors_2 = read_csv_file(first_map_data["mountains floors 2"])
    #     self.mountains_floors_2_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_floors_2):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_floors_2_group.add(Static_Tile((x, y), tile_size, grass[int(val)]))
    #     mountains_3 = read_csv_file(first_map_data["mountains 3"])
    #     self.mountains_3_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_3):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_3_group.add(Static_Tile((x, y), tile_size, elevation[int(val)]))
    #     mountains_floors_3 = read_csv_file(first_map_data["mountains floors 3"])
    #     self.mountains_floors_3_group = pygame.sprite.Group()
    #     for row_index, row in enumerate(mountains_floors_3):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size
    #                 self.mountains_3_group.add(Static_Tile((x, y), tile_size, grass[int(val)]))
    #     details_csv = read_csv_file(first_map_data["details"])
    #     for row_index, row in enumerate(details_csv):
    #         for col, val in enumerate(row):
    #             if val != "-1":
    #                 x = col * tile_size
    #                 y = row_index * tile_size




    def draw_map(self):
        pass
        

    def run(self):
        pass


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        pass
