import pygame, random

class MenuVirus:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.pos = pygame.math.Vector2( random.randint( 0, self.surf.get_width() ), random.randint( 0, self.surf.get_height() ) )
        self.vel = pygame.math.Vector2( random.random() * 6 - 3, random.random() * 6 - 3 )