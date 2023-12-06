import pygame

from App.Config import SCALE
from App.Controls import controls

class Player:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.image = pygame.image.load( 'Assets/player.png' ).convert_alpha()
        self.image = pygame.transform.scale( self.image, ( self.image.get_width() * SCALE, self.image.get_height() * SCALE ) )
        self.pos = pygame.math.Vector2( self.surf.get_width() / 2, self.surf.get_height() / 2 )
        self.dir = pygame.math.Vector2()

    def update( self ):
        if controls.d_pad_x < 0 or controls.axis_l_x < -.15:
            self.dir[ 0 ] = -1
        elif controls.d_pad_x > 0 or controls.axis_l_x > .15:
            self.dir[ 0 ] = 1
        else:
            self.dir[ 0 ] = 0
            
        if controls.d_pad_y < 0 or controls.axis_l_y < -.15:
            self.dir[ 1 ] = -1
        elif controls.d_pad_y > 0 or controls.axis_l_y > .15:
            self.dir[ 1 ] = 1
        else:
            self.dir[ 1 ] = 0
        
        self.pos[ 0 ] += self.dir[ 0 ] * 100 / 60
        self.pos[ 1 ] += self.dir[ 1 ] * 100 / 60

    def render( self ):
        self.surf.blit( self.image, self.pos )