import pygame
from settings import tile_size
from tile import Static_Tile
from support import cut_graphics
from pytmx.util_pygame import load_pygame
from animations import Viking_solider, Soldier_blue, Cannon, Soldier_yellow, Archer_tower, Soldier_purple
from User import User
from random import randint



class Button(pygame.sprite.Sprite):
    def __init__(self, pos, type):
        super().__init__()
        self.pos = list(pos)
        self.type = type
        self.image = pygame.transform.smoothscale(pygame.image.load("../UI/Buttons/Button_Blue_9Slides.png"), (150, 150))
        self.rect = self.image.get_rect(topleft = self.pos)
        self.mouse_button_clicked = False
        self.button_clicked = False
        if type == "soldier_blue":
            self.soldier_blue = pygame.image.load("../characters/soldier blue/idle blue/0.png")
            self._rect = self.soldier_blue.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.soldier_blue, self._rect)
        if type == "soldier_yellow":
            self.soldier_yellow = pygame.image.load("../characters/soldier yellow/idle yellow/0.png")
            self._rect = self.soldier_yellow.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.soldier_yellow, self._rect)
        if type == "soldier_purple":
            self.soldier_purple  = pygame.image.load("../characters/soldier purple/idle purple/0.png")
            self._rect = self.soldier_purple.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.soldier_purple, self._rect)
        if type == "cannon":
            self.cannon = pygame.transform.smoothscale(pygame.image.load("../cannon/move/0.png"), (80, 80))
            self._rect = self.cannon.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.cannon, self._rect)
        if type == "archer_tower":
            self.archer_tower_images = cut_graphics("../characters/7.png", (70, 130))
            self.archer_tower = pygame.transform.scale(self.archer_tower_images[0], (100, 140))
            self._rect = self.archer_tower.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2 - 10))
            self.image.blit(self.archer_tower, self._rect)
        if type == "ship":
            self.ship_alive = cut_graphics("../ship/ship.png", (141, 50))[0]
            self.ship_destroyed = cut_graphics("../ship/ship.png", (141, 50))[1]
            self.ship = pygame.transform.smoothscale(self.ship_alive, (120, 100))
            self._rect = self.ship.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.ship, self._rect)
        if type == "dragon":
            self.dragon = pygame.transform.smoothscale(cut_graphics("../dragon/144x128/flying_twin_headed_dragon-blue.png", (144,128))[0], (130, 128))
            self._rect = self.dragon.get_rect(center=(self.image.get_width() // 2, self.image.get_height() // 2))
            self.image.blit(self.dragon, self._rect)


class Level:
    def __init__(self):
        # main setup
        pygame.mixer.init()
        self.viking_appeared = False
        self.night_surf = pygame.image.load("../map/Golden Dawn Map night.png")
        self.training_music = pygame.mixer.Sound("../music/Day/something_approaches.wav")
        self.night_surf_rect = self.night_surf.get_rect(topleft=(0,0))
        self.day = True
        self.day_time = pygame.time.get_ticks()
        self.night = False
        self.night_time = 0
        self.display = pygame.display.get_surface()
        self.internal_surf = pygame.Surface((self.display.get_width(), self.display.get_height()))
        self.internal_surf_rect = self.internal_surf.get_rect(center=(self.display.get_width() // 2, self.display.get_height() // 2))
        self.coin_image = pygame.image.load("../map/Tilesets/Resources/G_Idle.png")
        self.coin_rect = self.coin_image.get_rect(topright=(self.internal_surf.get_width() - 120,self.internal_surf.get_height() - self.internal_surf.get_height() + 30))
        self.sprite_x = 0
        self.sprite_y = 0
        self.start_time = pygame.time.get_ticks()
        self.game_story_image = pygame.transform.smoothscale(pygame.image.load("../Backgrounds/game_story_bg.png"), (self.display.get_width(), self.display.get_height()))
        self.game_story_finished = False
        self.font = pygame.font.Font("../fonts/Seagram tfb.ttf", 20)
        self.game_story = ["In 891 AD, Ethan, The King of Eldoria, a Castle in the Faroe Islands, was proclaimed dead, so his son, Ethar, sat on the throne and became the king of the castle.",
                           "The Vikings thought the New King didn't have enough experience to maintain safety inside the castle, so they decided to invade it.",
                           "Fortunately, Ethar started preparing the defense. When the Vikings came, they organized their army, preparing to attack at night.",
                           "Fortunately, the Ethar knew that there was a potential attack. The Night is getting soon, prepare your army.",
                           "The Vikings started invading the castle. If the castle falls, the Vikings will start invading the whole island without any resistance.",
                           "Each Night, the Vikings attack with a larger army. You must prepare your defensive army to save the castle before the Night.",
                           "We learn a new skill or weapons to fight the Vikings daily. In the beginning, we will learn how to build an archer tower and barracks to train new soldiers",
                           ", but then we will learn how to build rocket launchers and how to train a dragon.",
                           "When the Dawn comes out, the Vikings run away from the battlefield. We will continue fighting the Vikings until their army ends and the Golden Dawn comes."]

        # groups
        self.soldier_group = pygame.sprite.Group()
        self.viking_group = pygame.sprite.Group()

        # UI setup
        self.user = pygame.sprite.GroupSingle(User())
        self.map_data = load_pygame("../map/Golden Dawn Map.tmx")
        self.soldier_blue_button_pos = ((self.display.get_width() - (self.display.get_width() - 180)), self.display.get_height() - 140)
        self.soldier_yellow_button_pos = (self.display.get_width() - (self.display.get_width() - 365), self.display.get_height() - 140)
        self.soldier_purple_button_pos = ((self.display.get_width() - (self.display.get_width() - 550)), self.display.get_height() - 140)
        self.cannon_button_pos = (self.display.get_width() - (self.display.get_width() - 735), self.display.get_height() - 140)
        self.archer_tower_button_pos = (self.display.get_width() - (self.display.get_width() - 920), self.display.get_height() - 140)
        self.ship_button_pos = (self.display.get_width() - (self.display.get_width() - 1105), self.display.get_height() - 140)
        self.dragon_button_pos = (self.display.get_width() - (self.display.get_width() - 1290), self.display.get_height() - 140)
        self.soldier_blue_button = Button(self.soldier_blue_button_pos, "soldier_blue")
        self.soldier_yellow_button = Button(self.soldier_yellow_button_pos, "soldier_yellow")
        self.soldier_purple_button = Button(self.soldier_purple_button_pos, "soldier_purple")
        self.archer_tower_button = Button(self.archer_tower_button_pos, "archer_tower")
        self.cannon_button = Button(self.cannon_button_pos, "cannon")
        self.ship_button = Button(self.ship_button_pos, "ship")
        self.dragon_button = Button(self.dragon_button_pos, "dragon")
        self.button_group = pygame.sprite.Group()
        self.button_group.add(self.soldier_blue_button)
        self.button_group.add(self.soldier_yellow_button)
        self.button_group.add(self.soldier_purple_button)
        self.button_group.add(self.archer_tower_button)
        self.button_group.add(self.cannon_button)
        self.button_group.add(self.ship_button)
        self.button_group.add(self.dragon_button)
        self.visible_sprites = pygame.sprite.Group()

        # Scrolling setup
        self.max_scroll_val_rt = -1300
        self.max_scroll_val_lt = 3000
        self.read_map_data()
        self.viking_group.add(Viking_solider((self.internal_surf.get_width(), self.castle_height)))


    def read_map_data(self):
        for layer in self.map_data.visible_layers:
            if hasattr(layer, "data"):
                for x,y,surf in layer.tiles():
                    pos = (x * tile_size, y * tile_size)
                    self.visible_sprites.add(Static_Tile(pos, tile_size, surf))
        for obj in self.map_data.objects:
            # 560, 445
            self.castle_height = obj.y
            pos = (obj.x, obj.y)
            self.visible_sprites.add(Static_Tile(pos, (560,445), obj.image))

    def scrolling_keyboard(self):
        keys = pygame.key.get_pressed()
        scroll_val = 17
        if self.day:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                for sprite in self.visible_sprites:
                    self.sprite_x, self.sprite_y = sprite.rect.topleft
                    if self.sprite_x < self.max_scroll_val_lt:
                        sprite.rect.x = self.sprite_x + scroll_val
                    else:
                        break
                for soldier in self.soldier_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x + scroll_val
                    else:
                        break
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x + scroll_val
                    else:
                        break
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                for sprite in self.visible_sprites:
                    self.sprite_x, self.sprite_y = sprite.rect.topleft
                    if self.sprite_x > self.max_scroll_val_rt:
                        sprite.rect.x = self.sprite_x - scroll_val
                    else:
                        break
                for soldier in self.soldier_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x - scroll_val
                    else:
                        break
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x - scroll_val
                    else:
                        break
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                for sprite in self.visible_sprites:
                    self.sprite_x, self.sprite_y = sprite.rect.topleft
                    sprite.rect.y = self.sprite_y + scroll_val

                for soldier in self.soldier_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y + scroll_val
                    else:
                        break
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y + scroll_val
                    else:
                        break
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                for sprite in self.visible_sprites:
                    self.sprite_x, self.sprite_y = sprite.rect.topleft
                    sprite.rect.y = self.sprite_y - scroll_val
                for soldier in self.soldier_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y - scroll_val
                    else:
                        break
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y - scroll_val
                    else:
                        break
        if self.night:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.night_surf_rect.x -= scroll_val
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x - scroll_val
                    else:
                        break
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.night_surf_rect.x += scroll_val
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_width():
                        soldier.rect.x = self.sprite_x + scroll_val
                    else:
                        break
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.night_surf_rect.y -= scroll_val
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y - scroll_val
                    else:
                        break
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.night_surf_rect.y += scroll_val
                for soldier in self.viking_group:
                    self.sprite_x, self.sprite_y = soldier.rect.topleft
                    if self.sprite_x < self.display.get_height():
                        soldier.rect.y = self.sprite_y + scroll_val
                    else:
                        break
    def day_night_cooldowns(self):
        current_time = pygame.time.get_ticks()
        if self.day:
            if current_time - self.day_time >= 60000:
                self.night = True
                self.day = False
                self.day_time = 0
                self.night_time = pygame.time.get_ticks()
        if self.night:
            if current_time - self.night_time >= randint(1380000,1800000):
                self.night = False
                self.day = True
                self.day_time = pygame.time.get_ticks()
                self.night_time = 0

    def run(self):
        self.day_night_cooldowns()
        if not self.game_story_finished:
            current_time = pygame.time.get_ticks()
            if current_time - self.start_time <= 5000:
                self.internal_surf.blit(self.game_story_image, (0,0))
                y_position = 300
                for line in self.game_story:
                    render_text = self.font.render(line, True, "white")
                    self.internal_surf.blit(render_text, (20, y_position))
                    y_position += render_text.get_height() + 5

            if current_time - self.start_time > 5000:
                self.game_story_finished = True
            self.display.blit(self.internal_surf, self.internal_surf_rect)
        else:
            if self.day:
                self.scrolling_keyboard()       
                self.visible_sprites.draw(self.internal_surf)
            if self.night:
                self.viking_group.update()
                self.viking_group.draw(self.internal_surf)
                self.scrolling_keyboard()
                self.internal_surf.blit(self.night_surf, self.night_surf_rect)
                self.viking_group.draw(self.internal_surf)
            self.training_music.play(loops=-1)
            self.soldier_group.update()
            self.soldier_group.draw(self.internal_surf)
            self.user.update()
            self.button_group.update()
            self.button_group.draw(self.internal_surf)
            self.internal_surf.blit(self.coin_image,self.coin_rect)
            self.user.draw(self.internal_surf)
            self.display.blit(self.internal_surf, self.internal_surf_rect)
            