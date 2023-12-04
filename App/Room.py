import pygame

from App.Config import SCALE

class Room:

    def __init__( self, pos, sprites ):
        self.pos = pos
        self.doors = [ 0, 0, 0, 0 ]
        self.visited = 0
        self.surf = pygame.display.get_surface()
        self.sprites = sprites
    
    def hasAllDoors( self ):
        return sum( self.doors ) == 4

    def hasDoor( self, door ):
        return self.doors[ door ] == 1

    def render( self ):
        size = 32
        gridX = int( self.surf.get_width() / size / SCALE )
        gridY = int( self.surf.get_height() / size / SCALE )
        self.surf.blit( self.sprites.get( 'corner' ), ( 0, 0 ) )
        self.surf.blit( self.sprites.getRotate( 'corner', 90 ), ( 0, ( gridY - 1 ) * size * SCALE ) )
        self.surf.blit( self.sprites.getRotate( 'corner', 180 ), ( ( gridX - 1 ) * size * SCALE, ( gridY - 1 ) * size * SCALE ) )
        self.surf.blit( self.sprites.getRotate( 'corner', 270 ), ( ( gridX - 1 ) * size * SCALE, 0 ) )
        for i in range( 1, gridX - 1 ):
            self.surf.blit( self.sprites.get( 'wall' ), ( i * size * SCALE, 0 ) )
        for i in range( 1, gridY - 1 ):
            self.surf.blit( self.sprites.getRotate( 'wall', 90 ), ( 0, i * size * SCALE ) )
        for i in range( 1, gridX - 1 ):
            self.surf.blit( self.sprites.getRotate( 'wall', 180 ), ( i * size * SCALE, size * 10  * SCALE) )
        for i in range( 1, gridY - 1 ):
            self.surf.blit( self.sprites.getRotate( 'wall', 270 ), ( size * 10 * SCALE, i * size * SCALE ) )
        for i in range( 1, gridX - 1 ):
            for j in range( 1, gridY - 1 ):
                self.surf.blit( self.sprites.get( 'floor' ), ( j * size * SCALE, i * size * SCALE ) )