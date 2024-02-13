from dataclasses import dataclass
from enum import Enum


class Rover:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def accept(self, commande):
        match commande:
            case "f":
                self.position = self.position.translate(CardinalVector.NORD)
            case "b":
                self.position = self.position.translate(CardinalVector.SUD)
            case _:
                pass


@dataclass(frozen=True)
class Vecteur:
    x: int
    y: int


class CardinalVector(Enum):
    NORD = Vecteur(0, 1)
    SUD = Vecteur(0, -1)
    EST = Vecteur(1, 0)
    OUEST = Vecteur(-1, 0)


@dataclass(frozen=True)
class Coordonnees:
    x: int
    y: int

    def translate(self, cardinal_vector):
        # Cool code
        return Coordonnees(
            self.x + cardinal_vector.value.x, self.y + cardinal_vector.value.y
        )
