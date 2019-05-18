import random
from player import Player
import race
import planet

BOARD_SIZE = 7

class SundownEmpire:
    def __init__(self, number_of_players):
        # Planets and system
        self.planets = planet.PLANETS
        self.systems = planet.SYSTEMS
        self.anomalies = planet.ANOMALIES
        
        # Races
        self.races = race.RACES

        # Init Players
        self.players = [Player(self.races[i]) for i in range(number_of_players)]
        
        # game board
        self.board = []

        self.build_galaxy(number_of_players)
    
    def build_galaxy(self, number_of_players):
        self.build_board(number_of_players)

    def build_board(self, number_of_players):
        if number_of_players == 4:
            starting_positions = [(1, 0), (1, 4), (5, 0), (5, 4)]
            number_of_anomalies = 2
            number_of_systems = 5
        elif number_of_players == 5:
            starting_positions = [(0, 0), (3, 6), (1, 0), (5, 0), (6, 3)]
            number_of_anomalies = 2
            number_of_systems = 4
        elif number_of_players == 6:
            starting_positions= [(0, 0), (0, 3), (3, 0), (3, 6), (6, 0), (6, 3)]
            number_of_anomalies = 2
            number_of_systems = 3

        random.shuffle(starting_positions)

        # slice for amount of players
        self.anomalies = self.anomalies[:number_of_players * number_of_anomalies]
        self.systems = self.planets[:number_of_players * number_of_systems]

        # deal for each player
        dealt_anomalies = [self.anomalies[i:i+number_of_anomalies] for i in range(0, len(self.anomalies), number_of_anomalies)]
        dealt_systems = [self.systems[i:i+number_of_systems] for i in range(0, len(self.anomalies), number_of_systems)]
        
        # init empty board
        row_lengths = [4, 5, 6, 7, 6, 5, 4]
        self.game_board = [Hex(i, j) for i in range(7) for j in range(row_lengths[i])]        

        # init home systems and their hexes
        starting_systems = [planet.System(planet_names=None, home_planets=player.planets) for player in self.players]
        starting_hexes = [Hex(*position, system) for position, system in zip(starting_positions, starting_systems)]

        # replace corners with players
        for position in starting_positions:
            self.game_board.remove(self.get_hex(*position))
            self.game_board.append(next((hex for hex in starting_hexes if (hex.i, hex.j) == position), None))

        # replace middle with mecatol
        mecatol = Hex(3, 3, planet.System(['Mecatol-Rex']))
        self.game_board.remove(self.get_hex(3, 3))
        self.game_board.append(mecatol)      
        
        # link up hexes
        for i in range(BOARD_SIZE):
            for j in range(row_lengths[i]):
                hex = self.get_hex(i, j)
                hex.up = self.get_hex(i+1, j)
                hex.down = self.get_hex(i-1, j)
                hex.leftup = self.get_hex(i, j-1)
                hex.rightdown = self.get_hex(i, j+1)
                hex.rightup = self.get_hex(i+1, j+1)
                hex.leftdown = self.get_hex(i-1, j-1)

    def get_hex(self, i, j):
        # System without planets (not empty space) to represent out of bounds
        out_of_bounds = Hex(None, None, planet.System())
        return next((hex for hex in self.game_board if (hex.i, hex.j) == (i, j)), out_of_bounds)

class Hex:
    def __init__(self, i, j, system=None):
        self.system = system
        self.i, self.j = i, j
        
        # neighbors
        self.up, self.down, self.leftup, self.rightup, self.leftdown, self.rightdown = [None]*6

    def __repr__(self):
        size = 25
        filler = ' '*size
        up = filler + f'{self.up.system}\n'
        leftup = f'{self.leftup.system}'.ljust(size)
        rightup = f'{self.rightup.system}\n\n'.rjust(size)
        middle = filler + f'{self.system}\n'
        leftdown = f'{self.leftdown.system}'.ljust(size)
        rightdown = f'{self.rightdown.system}\n\n'.rjust(size)
        down = filler + f'{self.down.system}\n'
        return up + leftup + rightup + middle + leftdown + rightdown + down

if __name__ == "__main__":
    SundownEmpire(4)