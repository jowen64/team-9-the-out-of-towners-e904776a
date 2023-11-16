from levelup.position import Position
from levelup.direction import Direction
from levelup.map import Map

DEFAULT_CHARACTER_NAME = "Character"
class Character:
    name = ""
    current_position :Position = Position(-100,-100)
    map :Map = Map()

    def __init__(self, character_name=DEFAULT_CHARACTER_NAME):
        if character_name.strip() == '':
            self.name = DEFAULT_CHARACTER_NAME
        else:
            self.name = character_name

    def move(self, direction :Direction) -> None:
        self.current_position = self.map.calculate_new_position(
            self.current_position, direction)

    def enter_map(self, map :Map) -> None:
        self.map = map
        self.current_position = self.map.starting_position
