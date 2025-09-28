from enum import Enum

class LOCATION_TYPE(Enum):
    PORT = 'PORT'
    FOREST = 'FOREST'
    TUNDRA = 'TUNDRA'


class Location():

    def __init__(self, name: str, population: int, location_type: LOCATION_TYPE):
        self.name = name
        self.population = population
        self.location_type = location_type

    