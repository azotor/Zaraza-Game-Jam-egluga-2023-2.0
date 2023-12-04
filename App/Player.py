import pygame

from App.Config import SCALE
from App.Events import pad

class Player:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.image = pygame.image.load( 'Assets/player.png' ).convert_alpha()
        self.image = pygame.transform.scale( self.image, ( self.image.get_width() * SCALE, self.image.get_height() * SCALE ) )
        self.pos = pygame.math.Vector2( self.surf.get_width() / 2, self.surf.get_height() / 2 )
        self.dir = pygame.math.Vector2()

    def update( self ):
        if pad[ 'axis' ][ 'l' ][ 'x' ] < -.3:
            self.dir[ 0 ] = -1
        elif pad[ 'axis' ][ 'l' ][ 'x' ] > .3:
            self.dir[ 0 ] = 1
        else:
            self.dir[ 0 ] = 0
            
        if pad[ 'axis' ][ 'l' ][ 'y' ] < -.3:
            self.dir[ 1 ] = -1
        elif pad[ 'axis' ][ 'l' ][ 'y' ] > .3:
            self.dir[ 1 ] = 1
        else:
            self.dir[ 1 ] = 0
        
        self.pos[ 0 ] += self.dir[ 0 ] * 100 / 60
        self.pos[ 1 ] += self.dir[ 1 ] * 100 / 60

    def render( self ):
        self.surf.blit( self.image, self.pos )