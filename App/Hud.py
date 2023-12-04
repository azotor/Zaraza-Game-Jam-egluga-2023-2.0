import pygame

from App.Config import SCALE
from App.Events import pad

class Hud:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.image = pygame.image.load( 'Assets/hud.png' ).convert_alpha()
        self.gridSize = 16
        self.gridX = self.image.get_width() / self.gridSize
        self.gridY = self.image.get_height() / self.gridSize
        self.sprites = {}
        self.data = {
            'heart' : 100,
            'mana' : 100,
            'a' : 1,
            'b' : 0,
            'x' : 0,
            'y' : 0
        }
        self.selectedAttac = 'a'
        self.cutSprite( 'green-lock', 0 )
        self.cutSprite( 'red-lock', 1 )
        self.cutSprite( 'blue-lock', 2 )
        self.cutSprite( 'yellow-lock', 3 )
        self.cutSprite( 'green-unlock', 4 )
        self.cutSprite( 'red-unlock', 5 )
        self.cutSprite( 'blue-unlock', 6 )
        self.cutSprite( 'yellow-unlock', 7 )
        self.cutSprite( 'heart', 8 )
        self.cutSprite( 'mana', 9 )
    
    def cutSprite( self, name, id ):
        image = pygame.Surface( ( self.gridSize, self.gridSize ) ).convert_alpha()
        image.fill( ( 0, 0, 0 ) )
        image.blit( self.image, ( 0, 0 ), ( ( id % self.gridX ) * self.gridSize, ( id // self.gridX ) * self.gridSize, self.gridSize, self.gridSize ) )
        image = pygame.transform.scale( image, ( self.gridSize * SCALE, self.gridSize * SCALE ) )
        image.set_colorkey( ( 0, 0, 0 ) )
        self.sprites[ name ] = image

    def update( self, data ):
        self.data = data

    def render( self ):
        self.hearts()
        self.mana()
        self.attacks()
    
    def hearts( self ):
        pygame.draw.rect( self.surf, ( 155, 173, 183 ), ( 22, 15, 200, 20 ) )
        pygame.draw.rect( self.surf, ( 217, 87, 99 ), ( 22, 15, self.data[ 'heart' ], 20 ) )
        pygame.draw.rect( self.surf, ( 127, 50, 50 ), ( 22, 15, 200, 20 ), 4 )
        self.surf.blit( self.sprites[ 'heart' ], ( 10, 10 ) )
    
    def mana( self ):
        pygame.draw.rect( self.surf, ( 155, 173, 183 ), ( 262, 15, 200, 20 ) )
        pygame.draw.rect( self.surf, ( 99, 155, 255 ), ( 262, 15, self.data[ 'mana' ], 20 ) )
        pygame.draw.rect( self.surf, ( 63, 63, 113 ), ( 262, 15, 200, 20 ), 4 )
        self.surf.blit( self.sprites[ 'mana' ], ( 250, 10 ) )

    def attacks( self ):
        if pad[ 'button' ][ 'a' ] or self.selectedAttac == 'a' :
            pygame.draw.circle( self.surf, ( 55, 148, 110 ), ( self.surf.get_width() - 70 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 40 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'green-unlock' if self.data[ 'a' ] else 'green-lock' ], ( self.surf.get_width() - 70, self.surf.get_height() - 40 ) )
        if pad[ 'button' ][ 'x' ] or self.selectedAttac == 'x' :
            pygame.draw.circle( self.surf, ( 91, 110, 255 ), ( self.surf.get_width() - 100 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 70 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'blue-unlock' if self.data[ 'x' ] else 'blue-lock' ], ( self.surf.get_width() - 100, self.surf.get_height() - 70 ) )
        if pad[ 'button' ][ 'b' ] or self.selectedAttac == 'b' :
            pygame.draw.circle( self.surf, ( 172, 50, 50 ), ( self.surf.get_width() - 40 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 70 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'red-lock' ], ( self.surf.get_width() - 40, self.surf.get_height() - 70 ) )
        if pad[ 'button' ][ 'y' ] or self.selectedAttac == 'y' :
            pygame.draw.circle( self.surf, ( 251, 242, 54 ), ( self.surf.get_width() - 70 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 100 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'yellow-lock' ], ( self.surf.get_width() - 70, self.surf.get_height() - 100 ) )