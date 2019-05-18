import random
import utils 

PLANETS_PATH = 'planets.json'
SYSTEMS_PATH = 'systems.json'
ANOMALIES_PATH = 'anomalies.json'

def parse_planet_data(planet_data):
    name, (resource, influence), planet_type, planet_tech = planet_data
    return name, resource, influence, planet_type, planet_tech

def get_planet(planet_name):
    return next((planet for planet in PLANETS if planet.name == planet_name), None)
    
class Planet:
    def __init__(self, planet_data):
        self.name, self.resource, self.influence, self.planet_type, self.planet_tech = parse_planet_data(planet_data)
    
class Anomaly(Planet):
    def __init__(self, planet_data):
        self.name, self.resource, self.influence, self.planet_type, self.planet_tech = planet_data, None, None, None, None

class System:
    def __init__(self, planet_names=None, home_planets=None):
        if planet_names:
            self.planets = [get_planet(planet_name) for planet_name in planet_names]
        elif home_planets:
            self.planets = [planet for planet in home_planets]
        else:
            self.planets = None

    def __repr__(self):
        if self.planets is not None:
            return ''.join([planet.name for planet in self.planets])
        return 'OUT OF BOUNDS'
        

PLANETS = [Planet(planet_data) for planet_data in utils.get_data_file(PLANETS_PATH)]
ANOMALIES = [Anomaly(anomaly_name) for anomaly_name in utils.get_data_file(ANOMALIES_PATH)]
SYSTEMS = [System(planet_names) for planet_names in utils.get_data_file(SYSTEMS_PATH)]

random.shuffle(PLANETS)
random.shuffle(ANOMALIES)
random.shuffle(SYSTEMS)


if __name__ == '__main__':
    print('Systems:', len(SYSTEMS))
    print('Anomalies:', len(ANOMALIES))
    for planet in PLANETS:
        if (planet.planet_type, planet.planet_tech) == (None, None):
            print(planet.name, planet.planet_type, planet.planet_tech)
    
