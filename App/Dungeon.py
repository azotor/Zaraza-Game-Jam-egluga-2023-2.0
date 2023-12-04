from App.Room import Room
from App.DungeonSprites import DungeonSprites
from App.Events import pad
from App.Cooldown import Cooldown

import random, pygame

class Dungeon:
    rooms = []

    def __init__( self, main, second ):
        self.main = main
        self.second = second
        self.surf = pygame.display.get_surface()
        self.sprites = DungeonSprites()
        self.generateMain()
        self.generateSecond()
        self.minimap = False
        self.minimapCooldown = Cooldown()

    def generateMain( self ):
        lastPos = pygame.math.Vector2( 0, 0 )
        self.rooms.append( Room( lastPos, self.sprites ) )
        lastRoom = self.getRoom( lastPos )
        ( d, dir ) = self.getNewDir()
        i = 1
        while i < self.main:
            newPos = lastPos + dir
            if not self.roomExists( newPos ):
                lastRoom.doors[ d ] = 1
                self.rooms.append( Room( newPos, self.sprites ) )
                lastRoom = self.getRoom( newPos )
                lastRoom.doors[ self.getOpositeWall( d ) ] = 1
                lastPos = newPos
                i += 1

    def generateSecond( self ):
        i = 0
        while i < self.second:
            r = random.choice( self.rooms )
            if not r.hasAllDoors():
                ( d, dir ) = self.getNewDir()
                r.doors[ d ] = 1
                neighbor = r.pos + dir
                if not self.roomExists( neighbor ):
                    self.rooms.append( Room( neighbor, self.sprites ) )
                    i += 1
                neighborRoom = self.getRoom( neighbor )
                neighborRoom.doors[ self.getOpositeWall( d ) ] = 1

    def roomExists( self, pos ):
        for room in self.rooms:
            if room.pos == pos:
                return True
        return False
    
    def getRoom( self, pos ):
        for room in self.rooms:
            if room.pos == pos:
                return room
        return False

    def drawMiniMap( self, player ):
        if self.minimap:
            bound = self.getRoomsBound()
            size = 18
            font = pygame.font.SysFont( 'Sans Serif', 32 )
            minisurf = pygame.Surface( ( int( ( bound[ 1 ] - bound[ 3 ] + 3 ) * size ), int( ( bound[ 2 ] - bound[ 0 ] + 3 ) * size ) ), pygame.DOUBLEBUF ).convert_alpha()
            minisurf.fill( ( 0, 0, 0, 200 ) )
            fill_color = pygame.Color( 69, 40, 60 )
            stroke_color = pygame.Color( 34, 32, 52 )
            for room in self.rooms:
                originX = size * ( room.pos[ 0 ] - bound[ 3 ] + 1 )
                originY = size * ( room.pos[ 1 ] - bound[ 0 ] + 1 )
                pygame.draw.rect( minisurf, fill_color, ( originX, originY, size, size ) )
                pygame.draw.rect( minisurf, stroke_color, ( originX, originY, size, size ), 1 )
                if room.doors[ 0 ] == 1:
                    pygame.draw.line( minisurf, fill_color, ( originX + size / 2 - size / 6, originY ), ( originX + size / 2 + size / 6, originY ), 1 )
                if room.doors[ 1 ] == 1:
                    pygame.draw.line( minisurf, fill_color, ( originX + size - 1, originY + size / 2 - size / 6 ), ( originX + size - 1, originY + size / 2 + size / 6 ), 1 )
                if room.doors[ 2 ] == 1:
                    pygame.draw.line( minisurf, fill_color, ( originX + size / 2 - size / 6, originY + size - 1 ), ( originX + size / 2 + size / 6, originY + size - 1 ), 1 )
                if room.doors[ 3 ] == 1:
                    pygame.draw.line( minisurf, fill_color, ( originX, originY + size / 2 - size / 6 ), ( originX, originY + size / 2 + size / 6 ), 1 )
                if room.pos == player:
                    pygame.draw.circle( minisurf, ( 152, 229, 80 ), ( originX + size / 2, originY + size / 2 ), size / 6 )
            text = font.render( "MAP", False, ( 255, 255, 255 ) )
            text_rect = text.get_rect( center = ( self.surf.get_width() / 2, ( self.surf.get_height() - minisurf.get_height() ) / 2 - size ) )
            self.surf.blit( text, text_rect )
            self.surf.blit( minisurf, ( ( self.surf.get_width() - minisurf.get_width() ) / 2, ( self.surf.get_height() - minisurf.get_height() ) / 2 ) )
    
    def getNewDir( self ):
        d = random.randint( 0, 3 )
        dir = [ 0, 0 ]
        match d:
            case 0 :
                dir = pygame.math.Vector2( 0, -1 )
            case 1 :
                dir = pygame.math.Vector2( 1, 0 )
            case 2 :
                dir = pygame.math.Vector2( 0, 1 )
            case 3 :
                dir = pygame.math.Vector2( -1, 0 )
        return ( d, dir )
    
    def getOpositeWall( self, d ):
        return ( d + 2 ) % 4
    
    def getRoomsBound( self ):
        bound = [ 0, 0, 0, 0 ]
        for room in self.rooms:
            if room.pos[ 1 ] < bound[ 0 ]:
                bound[ 0 ] = room.pos[ 1 ]
            if room.pos[ 0 ] > bound[ 1 ]:
                bound[ 1 ] = room.pos[ 0 ]
            if room.pos[ 1 ] > bound[ 2 ]:
                bound[ 2 ] = room.pos[ 1 ]
            if room.pos[ 0 ] < bound[ 3 ]:
                bound[ 3 ] = room.pos[ 0 ]
        return bound
    
    def renderRoom( self, pos ):
        if self.roomExists( pos ):
            room = self.getRoom( pos )
            room.render()

    def update( self ):
        self.toggleMiniMap()
        self.minimapCooldown.update()

    def toggleMiniMap( self ):
        if pad[ 'button' ][ 'share' ] and not self.minimapCooldown.run:
            self.minimap = not self.minimap
            self.minimapCooldown.start( 200 )