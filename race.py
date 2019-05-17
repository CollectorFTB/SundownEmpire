# TODO: implement flagship
# TODO: implement race special effects
# TODO: implement race special starting unit techs

import random
import json
import utils
import planet

RACES_PATH = 'races.json'

def parse_race_data(race_data):
    name, starting_values = race_data
    
    technologies = starting_values['technologies']
    units = starting_values['units']
    home_planets = starting_values['home planets']
    commodities = starting_values['commodities']

    return name, technologies, units, home_planets, commodities

def print_race_data(race):
    print('Race name:\n\t', race.name)
    print('Techs:\n\t', ', '.join(race.technologies))
    print('Starting planets:\n\t', '\n\t '.join(race.home_planets))
    print('Units:', )
    for unit in race.units:
        print('\t', unit, ':',race.units[unit])
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

class Race:
    def __init__(self, race_data):
        self.name, self.technologies, self.units, planet_names, self.commodities = parse_race_data(race_data)
        self.home_planets = [planet.get_planet(planet_name) for planet_name in planet_names]


RACES = [Race(race_info) for race_info in utils.get_data_file(RACES_PATH).items()]
random.shuffle(RACES)