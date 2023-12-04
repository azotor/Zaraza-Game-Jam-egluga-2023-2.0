from App.States.State import State
from App.Cooldown import Cooldown
from App.Events import pad

import pygame, sys

class MenuState( State ):
    def __init__( self ):
        super().__init__( 'MenuState' )
        self.options = [ 'START', 'OPTIONS', 'EXIT' ]
        self.currentOption = 0
        self.cooldown = Cooldown()
        self.surf = pygame.display.get_surface()
        self.viruses = []
    
    def start( self ):
        self.currentOption = 0

    def update( self, change ):
        self.cooldown.update()
        if not self.cooldown.run:
            if pad[ 'axis' ][ 'l' ][ 'y' ] < -.3:
                self.cooldown.start( 200 )
                self.currentOption -= 1
                if self.currentOption < 0:
                    self.currentOption = len( self.options ) - 1
            elif pad[ 'axis' ][ 'l' ][ 'y' ] > .3:
                self.cooldown.start( 200)
                self.currentOption += 1
                if self.currentOption >= len( self.options ):
                    self.currentOption = 0
        
        if pad[ 'button' ][ 'a' ]:
            match self.currentOption:
                case 0:
                    change( 'play' )
                case 1:
                    pass
                case 2:
                    pygame.quit()
                    sys.exit()

    def render( self ):
        titleFont = pygame.font.SysFont( "Tahoma", 32 )
        title = titleFont.render( "VirusDangeon", False, ( 172, 50, 50 ) )
        titleRect = title.get_rect( midright = ( self.surf.get_width() - 45, self.surf.get_height() / 2 ) )
        self.surf.blit( title, titleRect )

        optionFont = pygame.font.SysFont( "ArialBold", 24 )
        offsetX = self.surf.get_width() - 35
        offsetY = self.surf.get_height() / 2 + 50
        op = 0
        for opt in self.options:
            option = optionFont.render( opt, False, ( 55, 148, 110 ) )
            optionRect = option.get_rect( midright = ( offsetX, offsetY ) )
            self.surf.blit( option, optionRect )
            if op == self.currentOption:
                pygame.draw.line( self.surf, ( 153, 229, 80 ), ( self.surf.get_width() / 3 * 2, offsetY + 10 ), ( self.surf.get_width() - 20, offsetY + 10 ) )
            offsetY += 40
            op += 1
