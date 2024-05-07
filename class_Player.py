import pygame
import time
from background import*

class player:
    def __init__ (self, name, picture, speed, weapon, health,
                    armour_Type, spawn_X, spawn_Y, screen, background_hitbox):
        self.name = name
        self.picture = picture
        self.speed = speed
        self.weapon = weapon
        self.health = health
        self.armour_Type = armour_Type
        self.spawn_X = spawn_X
        self.spawn_Y = spawn_Y
        self.current_X = spawn_X
        self.current_Y = spawn_Y
        self.Rect = pygame.Rect(self.current_X, self.current_Y, 10,10)
        self.movement = 1
        self.screen = screen
        self.fall_speed = 0
        self.gravity = 0.75
        self.screen_height = 700
        self.character_height = 20
        self.jump_Cooldown = 0
        self.frame = 0
        self.direction = "Right"
        self.direction_change = "Right"
        self.background_hitbox = background_hitbox.copy()
        self.background_x = 0
        self.temp_x = 0
        self.temp_y = 0
        self.animation_dictionary = {
                "idle": self.animate("_Idle.png"),
                "walk": self.animate("_Run.png"),
                "attack": self.animate("Outline/120x80_PNGSheets/_Attack.png"),
                "jump": self.animate("Outline/120x80_PNGSheets/_Jump.png"),
                "roll": self.animate("Outline/120x80_PNGSheets/_Roll.png"),
                "crouch": self.animate("Outline/120x80_PNGSheets/_CrouchWalk.png")
                }
        self.current_animation = self.animation_dictionary["idle"]
        self.no_current = False
        self.attack_cooldown = 0

    def movement_Update(self):
        
        self.temp_x = self.current_X
        self.temp_y = self.current_Y
        
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
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1
        
        if keys[pygame.K_DOWN] == True:
            if self.detect_collision():
                self.currentAnimation("crouch") 
        if self.is_moving() == False and self.in_air() == False:
            self.currentAnimation("idle")
        if self.in_air():
            self.currentAnimation("jump")
        if self.in_air() == False and self.is_moving() == True:
            self.currentAnimation("walk")    
        if self.no_current == True:
            self.update_Animation(self.current_animation, self.step)

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
            
    def is_moving(self):
        isMoving = False
        if self.current_X != self.temp_x or self.current_Y != self.temp_y:
            isMoving = True
        return isMoving
            
    def in_air(self): 
        inAir = True
        for bounding_Box in self.background_hitbox:
            if self.Rect.colliderect(bounding_Box) == True:
                inAir = False
        return inAir
        
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
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:    
                if self.attack_cooldown <= 0:
                    self.currentAnimation("attack")  
                    self.attack_cooldown = 4
    
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
            
    def update_Animation(self,sheet,step):
        
        image = sheet[step]
        
        #print(image)
            
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
        
    def rolling_background(self,background_x):
        if self.current_X > 350 and self.temp_x != self.current_X:
            hitbox_update(self.background_hitbox, 5)
            self.current_X -= 5
            return 5
        elif self.current_X < 350 and self.temp_x != self.current_X:
            if background_x < 0:
                hitbox_update(self.background_hitbox, -5)
                self.current_X += 5
                return -5
            else:
                return 0
        else:
            return 0