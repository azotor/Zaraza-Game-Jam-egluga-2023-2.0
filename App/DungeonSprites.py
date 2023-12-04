import pygame

from App.Config import SCALE

class DungeonSprites:
    def __init__( self ):
        self.size = 32
        self.sprites = {}
        self.image = pygame.image.load( 'Assets/dungeon.png' ).convert_alpha()
        self.gridX = int( self.image.get_width() / self.size )
        self.create( 'corner', 0 )
        self.create( 'wall', 1 )
        self.create( 'floor', 2 )
        self.create( 'leftcorner', 3 )
        self.create( 'exit', 4 )
        self.create( 'rightcorner', 5 )
        self.create( 'column', 6 )
    
    def create( self, name, id ):
        image = pygame.Surface( ( self.size, self.size ) ).convert_alpha()
        image.fill( ( 0, 0, 0 ) )
        image.blit( self.image, ( 0, 0 ), ( ( id % self.gridX ) * self.size, ( id // self.gridX ) * self.size, self.size, self.size ) )
        image = pygame.transform.scale( image, ( self.size * SCALE, self.size * SCALE ) )
        image.set_colorkey( ( 0, 0, 0 ) )
        self.sprites[ name ] = image

    def get( self, name ):
        return self.sprites[ name ]
    
    def getRotate( self, name, angle ):
        return pygame.transform.rotate( self.get( name ), angle )