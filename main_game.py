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
mixer.music.set_volume(0.2) 
  
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


"""
    
Make it so that the player is in the rain during the game, and the checkpoints are shacks that have
light's inside of them that are rest areas for the player to rest at. 
    
Title: "Windkeep: Twin Shadows"

Theme:
"Windkeep: Twin Shadows" immerses players in a medieval-fantasy world where the winds guide them
on a solitary journey to confront the twin sisters, Leona and Cassandra. In the kingdom of
Windkeep, players navigate treacherous terrain, solve puzzles, and engage in combat as they unravel the
twisted tale of two sisters consumed by ambition and darkness. With a blend of strategic challenges and
thrilling action, players embark on a quest to dispel the eternal storm and restore balance to the realm.

Main Storyline:
In the once-beautiful land of Windkeep, the land is now battered by perpetual winds, a manifestation of the
malevolent sorcery of the twin sisters. Trained by different elder mages, the sisters were once equal heirs
to the throne. While Cassandra remained pure and loyal to the throne, Leona was succumbed by the power of
darkness, consumed by ambition and driven by a hunger for power. She took control of her sisters 
body after a battle between the two of them. Together they now control the throne and plunged the land into a
perpetual rainfall.

As a lone adventurer, players find themselves guided by the winds to Windkeep, the ancient castle where the
twin sisters once trained. Along their journey, they uncover fragments of the past and whispers of the wind,
revealing the tragic history of the twins and their connection to the perpetual storm that ravages Windkeep.

Within the land's of Windkeep, players confront challenges crafted by the twisted minds of Leona and Cassandra,
each test designed to test their resolve and courage. As they delve deeper into the castle of Windkeep's
darkness they confront the manifestations of the sisters's corrupted ambitions, each more formidable and 
challenging than the last.

As the story unfolds, players uncover the truth behind the twins' tragic history and their connection to the
perpetual storm. With each victory, they draw closer to confronting Leona and Cassandra and
bringing an end to their reign of terror. In a final showdown, players must confront the darkness within
themselves to overcome the twin sisters and restore light to the kingdom.
    
"""