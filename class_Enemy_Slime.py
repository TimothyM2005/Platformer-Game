#from main_game import screen
import pygame


"""
    -Add animations for the slime
    -work on making an attack
    -add an actual working movement system to the player including jumps
    -add other colors of slime to that have different stats
    
"""

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
        self.speed = 5
        
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
        
    def hitbox_update(self, hitboxs, step):
        for hitbox in hitboxs:
            hitbox[0] -= step
        
    def animate(self, image): #Returns a list of frames for the given animation
        slime_image = pygame.image.load(image)
        frames = slime_image.get_width()/80
        frames_image = []
        
        for x in range(0,int(frames)):
            frames_image.append(slime_image.subsurface(pygame.Rect(x * 80, 0, slime_image.get_width() // frames, slime_image.get_height())))
            
        return frames_image
    
    def currentAnimation(self, action):
        #Detect for idle walk attack jump roll crouch
        if self.no_current == False:
            self.step = 0
            self.no_current = True
            if action == "jump":
                self.update_Animation(self.animation_dictionary["jump"], self.step)
                self.current_animation = self.animation_dictionary["jump"]
            if action == "walk":
                self.update_Animation(self.animation_dictionary["walk"], self.step)
                self.current_animation = self.animation_dictionary["walk"]
            if action == "idle":
                self.update_Animation(self.animation_dictionary["idle"], self.step)
                self.current_animation = self.animation_dictionary["idle"]
            if action == "attack":
                self.update_Animation(self.animation_dictionary["attack"], self.step)
                self.current_animation = self.animation_dictionary["attack"]
            if action == "roll":
                self.update_Animation(self.animation_dictionary["roll"], self.step)
                self.current_animation = self.animation_dictionary["roll"]
            if action == "crouch":
                self.update_Animation(self.animation_dictionary["crouch"], self.step)
                self.current_animation = self.animation_dictionary["crouch"]
    
    def update_Animation(self,sheet,step):
        
        image = sheet[step]
            
        if self.direction_change == self.direction == "Right":
            image = pygame.transform.flip(image, True, False)
        elif self.direction_change == self.direction == "Left":
            image = pygame.transform.flip(image, True, False)
        
        self.screen.blit(image, (self.current_X - image.get_width()/2,self.current_Y - image.get_height()/2))
        
        #print(len(sheet))
        #print(step)
        
        if len(sheet)-2 <= step:
            self.no_current = False
        else:
            self.step += 1
    
    def movement_Update(self):
        image = self.anitmations["idle3"][0]
        self.calculate_movement()
        self.detect_collision()
        self.screen.blit(image, (self.current_X - image.get_width()/2,self.current_Y))
        
    def calculate_movement(self):
        self.current_X = self.current_X + 1
        #self.hitbox_update(self.background_hitbox, 1)
    
    def detect_collision(self):
        for bounding_Box in self.background_hitbox:
            if self.Rect.colliderect(bounding_Box) == True:
                print(self.current_Y)
                self.current_Y = bounding_Box.top + 26
                return True
    
    def back_Forth(self, obstacle_Bounding):
        pass
        
    def health_Update(self, health_Change) -> int:
        pass
            
    def attack(self, target):
        pass