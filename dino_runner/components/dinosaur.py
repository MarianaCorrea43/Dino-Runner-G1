import pygame
from pygame import Surface
from pygame.sprite import  Sprite
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"


class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310 
    POS_Y_DUCK = POS_Y +35 
    JUMP_VELOCITY = 8.5

    def __init__(self):
        self.image = RUNNING[0]
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY
        self.position()

    def position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X 
        self.rect.y = self.POS_Y

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else:
                self.action = DINO_RUNNING

            if self.step  >= 10:
                self.step = 0

    def duck(self):
        self.update_image(DUCKING[self.step //5], pos_y=self.POS_Y_DUCK)
        self.step += 1

    def update_image(self, image: pygame.Surface, pos_x=None, pos_y=None):
        self.image = image
        self.rect = image.get_rect()
        self.rect.x = pos_x or self.POS_X
        self.rect.y = pos_y or self.POS_Y 

        """self.image = DUCKING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y + 35
        self.step += 1
        self.position()"""

    def run(self):
        self.image = RUNNING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X 
        self.rect.y = self.POS_Y
        self.step += 1
        self.position()

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        print(self.rect.y, self.jump_velocity, sep="::")
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMP_VELOCITY
            self.position()


    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))




