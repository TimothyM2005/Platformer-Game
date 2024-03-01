import pygame
import sys

pygame.init()

# Create surfaces
surface1 = pygame.Surface((50, 50))
surface1.fill((255, 0, 0))  # Red square
surface1.set_colorkey((0, 0, 0))  # Set black as transparent color
mask1 = pygame.mask.from_surface(surface1)

surface2 = pygame.Surface((50, 50))
surface2.fill((0, 255, 0))  # Green square
surface2.set_colorkey((0, 0, 0))  # Set black as transparent color
mask2 = pygame.mask.from_surface(surface2)

# Check for collision
collision = mask1.overlap(mask2, (0, 0))

print("Collision detected:", collision is not None)

pygame.quit()
sys.exit()
