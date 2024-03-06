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

def background(screen,ground_tiles,ground_hitbox):
    
    objects = [
        [pygame.image.load("Misc\House-Background-01.png")],
        [pygame.image.load("Misc\House-01.png"), -32,3],
        [pygame.image.load("Misc\House-02.png"), -32,3],
        [pygame.image.load("Misc\Bush-Background.png"), 10,3],
        [pygame.image.load("Misc\Bush-Green-Foreground.png"), 10,3],
        [pygame.image.load("Misc\Bush-Purple-Foreground.png"), 10,3],
        #[pygame.image.load("Objects\Obj-Light-01.png"), 10,2],
        #[pygame.image.load("Objects\Obj-Fence.png"), 10,2],
        #[pygame.image.load("Objects\Obj-Barrel.png"), 10,1],
        [pygame.image.load("Objects\Obj-Statue.png"), 5,3]
    ]
    
    background = pygame.image.load("Backgrounds\merged-full-background.png")
    
    background = pygame.transform.scale(background, (340,500))
    length = ground_tiles.get_width()
    background_surface = pygame.Surface((length, 500))
    tiles = int(length/background.get_width())
    background_width = background.get_width()
    ground_tiles.set_colorkey((0, 0, 0)) 
    
    for x in range(tiles):
        background_surface.blit(background, (x*background_width, 0))
    
    for x in range(0,len(ground_hitbox)-10, 10):
        
        if ground_hitbox[x][1] == ground_hitbox[x+3][1]:
            background_surface.blit(objects[0][0],(ground_hitbox[x][0],ground_hitbox[x][1]-32))
            #print("house")
            
        placement_areas = []
        for y in range(0,10):
            if ground_hitbox[x + y][1] == ground_hitbox[x+ y + 1][1]:
                placement_areas.append(y)
        #print(placement_areas)
        
        print(len(placement_areas))
        
        if len(placement_areas) > 2:
            
            while len(placement_areas) > 2:
                print(len(placement_areas))
                random_obj = random.randint(1,len(objects) - 1)
                if objects[random_obj][2] > len(placement_areas):
                    background_surface.blit(objects[random_obj][0],(ground_hitbox[x+5][0],ground_hitbox[x+5][1] + objects[random_obj][1]))
                    
                    
                    #for x in range(objects[random_obj][2]):
                    #    print("hi")
                    #    placement_areas.pop()
                    
                else:
                    placement_areas.pop()
        
        #background_surface.blit(objects[0],(ground_hitbox[x][0],ground_hitbox[x][1]-32))
        #background_surface.blit(objects[random_obj][0],(ground_hitbox[x+5][0],ground_hitbox[x+5][1] + objects[random_obj][1]))
        
        
    background_surface.blit(ground_tiles, (0,0))
    
    return background_surface
        
    
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
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Flat","Flat","Flat","Flat","Down","Up"])
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
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Flat","Flat","Flat","Flat","Down","Up"])
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
                    
            #print(tile_temp)
            if tile_temp == "Flat":
                random_tile = random.choice(["Flat","Flat","Flat","Flat","Flat","Flat","Flat","Flat","Down","Up"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Down":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
            if tile_temp == "Up":
                random_tile = random.choice(["Flat"])
                groundtiles.append(random_block(random_tile))
                
    ground_image = pygame.Surface((length * 48, 500))
    ground_hitbox = []
    x = 0
    y = 400
    
    for tile in groundtiles:
        if tile[1] == "Flat":
            ground_image.blit(tile[0],(x,y))
            ground_hitbox.append(pygame.Rect(x, y - 42, 22, 100))
            x += 22
        if tile[1] == "Down":
            if y > 450:
                ground_image.blit(pygame.image.load("Tiles\Tile-01.png"),(x,y))
                ground_hitbox.append(pygame.Rect(x, y - 42, 22, 100))
                x += 22
            else:
                ground_image.blit(tile[0],(x,y))
                ground_hitbox.append(pygame.Rect(x, y - 40, 44, 100))
                y += 20
                x += 44
        if tile[1] == "Up":
            if y < 300:
                ground_image.blit(pygame.image.load("Tiles\Tile-01.png"),(x,y))
                ground_hitbox.append(pygame.Rect(x, y - 42, 22, 100))
                x += 22
            else:
                y -= 14
                ground_image.blit(tile[0],(x,y))
                ground_hitbox.append(pygame.Rect(x, y - 34, 22, 100))
                x += 22

        for temp in range(0, 13):
            ground_image.blit(random.choice([pygame.image.load("Tiles\Tile-03.png"),]),(x,y+temp*22 + 12))      
         
    return [ground_image,ground_hitbox]

def hitbox_update(hitboxs, step):
    for hitbox in hitboxs:
        hitbox[0] -= step
     