import pygame
import random

"""
    Tile 1 - Flat - Cave
    Tile 2 - Down - Cave
    Tile 6 - Flat - Cave
    Tile 8 - Flat - grass
    Tile 9 - Flat - grass
    Tile 10 - Flat - Grass
    Tile 11 - Flat - Cave
    Tile 12 - Flat - Cave
    Tile 13 - Up - Cave
    Tile 14 - Up - Cave
    Tile 16 - Flat - Cave
    Tile 17 - Flat - Grass
    Tile 19 - Up - cave
    Tile 20 - Up - Cave
    Tile 21 - Down - Cave
    Tile 27 - Down - Cave
    Tile 29 - Flat - Purple Grass
    Tile 30 - Flat - Purple Grass
    Tile 31 - Flat - Purple Grass
    
    for right now just use the cave tiles, in the future after a curtain amount of one tiles
    an attempt will be made to switch the biome. Depending on the result the biome will switch
    
"""

"""
    First set the background image and have them merged together to make the length of the level.
    
    Use a function that creates an image for the ground of the level. The way this works is by inputting
    a starting image that sets the hight of the ground. The program can then generate the rest of the
    length of the background with the different ground tiles available to the program.
        - Possible hight variation max's to limit the number of slopes.
        - How to tell if the tile is a slope or not.
        - if it is a slop how to detect if its up or down and then depending on that change the hight
            of the next slope to be placed
    
        Then using this set of tiles the program will generate the hitbox's needed to keep the player on the
        ground.
        
    
    The program will then return one image that has the ground merged with the background image, and
    the hitbox's needed for the player to be on the ground. 
"""

cave_Tiles = [
    [pygame.image.load("Tiles\Tile-01.png"),"Flat"],
    [pygame.image.load("Tiles\Tile-06.png"),"Flat"],
    [pygame.image.load("Tiles\Tile-11.png"),"Flat"],
    [pygame.image.load("Tiles\Tile-12.png"),"Flat"],
    [pygame.image.load("Tiles\Tile-16.png"),"Flat"],
    [pygame.image.load("Tiles\Tile-14.png"),"Up"],
    [pygame.image.load("Tiles\Tile-21.png"),"Down"],
    ]

grass_Tiles_green =[
    pygame.image.load("Tiles\Tile-08.png"),
    pygame.image.load("Tiles\Tile-09.png"),
    pygame.image.load("Tiles\Tile-10.png"),
    pygame.image.load("Tiles\Tile-17.png"),
]

grass_Tiles_purple =[
    pygame.image.load("Tiles\Tile-29.png"),
    pygame.image.load("Tiles\Tile-30.png"),
    pygame.image.load("Tiles\Tile-31.png"),
]

def random_block(tile_type):
    if tile_type == "Flat":
        random_number = random.randint(0,4)
        return cave_Tiles[random_number]
    if tile_type == "Up":
        #random_number = random.randint(5,7)
        return cave_Tiles[5]
    if tile_type == "Down":
        #random_number = random.randint(7,10)
        return cave_Tiles[6]

def background():
    background = pygame.image.load("Backgrounds\merged-full-background.png")
    ground_tiles = generate_ground()
    
def generate_ground(length):
    tile_amount = length - 3
    groundtiles = []
    groundtiles.append(random_block("Flat"))
    groundtiles.append(random_block("Flat"))
    groundtiles.append(random_block("Flat"))
    for tiles in range(tile_amount):
        #print(groundtiles[-1])
        
        if groundtiles[-1][1] == "Flat":
            #print("Flat")
            tile_temp = "Flat"
            for x in range(0,2):
                if groundtiles[-x][1] == "Up":
                    tile_temp = "Up"
                if groundtiles[-x][1] == "Down":
                    tile_temp = "Down"
            if tile_temp == "Flat":
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Down","Up"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Down":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Up":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
            
        if groundtiles[-1][1] == "Up":
            tile_temp = "Up"
            for x in range(0,2):
                if groundtiles[-x][1] == "Flat":
                    tile_temp = "Flat"
                if groundtiles[-x][1] == "Up":
                    tile_temp = "Up"
            if tile_temp == "Flat":
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Down","Up"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Down":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Up":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
                
        if groundtiles[-1][1] == "Down":
            tile_temp = "Down"
            for x in range(0,2):
                if groundtiles[-x][1] == "Flat":
                    tile_temp = "Flat"
                if groundtiles[-x][1] == "Down":
                    tile_temp = "Down"
                    
            print(tile_temp)
            if tile_temp == "Flat":
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Down","Up"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Down":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Up":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
                
    #ground_image = pygame.display.set_mode((700, 700))
    #ground_image = pygame.image.load("Tiles\Tile-01.png")
    ground_image = pygame.Surface((length * 48, 700))
    ground_hitbox = []
    x = 0
    y = 500
    
    
    for tile in groundtiles:
        if tile[1] == "Flat":
            ground_image.blit(tile[0],(x,y))
            ground_hitbox.append(pygame.Rect(x, y, 22, 100))
            x += 22
        if tile[1] == "Down":
            if y > 650:
                ground_image.blit(pygame.image.load("Tiles\Tile-01.png"),(x,y))
                ground_hitbox.append(pygame.Rect(x, y, 22, 100))
                x += 22
            else:
                ground_image.blit(tile[0],(x,y))
                ground_hitbox.append(pygame.Rect(x, y, 44, 100))
                y += 20
                x += 44
        if tile[1] == "Up":
            if y < 400:
                ground_image.blit(pygame.image.load("Tiles\Tile-01.png"),(x,y))
                ground_hitbox.append(pygame.Rect(x, y, 22, 100))
                x += 22
            else:
                y -= 14
                ground_image.blit(tile[0],(x,y))
                ground_hitbox.append(pygame.Rect(x, y, 22, 100))
                x += 22
        #print(y)
        #x += 24
        #print(x)
        for temp in range(0, 13):
            ground_image.blit(random.choice([pygame.image.load("Tiles\Tile-03.png"),]),(x,y+temp*22 + 12))
            
        #add somthing that add's all of the different tiles to a hitbox list that can be plugged into the
        #   player class
            

         
    return [ground_image,ground_hitbox]