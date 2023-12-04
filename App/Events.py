import pygame

pad = {
    'init' : False,
    'button' : {
        'a' : 0,
        'b' : 0,
        'x' : 0,
        'y' : 0,
        'lb' : 0,
        'rb' : 0,
        'share' : 0,
        'option' : 0,
        'l' : 0,
        'p' : 0
    },
    'axis' : {
        'l' : {
            'x' : 0,
            'y' : 0
        },
        'r' : {
            'x' : 0,
            'y' : 0
        },
        'lt' : 0,
        'rt' : 0
    },
    'dpad' : {
        'x' : 0,
        'y' : 0
    }
}

class Events:
    
    quit = False
    pad = None

    def __init__( self ):
        if pygame.joystick.get_count() :
            self.controller = pygame.joystick.Joystick( 0 )
            self.controller.init()
            pad[ 'init' ] = True


    def update( self ):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True
        
        if pad[ 'init' ]:
            i = 0
            for key in pad[ 'button' ]:
                pad[ 'button' ][ key ] = self.controller.get_button( i )
                i += 1
            
            pad[ 'axis' ][ 'l' ] = { 'x': self.controller.get_axis( 0 ), 'y' : self.controller.get_axis( 1 ) }
            pad[ 'axis' ][ 'r' ] = { 'x': self.controller.get_axis( 2 ), 'y' : self.controller.get_axis( 3 ) }
            pad[ 'axis' ][ 'lt' ] = self.controller.get_axis( 4 )
            pad[ 'axis' ][ 'rt' ] = self.controller.get_axis( 5 )

            dpad = self.controller.get_hat( 0 )
            pad[ 'dpad' ] = { 'x' : dpad[ 0 ], 'y' : dpad[ 1 ] }

                