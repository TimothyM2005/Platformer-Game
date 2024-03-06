#from main_game import screen
import pygame

class enemy:
    def __init__ (self, name, picture, speed, attack_Damage, health, type_Enemy,
                  death_Animation, death_Sound, movement_Sound, attack_Sound, attack_Animation,
                  movement_Animation, armour_Type, spawn_X, spawn_Y, screen):
        self.name = name
        self.picture = picture
        self.speed = speed
        self.damage = attack_Damage
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
        self.cooldown = 0

        """
        Movement Update -> (updated X and Y coordinates)
            - Enemy to player distance calculation -> (Separate function)
            - Movement to the player calculation -> (Separate function)
            - Movement sounds
            
        Health Update -> (Changes the health of the enemy)
            - Either gaining or losing health
            - Death animation and sound
        """
    
    def movement_Update(self, obstacle_Bounding):
        if self.type_Enemy == "hopper" or self.type_Enemy == "Runner":
            pass
            #self.chase_Player(self, obstacle_Bounding)
        else:
            self.back_Forth(obstacle_Bounding)
        
    def chase_Player(self, obstacle_Bounding):
        """
            Calculate the direction and the distance to the player
            How to have the enemies chase the player
        """
        pass
    
    def back_Forth(self, obstacle_Bounding):
        
        obstacle_Bound = 0
        
        for bounding_Box in obstacle_Bounding:
            if self.Rect.colliderect(bounding_Box) == True:
                obstacle_Bound = bounding_Box
        
        self.current_X += self.movement #* self.speed
        
        if obstacle_Bound != 0:
            if self.current_X < obstacle_Bound[0]:
                self.movement = 1
            elif self.current_X >  obstacle_Bound[0] + obstacle_Bound[2]-10:
                self.movement = -1
            
        pygame.draw.rect(self.screen, (0, 250, 0), (self.current_X, self.current_Y, 10, 10))
        
        #pygame.display.update()
        
    def health_Update(self, health_Change) -> int:
        if self.type == "hopper" or "Runner" or "walker":
            if self.armour_Type == "leather":
                self.health -= health_Change/4
            if self.armour_Type == "iron":
                self.health -= health_Change/8
            if self.armour_Type == "gold":
                self.health -= health_Change/12
            else:
                self.health -= health_Change
        if self.health <= 0:
            pass
            #death animation
            
    def attack(self, target):
        #print(self.Rect.colliderect(target))
        target = pygame.Rect(target[0], target[1] + 12, target[2], target[3])
        if self.cooldown <= 0:
            if self.Rect.colliderect(target):
                self.cooldown += 100
                return self.damage
            else:
                return 0
        else:
            self.cooldown -= 1
            return 0