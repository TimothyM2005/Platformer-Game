#from main_game import screen
import pygame
from background import*

class enemy_Slime:
    def __init__ (self, name, spawn_X, spawn_Y, screen, background_hitbox):
        self.name = name
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.screen = screen
        
        #Movement
        self.background_hitbox = background_hitbox.copy()
        self.current_X = spawn_X
        self.current_Y = spawn_Y
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 17,17)
        self.fall_speed = 0
        self.gravity = 0.5
        self.speed = {
            "pink": 2,
            "red": 3,
            "yellow": 4,
            "blue": 5,
            "green": 6, 
            "brown": 7,
            "grey": 8
        }
        
        #Animation
        self.anitmations = {
                "die": 2,
                "hit": 3,
                "idle1": 4,
                "idle2": 5,
                "idle3": self.animate("Slimes/slime_idle3.png"), 
                "jump": 7,
                "move": 8,
                "swallow": 10
            }
        
    def animate(self, image): #Returns a list of frames for the given animation
        slime_image = pygame.image.load(image)
        frames = slime_image.get_width()/80
        frames_image = []
        
        for x in range(0,int(frames)):
            frames_image.append(slime_image.subsurface(pygame.Rect(x * 80, 0, slime_image.get_width() // frames, slime_image.get_height())))
            
        return frames_image
    
    def movement_Update(self):
        image = self.anitmations["idle3"][0]
        self.calculate_movement()
        self.detect_collision()
        self.screen.blit(image, (self.current_X - image.get_width()/2,self.current_Y))
        
    def calculate_movement(self):
        self.current_X = self.current_X + 1
        hitbox_update(self.background_hitbox, 1)
    
    def detect_collision(self):
        for bounding_Box in self.background_hitbox:
            if self.Rect.colliderect(bounding_Box) == True:
                print(self.current_Y)
                self.current_Y = bounding_Box.top
                return True
    
    def back_Forth(self, obstacle_Bounding):
        pass
        
    def health_Update(self, health_Change) -> int:
        pass
            
    def attack(self, target):
        pass