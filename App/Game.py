import pygame, sys
from App.Events import Events, pad
from App.Config import SCALE
from App.StatesManager import StatesManager

class Game:
    def __init__( self ):
        pygame.init()
        self.screen = pygame.display.set_mode( ( 32 * 11 * SCALE, 32 * 11 * SCALE ), pygame.DOUBLEBUF )
        pygame.display.set_caption( "ZARAZA" )

        self.events = Events()

        self.statesManager = StatesManager()
        
        self.run = True
        self.loop()


    def loop( self ):
        while self.run:
            self.events.update()
            if self.events.quit:
                self.run = False

            self.update()
            self.render()
        
        pygame.quit()
        sys.exit()


    def update( self ):
        self.statesManager.update()

    def render( self ):
        self.screen.fill( ( 34, 32, 52) )
        self.statesManager.render()
        pygame.display.update()