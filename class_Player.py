import pygame
import time
from background import*

class player:
    def __init__ (self, name, picture, speed, weapon, health, type_Enemy,
                  death_Animation, death_Sound, movement_Sound, attack_Sound, attack_Animation,
                  movement_Animation, armour_Type, spawn_X, spawn_Y, screen, background_hitbox):
        self.name = name
        self.picture = picture
        self.speed = speed
        self.weapon = weapon
        self.health = health
        self.type_Enemy = type_Enemy
        self.death_animation = death_Animation
        self.death_Sound = death_Sound
        self.attack_Sound = attack_Sound
        self.movement_Sound = movement_Sound
        self.attack_Animation = attack_Animation
        self.movement_Animation = movement_Animation
        self.armour_Type = armour_Type
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.current_X = spawn_X
        self.current_Y = spawn_Y
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 10,10)
        self.movement = 1
        self.screen = screen
        self.obstacle_rect = [
            pygame.Rect(0, 580, 700, 100), 
            pygame.Rect(100, 380, 100, 10),
            pygame.Rect(300, 480, 100, 10),
            pygame.Rect(500, 280, 100, 10)
        ]
        self.fall_speed = 0
        self.gravity = 0.35
        self.screen_height = 700
        self.character_height = 20
        self.jump_Cooldown = 0
        self.frame = 0
        self.direction = "Right"
        self.direction_change = "Right"
        self.background_hitbox = background_hitbox
        self.background_x = 0

    def movement_Update(self):
        
        temp_x = self.current_X
        temp_y = self.current_Y
        
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 10,10)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.current_X -= 5
            self.direction = "Right"
            
        if keys[pygame.K_RIGHT]:
            self.current_X += 5
            self.direction = "Left"
        
        if keys[pygame.K_DOWN]:
            if self.detect_collision():
                self.fall_speed = 0
            else:
                if self.fall_speed <= 15:
                    self.fall_speed += 5
                
        if keys[pygame.K_UP]:
            self.fall_speed = -10
        else:
            if self.detect_collision():
                if self.fall_speed != 0:
                    self.fall_speed = 0
            else: 
                self.fall_speed += self.gravity
        
        self.current_Y += self.fall_speed
        
        
        time.sleep(0.01)
        
        if self.current_X != temp_x or self.current_Y != temp_y:
            self.update_Animation(True)
        else:
            self.update_Animation(False)
        
    def health_Update(self, health_Change):
        self.health -= int(health_Change)
        print(self.health)
        self.display_Health()
        if self.health <= 0:
            return False
            #death animation
        else:
            return True
            
    def attack(self):
        self.animate("_Attack.png")
    
    def detect_collision(self):
        
        for bounding_Box in self.background_hitbox:
            if self.Rect.colliderect(bounding_Box) == True:
                self.current_Y = bounding_Box.top
                return True
    
    def reference_Rect(self):
        return self.Rect
    
    def display_Health(self):
        font = pygame.font.SysFont("calibri", 40)
        text = font.render(str(self.health),True, (0, 255, 0))
        self.screen.blit(text, (10, 10))
        
    def animate(self, image):
        character_image = pygame.image.load(image)
        character_rect = character_image.get_rect()
        character_height = character_rect.height
        frames = character_image.get_width()/120
        
        frames_image = []
        
        for x in range(0,int(frames)):
            frames_image.append(character_image.subsurface(pygame.Rect(x * 120, 0, character_image.get_width() // frames, character_image.get_height()-4)))
            
        return frames_image
            
    def update_Animation(self,step):
        
        frames = self.animate("_Run.png")
        frames_idle = self.animate("_idle.png")
        image = ""
        
        if step == True:
            if self.frame > len(frames):
                self.frame = 0
            self.frame = self.frame + 1  
            image = frames[self.frame - 1]
        
        if step == False:
            if self.frame > len(frames_idle):
                self.frame = 0
            self.frame = self.frame + 1
            image = frames_idle[self.frame - 1]
        
        if len(frames) <= self.frame:
            self.frame = 0
            
            
        if self.direction_change == self.direction == "Right":
            image = pygame.transform.flip(image, True, False)
        elif self.direction_change == self.direction == "Left":
            image = pygame.transform.flip(image, True, False)
        
        self.screen.blit(image, (self.current_X - image.get_width()/2,self.current_Y - image.get_height()/2))
        
    def rolling_background(self,background_x):
        if self.current_X > 600:
            hitbox_update(self.background_hitbox, 5)
            return 5
        elif self.current_X < 100:
            if background_x < 0:
                hitbox_update(self.background_hitbox, -5)
                return -5
            else:
                return 0
        else:
            return 0