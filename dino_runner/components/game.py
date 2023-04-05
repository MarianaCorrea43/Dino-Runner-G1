from tkinter import font
import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.obstacles.score import Score
from dino_runner.utils.constants import BG, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, START, TITLE, FPS

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.score = Score()
        self.death_count = 0
        self.high_score = 0
       
      

    def run(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
                
  
        pygame.quit()

    def play(self):
        self.playing = True
        self.obstacle_manager.reset()
        while self.playing:
           self.events()
           self.update()
           self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            
                
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(
            self.game_speed, self.player, self.on_death)
        self.score.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def on_death(self):
        pygame.time.delay(500)
        self.playing = False
        self.death_count += 1
        print("I am dead")
        print(self.death_count)
        #if self.score.score > self.high_score:
            #self.hight_score = self.score.score
        
    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        self.screen.fill((255, 255, 255))
        if self.death_count:
            self.screen.blit(GAME_OVER, (360, 325))
            self.print_menu(90,140,"High Score: " + str(self.high_score))
            self.print_menu(90,100,"Death Count: " + str(self.death_count))
        else:
            font = pygame.font.Font("freesansbold.ttf", 30)
            text = font.render("Push any key to begin", True,(0,0,0))
            text_rect  = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)
            self.screen.blit(START, (half_screen_width - 45, half_screen_height - 140))
  
        pygame.display.flip()
        self.menu_events()

    def print_menu(self,x,y, message ):
        font = pygame.font.Font("freesansbold.ttf", 30)
        text = font.render(message, True,(0,0,0)) 
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        self.screen.blit(text, (half_screen_width - x, half_screen_height + y))

    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()



    



        
    
