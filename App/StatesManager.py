from App.States.MenuState import MenuState
from App.States.PlayState import PlayState

class StatesManager:
    def __init__( self ):
        self.states = {
            'menu' : MenuState(),
            'play' : PlayState()
        }
        self.change( 'menu' )

    def change( self, state ):
        self.currentStatre = self.states[ state ]
        self.currentStatre.enter()
    
    def update( self ):
        self.currentStatre.update( self.change )

    def render( self ):
        self.currentStatre.render()