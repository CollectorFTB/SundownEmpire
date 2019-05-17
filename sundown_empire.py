import player
import race
import planet

class SundownEmpire:
    def __init__(self, number_of_players):
        # Planets and system
        self.planets = planet.PLANETS
        self.systems = planet.SYSTEMS

        # Races
        self.races = race.RACES

        # Init Players
        self.players = [player.Player(self.races[i]) for i in range(number_of_players)]
        
        # self.public_objectives = 
        # self.secret_objectives = 