from class_Enemy import enemy
from class_Player import player
from class_Platform import platform
from background import generate_ground
from background import background
import pygame
from pygame import mixer 

pygame.init() #initialize's pygame 
mixer.init() 
screen = pygame.display.set_mode((700, 500)) #(screen size x, screen size y)
clock = pygame.time.Clock()
running = True
ground = generate_ground(100)
ground_image = ground[0]
background_hitbox = ground[1]
background = background(screen,ground_image,background_hitbox)

#class initialize
walker = enemy("Walker", "pass", 10, 2, 2, "Walker", "pass", "pass", "pass", "pass", "pass", "pass", "none", 150, 391, screen)
player = player("Player", "pass", 10, 10, 20, "Walker", "pass", "pass", "pass", "pass", "pass", "pass", "none", 350, 300, screen, background_hitbox)


#Platform rects
obstacle_rect = [
    pygame.Rect(0, 600, 700, 100), 
    pygame.Rect(100, 400, 100, 10),
    pygame.Rect(300, 500, 100, 10),
    pygame.Rect(500, 300, 100, 10)
]
    
mixer.music.load("Music.mp3") 
  
# Setting the volume 
mixer.music.set_volume(0) 
  
# Start playing the song 
mixer.music.play() 

bk_x = 0
    
while running:
    for event in pygame.event.get(): # poll for events
        if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
            running = False
            
    # RENDER YOUR GAME HERE
    bk_x -= player.rolling_background(bk_x)
    screen.blit(background,(bk_x ,0))
    player.display_Health()
    #walker.movement_Update(obstacle_rect)
    player.movement_Update()
    #running = player.health_Update(walker.attack(player.reference_Rect()))
    
    #player.attack()
    
    pygame.display.update()
    
    clock.tick(20)  # limits FPS to 20
pygame.quit()