from App.States.State import State
from App.Cooldown import Cooldown
from App.Controls import controls
from App.Config import FONT_TITLE

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
            if controls.d_pad_y < 0 or controls.axis_l_y < -.15:
                self.cooldown.start( 200 )
                self.currentOption -= 1
                if self.currentOption < 0:
                    self.currentOption = len( self.options ) - 1
            elif controls.d_pad_y > 0 or controls.axis_l_y > .15:
                self.cooldown.start( 200)
                self.currentOption += 1
                if self.currentOption >= len( self.options ):
                    self.currentOption = 0
        
        if controls.confirm:
            match self.currentOption:
                case 0:
                    change( 'play' )
                case 1:
                    pass
                case 2:
                    pygame.quit()
                    sys.exit()

    def render( self ):
        title = FONT_TITLE.render( "VirusDungeon", False, ( 172, 50, 50 ) )
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
