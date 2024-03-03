import random
import pygame


class Viking_solider(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pos
        self.attacking_animations = [[pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/0.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/1.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/2.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/3.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/4.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/5.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/6.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/7.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/8.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Attack1H/9.png").convert_alpha(), (150, 150))],

                           [pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/0.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/1.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/2.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/3.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/4.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/5.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/6.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/7.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/8.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Attack2H/9.png").convert_alpha(), (150, 150))],

                           [pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/0.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/1.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/2.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/3.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/4.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/5.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/6.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/7.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/8.png").convert_alpha(), (150, 150)),
                           pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Attack1H/9.png").convert_alpha(), (150, 150))]]
        self.walking_animations = [
            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Walk/9.png").convert_alpha(), (150, 150))
             ],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/0.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/1.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/2.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/3.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/4.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/5.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/6.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/7.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/8.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Walk/9.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/0.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/1.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/2.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/3.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/4.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/5.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/6.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/7.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/8.png").convert_alpha(), (150, 150)),
            pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Walk/9.png").convert_alpha(), (150, 150))]
        ]
        self.idle_animation = [
            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Stand/9.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Stand/9.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Stand/9.png").convert_alpha(), (150, 150))]
        ]
        self.run_animation = [[pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking1/Run/9.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking2/Run/9.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/5.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/6.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/7.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/8.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/Viking3/Run/9.png").convert_alpha(), (150, 150))]]
        
        self.current_attack_animation = 0
        self.attack_times = 0
        self.current_walk_animation = 0
        self.current_idle_animation = 0
        self.current_run_animation = 0
        self.current_character = random.randint(0, 2)
        self.image = pygame.transform.flip(self.attacking_animations[self.current_character][self.current_attack_animation], True, False)
        self.rect = self.image.get_rect(center=pos)

    def reset(self, current_animation: str = False):
        if current_animation == "attack":
            self.current_walk_animation = 0
            self.current_idle_animation = 0
            self.current_run_animation = 0
        elif current_animation == "walk":
            self.current_attack_animation = 0
            self.current_idle_animation = 0
            self.current_run_animation = 0
        elif current_animation == "idle":
            self.current_attack_animation = 0
            self.current_walk_animation = 0
            self.current_run_animation = 0
        elif current_animation == "run":
            self.current_walk_animation = 0
            self.current_attack_animation = 0
            self.current_idle_animation = 0
        if not current_animation:
            self.current_walk_animation = 0
            self.current_attack_animation = 0
            self.current_idle_animation = 0
            self.current_run_animation = 0

    def animate_idle(self):
        if self.rect.x >= 1000:
            self.reset("idle")
            self.current_idle_animation += 0.2
            if self.current_idle_animation >= len(self.idle_animation[self.current_character]): self.current_idle_animation = 0
            self.image = pygame.transform.flip(self.idle_animation[self.current_character][int(self.current_idle_animation)], True, False)

    def animate_walk(self):
        if self.rect.x < 700:
            self.reset("walk")
            self.current_walk_animation += 0.2
            if self.current_walk_animation >= len(self.walking_animations[self.current_character]) : self.current_walk_animation = 0
            self.image = pygame.transform.flip(self.walking_animations[self.current_character][int(self.current_walk_animation)], True, False)
            self.rect.x += 1

    def animate_attack(self):
        if self.rect.x >= 700 and self.attack_times < 6:
            self.reset("attack")
            self.current_attack_animation += 0.2
            if self.current_attack_animation >= len(self.attacking_animations[self.current_character]):
                self.current_attack_animation = 0
                self.attack_times += 1
            self.image = pygame.transform.flip(self.attacking_animations[self.current_character][int(self.current_attack_animation)], True,False)
    def animate_run(self):
        self.reset("run")
        self.current_run_animation += 0.3
        if self.current_run_animation >= len(self.run_animation[self.current_character]):
            self.current_run_animation = 0
        self.image = pygame.transform.flip(self.run_animation[self.current_character][int(self.current_run_animation)], True, False)
        self.rect.x -= 2

    def update(self):
        self.animate_run()

class Soldier_blue(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.attacking_animations = [
            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 1 blue/5.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/attacking 2 blue/5.png").convert_alpha(), (150, 150))
             ]
        ]
        self.idle_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/0.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/1.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/2.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/3.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/4.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/5.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/idle blue/6.png").convert_alpha(), (150, 150)),]
        self.running_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/0.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/1.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/2.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/3.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/4.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier blue/running blue/5.png").convert_alpha(), (150, 150))
                                   ]
        self.current_attack = random.randint(0, 1)
        self.current_attack_animation = 0
        self.finish_attack_counter = 0
        self.current_idle_animation = 0
        self.current_running_animation = 0
        self.current_time = pygame.time.get_ticks()
        self.image = self.attacking_animations[self.current_attack][self.current_attack_animation]
        self.rect = self.image.get_rect(center=pos)

    def animate_attack(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time <= 10000:
            self.current_attack_animation += 0.2
            if self.current_attack_animation >= len(self.attacking_animations[self.current_attack]):
                self.current_attack_animation = 0
                self.current_attack = random.randint(0, 1)
            self.image = self.attacking_animations[self.current_attack][int(self.current_attack_animation)]

    def animate_idle(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 10000:
            self.current_idle_animation += 0.2
            if self.current_idle_animation >= len(self.idle_animations): self.current_idle_animation = 0
            self.image = self.idle_animations[int(self.current_idle_animation)]
    def animate_run(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 15000:
            self.current_running_animation += 0.2
            if self.current_running_animation >= len(self.running_animations): self.current_running_animation = 0
            self.image = self.running_animations[int(self.current_running_animation)]
            self.rect.x += 1

    def update(self):
        self.animate_attack()
        self.animate_idle()
        self.animate_run()

class Soldier_yellow(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.attacking_animations = [
            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 1 yellow/5.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/attacking 2 yellow/5.png").convert_alpha(), (150, 150))
             ]
        ]
        self.idle_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/0.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/1.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/2.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/3.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/4.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/5.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/idle yellow/6.png").convert_alpha(), (150, 150)),]
        self.running_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/0.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/1.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/2.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/3.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/4.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier yellow/running yellow/5.png").convert_alpha(), (150, 150))
                                   ]
        self.current_attack = random.randint(0, 1)
        self.current_attack_animation = 0
        self.finish_attack_counter = 0
        self.current_idle_animation = 0
        self.current_running_animation = 0
        self.current_time = pygame.time.get_ticks()
        self.image = self.attacking_animations[self.current_attack][self.current_attack_animation]
        self.rect = self.image.get_rect(center=pos)

    def animate_attack(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time <= 10000:
            self.current_attack_animation += 0.2
            if self.current_attack_animation >= len(self.attacking_animations[self.current_attack]):
                self.current_attack_animation = 0
                self.current_attack = random.randint(0, 1)
            self.image = self.attacking_animations[self.current_attack][int(self.current_attack_animation)]

    def animate_idle(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 10000:
            self.current_idle_animation += 0.2
            if self.current_idle_animation >= len(self.idle_animations): self.current_idle_animation = 0
            self.image = self.idle_animations[int(self.current_idle_animation)]
    def animate_run(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 15000:
            self.current_running_animation += 0.2
            if self.current_running_animation >= len(self.running_animations): self.current_running_animation = 0
            self.image = self.running_animations[int(self.current_running_animation)]
            self.rect.x += 1

    def update(self):
        self.animate_attack()
        self.animate_idle()
        self.animate_run()

class Soldier_purple(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.attacking_animations = [
            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 1 purple/5.png").convert_alpha(), (150, 150))],

            [pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/0.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/1.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/2.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/3.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/4.png").convert_alpha(), (150, 150)),
             pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/attacking 2 purple/5.png").convert_alpha(), (150, 150))
             ]
        ]
        self.idle_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/0.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/1.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/2.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/3.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/4.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/5.png").convert_alpha(), (150, 150)),
                                pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/idle purple/6.png").convert_alpha(), (150, 150)),]
        self.running_animations = [pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/0.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/1.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/2.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/3.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/4.png").convert_alpha(), (150, 150)),
                                   pygame.transform.smoothscale(pygame.image.load("../characters/soldier purple/running purple/5.png").convert_alpha(), (150, 150))
                                   ]
        self.current_attack = random.randint(0, 1)
        self.current_attack_animation = 0
        self.finish_attack_counter = 0
        self.current_idle_animation = 0
        self.current_running_animation = 0
        self.current_time = pygame.time.get_ticks()
        self.image = self.attacking_animations[self.current_attack][self.current_attack_animation]
        self.rect = self.image.get_rect(center=pos)

    def animate_attack(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time <= 10000:
            self.current_attack_animation += 0.2
            if self.current_attack_animation >= len(self.attacking_animations[self.current_attack]):
                self.current_attack_animation = 0
                self.current_attack = random.randint(0, 1)
            self.image = self.attacking_animations[self.current_attack][int(self.current_attack_animation)]

    def animate_idle(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 10000:
            self.current_idle_animation += 0.2
            if self.current_idle_animation >= len(self.idle_animations): self.current_idle_animation = 0
            self.image = self.idle_animations[int(self.current_idle_animation)]
    def animate_run(self):
        self.new_time = pygame.time.get_ticks()
        if self.new_time - self.current_time >= 15000:
            self.current_running_animation += 0.2
            if self.current_running_animation >= len(self.running_animations): self.current_running_animation = 0
            self.image = self.running_animations[int(self.current_running_animation)]
            self.rect.x += 1

    def update(self):
        self.animate_attack()
        self.animate_idle()
        self.animate_run()

class Cannon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.turn_animations = [
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/0.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/1.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/2.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/3.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/4.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/turn/5.png"), (200, 200))
        ]

        self.shoot_animations = [
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/0.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/1.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/2.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/3.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/4.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/5.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/6.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot/7.png"), (200, 200))
        ]

        self.move_animations = [
            pygame.transform.smoothscale(pygame.image.load("../cannon/move/0.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/move/1.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/move/2.png"), (200, 200))
        ]

        self.shoot_ball = [
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot_ball/0.png"), (200, 200)),
            pygame.transform.smoothscale(pygame.image.load("../cannon/shoot_ball/1.png"), (200, 200))
        ]
        self.direction = "Right"
        self.image = self.move_animations[0]
        self.rect = self.image.get_rect(center = pos)

        self.current_turn_animation = 0
        self.current_shoot_animation = 0
        self.current_move_animation = 0
        self.current_shoot_ball_animation = 0

    def animate_turn(self):
        self.current_turn_animation += 0.02
        if self.current_turn_animation >= len(self.turn_animations):
            self.current_turn_animation = 0
            if self.direction == "Right":
                self.direction = "left"
            elif self.direction == "left":
                self.direction = "Right"
        self.image = self.turn_animations[int(self.current_turn_animation)]

    def animate_shoot(self):
        self.current_shoot_animation += 0.2
        if self.current_shoot_animation >= len(self.shoot_animations):
            self.current_shoot_animation = 0
        self.image = self.shoot_animations[int(self.current_shoot_animation)]
        # self.animate_shoot_ball()

    def animate_move(self):
        self.current_move_animation += 0.02
        if self.current_move_animation >= len(self.move_animations): self.current_move_animation = 0
        self.image = self.move_animations[int(self.current_move_animation)]

    # def animate_shoot_ball(self):
    #     self.current_shoot_ball_animation += 1
    #     if self.current_shoot_ball_animation >= len(self.shoot_ball): self.current_shoot_ball_animation = 0
    #     self.ball = self.shoot_ball[self.current_shoot_ball_animation]
    #     self.display.blit(self.image, self.rect)
    #     if self.direction == "Right": self.display.blit(self.ball, self.rect.midright)
    #     if self.direction == "Left": self.display.blit(self.ball, self.rect.midleft)



    def update(self):
        self.animate_shoot()

class Archer_tower(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.animations = cut_graphics("../characters/7.png", (420, 130))
        self.current_animation = 0
        self.image = self.animations[self.current_animation]
        self.rect = self.image.get_rect(center=pos)


    def animate(self):
        self.current_animation += 0.2
        if self.current_animation >= len(self.animate): self.current_animation = 0
        self.image = self.animations[int(self.current_animation)]

    def update(self):
        self.animate(self)

class Vikings_dragon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        whole_animation = cut_graphics("../dragon/Dragon.png", (160, 133))
        self.front_animations = [whole_animation[0], whole_animation[1], whole_animation[2]]
        self.right_animations = [whole_animation[3], whole_animation[4], whole_animation[5]]
        self.back_animations = [whole_animation[6], whole_animation[7], whole_animation[8]]
        self.left_animations = [whole_animation[9], whole_animation[10], whole_animation[11]]
        self.current_right_animation = 0
        self.current_left_animation = 0
        self.current_front_animation = 0
        self.current_back_animation = 0
        self.image = self.right_animations[self.current_right_animation]
        self.rect = self.image.get_rect(center = pos)
    def animate_right_movement(self):
        self.current_right_animation += 0.2
        if self.current_right_animation >= len(self.right_animations): self.current_right_animation = 0
        self.image = self.right_animations[self.current_right_animation]
    def animate_left_movement(self):
        self.current_left_animation += 0.2
        if self.current_left_animation >= len(self.left_animations): self.current_left_animation = 0
        self.image = self.left_animations[self.current_left_animation]
    def animate_front_movement(self):
        self.current_front_animation += 0.2
        if self.current_front_animation >= len(self.front_animations): self.current_front_animation = 0
        self.image = self.front_animations[self.current_front_animation]
    def animate_back_movement(self):
        self.current_back_animation += 0.2
        if self.current_back_animation >= len(self.back_animations): self.current_back_animation = 0
        self.image = self.back_animations[self.current_back_animation]

class Dragon(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        whole_animation = cut_graphics("../dragon/144x128/flying_twin_headed_dragon-blue.png", (144,128))
        self.front_animations = [whole_animation[0], whole_animation[1], whole_animation[2]]
        self.right_animations = [whole_animation[3], whole_animation[4], whole_animation[5]]
        self.back_animations = [whole_animation[6], whole_animation[7], whole_animation[8]]
        self.left_animations = [whole_animation[9], whole_animation[10], whole_animation[11]]
        self.current_right_animation = 0
        self.current_left_animation = 0
        self.current_front_animation = 0
        self.current_back_animation = 0
        self.image = self.left_animations[self.current_left_animation]
        self.rect = self.image.get_rect(center = pos)
    def animate_right_movement(self):
        self.current_right_animation += 0.2
        if self.current_right_animation >= len(self.right_animations): self.current_right_animation = 0
        self.image = self.right_animations[self.current_right_animation]
    def animate_left_movement(self):
        self.current_left_animation += 0.2
        if self.current_left_animation >= len(self.left_animations): self.current_left_animation = 0
        self.image = self.left_animations[self.current_left_animation]
    def animate_front_movement(self):
        self.current_front_animation += 0.2
        if self.current_front_animation >= len(self.front_animations): self.current_front_animation = 0
        self.image = self.front_animations[self.current_front_animation]
    def animate_back_movement(self):
        self.current_back_animation += 0.2
        if self.current_back_animation >= len(self.back_animations): self.current_back_animation = 0
        self.image = self.back_animations[self.current_back_animation]
