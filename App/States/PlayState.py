from App.States.State import State
from App.Dungeon import Dungeon
from App.Player import Player
from App.Hud import Hud

class PlayState( State ):
    def __init__( self ):
        super().__init__( 'PlayState' )
        self.hud = Hud()
    
    def enter( self ):
        self.dungeon = Dungeon( 5, 20 )
        self.player = Player()

    def update( self, change ):
        self.dungeon.update()
        self.player.update()
        self.hud.update( { 'heart' : 100, 'mana' : 100, 'action1' : 1, 'action2' : 0, 'action3' : 1, 'action4' : 0 } )

    def render( self ):
        self.dungeon.renderRoom( ( 0, 0 ) )
        self.player.render()
        self.hud.render()
        self.dungeon.drawMiniMap( ( 0, 0 ) )
