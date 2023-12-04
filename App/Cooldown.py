import pygame

class Cooldown:
    def __init__( self ):
        self.run = False
        self.now = 0
        self.end = 0
    
    def start( self, time ):
        self.now = pygame.time.get_ticks()
        self.end = self.now + time
        self.run = True
    
    def stop( self ):
        self.run = False
        self.now = 0
        self.end = 0

    def update( self ):
        if self.run:
            self.now = pygame.time.get_ticks()
            if self.now >= self.end:
                self.stop()