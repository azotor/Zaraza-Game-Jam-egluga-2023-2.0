import pygame
from App.Controls import controls

pad = {
    'init' : False,
    'focus' : False,
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

keys = {
    'focus' : True,
    'up' : False,
    'right' : False,
    'down' : False,
    'left' : False,
    'action1' : False,
    'action2' : False,
    'action3' : False,
    'action4' : False,
    'return' : False,
    'tab' : False
}

class Events:
    
    quit = False
    pad = None

    def __init__( self ):
        pass

    def update( self ):
        self.updateKeys()
        self.updateController()
        self.setControls()

    def updateKeys( self ):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                self.quit = True
            
            if event.type == pygame.KEYDOWN:
                if not keys[ 'focus' ]:
                    keys[ 'focus' ] = True
                    pad[ 'focus' ] = False
                    controls.type = 'keys'

                match event.key:
                    case pygame.K_UP:
                        keys[ 'up' ] = True
                    case pygame.K_RIGHT:
                        keys[ 'right' ] = True
                    case pygame.K_DOWN:
                        keys[ 'down' ] = True
                    case pygame.K_LEFT:
                        keys[ 'left' ] = True
                    case pygame.K_1:
                        keys[ 'action1' ] = True
                    case pygame.K_2:
                        keys[ 'action2' ] = True
                    case pygame.K_3:
                        keys[ 'action3' ] = True
                    case pygame.K_4:
                        keys[ 'action4' ] = True
                    case pygame.K_RETURN:
                        keys[ 'return' ] = True
                    case pygame.K_TAB:
                        keys[ 'tab' ] = True

            if event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_UP:
                        keys[ 'up' ] = False
                    case pygame.K_RIGHT:
                        keys[ 'right' ] = False
                    case pygame.K_DOWN:
                        keys[ 'down' ] = False
                    case pygame.K_LEFT:
                        keys[ 'left' ] = False
                    case pygame.K_1:
                        keys[ 'action1' ] = False
                    case pygame.K_2:
                        keys[ 'action2' ] = False
                    case pygame.K_3:
                        keys[ 'action3' ] = False
                    case pygame.K_4:
                        keys[ 'action4' ] = False
                    case pygame.K_RETURN:
                        keys[ 'return' ] = False
                    case pygame.K_TAB:
                        keys[ 'tab' ] = False

    def updateController( self ):
        if not pad[ 'init' ] and pygame.joystick.get_count() :
            self.controller = pygame.joystick.Joystick( 0 )
            self.controller.init()
            pad[ 'init' ] = True
        
        if pad[ 'init' ]:
            i = 0
            for key in pad[ 'button' ]:
                    
                pad[ 'button' ][ key ] = self.controller.get_button( i )

                if self.controller.get_button( i ) and not pad[ 'focus' ]:
                    pad[ 'focus' ] = True
                    keys[ 'focus' ] = False
                    controls.type = 'pad'

                i += 1
            
            if self.controller.get_numaxes:

                pad[ 'axis' ][ 'l' ] = { 'x' : self.controller.get_axis( 0 ), 'y' : self.controller.get_axis( 1 ) }
                pad[ 'axis' ][ 'r' ] = { 'x' : self.controller.get_axis( 2 ), 'y' : self.controller.get_axis( 3 ) }
                pad[ 'axis' ][ 'lt' ] = self.controller.get_axis( 4 )
                pad[ 'axis' ][ 'rt' ] = self.controller.get_axis( 5 )

            if self.controller.get_numhats:
                dpad = self.controller.get_hat( 0 )
                pad[ 'dpad' ] = { 'x' : -dpad[ 0 ], 'y' : dpad[ 1 ] }

            if(
                not pad[ 'focus' ] and (
                    self.controller.get_axis( 0 ) >.151 or self.controller.get_axis( 0 ) < -.15 or
                    self.controller.get_axis( 1 ) >.151 or self.controller.get_axis( 1 ) < -.15 or
                    self.controller.get_axis( 2 ) >.151 or self.controller.get_axis( 2 ) < -.15 or
                    self.controller.get_axis( 3 ) >.151 or self.controller.get_axis( 3 ) < -.15 or
                    self.controller.get_axis( 4 ) > -1 or self.controller.get_axis( 5 ) > -1 or
                    self.controller.get_hat( 0 )[ 0 ] != 0 or self.controller.get_hat( 0 )[ 1 ] != 0
                )
            ):
                pad[ 'focus' ] = True
                keys[ 'focus' ] = False
                controls.type = 'pad'

    def setControls( self ):
        if keys[ 'focus' ]:
            if keys[ 'up' ]:
                controls.d_pad_y = -1
            elif keys[ 'down' ]:
                controls.d_pad_y = 1
            else:
                controls.d_pad_y = 0
        
            if keys[ 'left' ]:
                controls.d_pad_x = -1
            elif keys[ 'right' ]:
                controls.d_pad_x = 1
            else:
                controls.d_pad_x = 0
            
            
            controls.confirm = keys[ 'return' ]
            controls.action1 = keys[ 'action1' ]
            controls.action2 = keys[ 'action2' ]
            controls.action3 = keys[ 'action3' ]
            controls.action4 = keys[ 'action4' ]
            controls.map = keys[ 'tab' ]

        elif pad[ 'focus' ]:
            controls.d_pad_x = -pad[ 'dpad' ][ 'x' ]
            controls.d_pad_y = -pad[ 'dpad' ][ 'y' ]
            controls.axis_l_x = pad[ 'axis' ][ 'l' ][ 'x' ]
            controls.axis_l_y = pad[ 'axis' ][ 'l' ][ 'y' ]
            controls.axis_r_x = pad[ 'axis' ][ 'r' ][ 'x' ]
            controls.axis_r_x = pad[ 'axis' ][ 'r' ][ 'y' ]
            controls.confirm = controls.action1 = True if pad[ 'button' ][ 'a' ] else False
            controls.action2 = True if pad[ 'button' ][ 'b' ] else False
            controls.action3 = True if pad[ 'button' ][ 'x' ] else False
            controls.action4 = True if pad[ 'button' ][ 'y' ] else False
            controls.map = True if pad[ 'button' ][ 'share' ] else False