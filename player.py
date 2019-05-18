MAX_CONTROL_TOKENS = 17
MAX_COMMAND_TOKENS = 16

class Player:
    def __init__(self, starting_race):
        self._starting_race = starting_race
        
        self.technologies = starting_race.technologies
        self.units = starting_race.units
        self.planets = starting_race.home_planets
        
        self.commodities = starting_race.commodities
        self.trade_goods = 0
        self.tactic_tokens = 3
        self.fleet_tokens = 3
        self.strategy_tokens = 2
        self.victory_points = 0