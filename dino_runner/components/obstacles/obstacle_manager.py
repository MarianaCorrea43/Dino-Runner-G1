
import random
from typing import Self
import pygame
from dino_runner.components import game
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.largecactus import LargeCactus
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.smallcactus import SmallCactus


class ObstacleManager:
    def __init__(self):
        self.obstacles: list[Obstacle] = []

    def update(self, game):
        if not self.obstacles:
            self.obstacles.append(self.bird2())

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if obstacle.rect.colliderect(game.player.rect):
                pygame.time.delay(500)
                game.playing = False

    def bird2(self):
        bird21 = [LargeCactus(), Bird(), SmallCactus()]
        return bird21[random.randint (0,2)]
    

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)




