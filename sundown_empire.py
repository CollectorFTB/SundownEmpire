import player
import race
import planet

class SundownEmpire:
    def __init__(self, number_of_players):
        # Planets and system
        self.planets = planet.PLANETS
        self.systems = planet.SYSTEMS
        self.anomalies = planet.ANOMALIES
        
        # Races
        self.races = race.RACES

        # Init Players
        self.players = [player.Player(self.races[i]) for i in range(number_of_players)]
        
        if number_of_players == 4:
            pass
        elif number_of_players == 5:
            pass
        elif number_of_players == 6:
            pass

if __name__ == "__main__":
    SundownEmpire(4)