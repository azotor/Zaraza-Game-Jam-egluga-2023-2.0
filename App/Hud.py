import pygame

from App.Config import SCALE
from App.Controls import controls
from App.Cooldown import Cooldown

class Hud:
    def __init__( self ):
        self.surf = pygame.display.get_surface()
        self.image = pygame.image.load( 'Assets/hud.png' ).convert_alpha()
        self.gridSize = 16
        self.gridX = self.image.get_width() / self.gridSize
        self.gridY = self.image.get_height() / self.gridSize
        self.sprites = {}
        self.currentControls = controls.type
        self.changeControls = False
        self.changeControlsState = 0
        self.changeControlsY = 0
        self.changeControlsCooldown = Cooldown()
        self.data = {
            'heart' : 100,
            'mana' : 100,
            'action1' : 1,
            'action2' : 1,
            'action3' : 0,
            'action4' : 0
        }
        self.selectedAttac = 'action1'
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
        if self.currentControls != controls.type:
            self.currentControls = controls.type
            self.changeControlsState = 0
            self.changeControlsY = 0
            self.changeControls = True

    def render( self ):
        self.hearts()
        self.mana()
        self.attacks()
        self.controlsSwitch()
    
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
        if controls.action1 or self.selectedAttac == 'action1' :
            pygame.draw.circle( self.surf, ( 55, 148, 110 ), ( self.surf.get_width() - 70 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 40 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'green-unlock' if self.data[ 'action1' ] else 'green-lock' ], ( self.surf.get_width() - 70, self.surf.get_height() - 40 ) )
        if controls.action2 or self.selectedAttac == 'action2' :
            pygame.draw.circle( self.surf, ( 172, 50, 50 ), ( self.surf.get_width() - 40 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 70 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'red-lock' if self.data[ 'action2' ] else 'red-lock' ], ( self.surf.get_width() - 40, self.surf.get_height() - 70 ) )
        if controls.action3 or self.selectedAttac == 'action3' :
            pygame.draw.circle( self.surf, ( 91, 110, 255 ), ( self.surf.get_width() - 100 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 70 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'blue-unlock' if self.data[ 'action3' ] else 'blue-lock' ], ( self.surf.get_width() - 100, self.surf.get_height() - 70 ) )
        if controls.action4 or self.selectedAttac == 'action4' :
            pygame.draw.circle( self.surf, ( 251, 242, 54 ), ( self.surf.get_width() - 70 + ( self.gridSize  * SCALE ) / 2, self.surf.get_height() - 100 + ( self.gridSize  * SCALE ) / 2 ), 20 )
        self.surf.blit( self.sprites[ 'yellow-lock' if self.data[ 'action4' ] else 'yellow-lock' ], ( self.surf.get_width() - 70, self.surf.get_height() - 100 ) )

    def controlsSwitch( self ):
        if self.changeControls:
            match self.changeControlsState:
                case 0 :
                    self.changeControlsY += 1
                    if self.changeControlsY >= 50:
                        self.changeControlsState = 1
                case 1 :
                    if not self.changeControlsCooldown.run:
                        self.changeControlsCooldown.start( 2000 )
                    else:
                        self.changeControlsCooldown.update()
                        if not self.changeControlsCooldown.run:
                            self.changeControlsState = 2
                case 2 :
                    self.changeControlsY -= 1
                    if self.changeControlsY <= 0:
                        self.changeControlsState = 0
                        self.changeControls = False
                
            
            rect = pygame.Surface( ( 100, 50 ), pygame.DOUBLEBUF ).convert_alpha()
            rect.fill( ( 0, 0, 0, 100 ) )
            pygame.draw.rect( rect, ( 255, 255, 255 ), ( 25, 15, 50, 20 ) )

            self.surf.blit( rect, ( 10, self.surf.get_width() - self.changeControlsY ) )