from enum import Enum, auto
from dataclasses import dataclass

class Manufactuer(Enum):
    kona = auto()
    privateer = auto()
    specialized = auto()

class Sram(Enum):
    none = 0
    sx = auto()
    nx = auto()
    gx = auto()
    x01 = auto()
    xx1 = auto()

class Shimano(Enum):
    none = 0
    deore = auto()
    slx = auto()
    xt = auto()

class Fox(Enum):
    pass

class Rockshoks(Enum):
    pass

class Wheel(Enum):
    w29 = auto()



@dataclass
class Bike:
    model: str
    sram: Sram
    shimano: Shimano
    wheels: int
    manufactuer: Manufactuer
    price: float

    def groupset(self):
        if self.shimano != Shimano.none:
            return self.shimano
        return self.sram
    def model_name(self):
        return self.model

    def __post_init__(self):
        self.price /=2000

    def __sub__(self, other):
        if self.shimano == other.shimano and self.sram == other.sram:
            return None
        if self.sram.value > other.sram.value and self.shimano == other.shimano:
            return self.sram
        elif self.shimano.value > other.shimano.value and self.sram == other.sram:
            return self.shimano
        return (self.groupset(), other.groupset())

