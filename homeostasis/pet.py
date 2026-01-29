from dataclasses import dataclass

from homeostasis.common import Traits, Motives


@dataclass
class PetSpec:
    name: str
    age: int
    style: str

@dataclass
class PetDecayRates:
    """Rates at which the pet's motives decay over time."""
    happiness_decay: int = 1
    energy_decay: int = 1
    social_decay: int = 1
    hunger_decay: int = 1

class BusyPetException(Exception):
    """The pet is currently busy with another action."""
    pass

class Pet:
    def __init__(self, info: PetSpec, personality: Traits, motives: Motives) -> None:
        self.info: PetSpec = info
        self.motives: Motives = motives
        self.personality: Traits = personality
        self.current_action = None

    @property
    def is_busy(self) -> bool:
        return self.current_action is not None

    def set_action(self, action) -> None:
        """Set the current action for the pet."""
        if self.is_busy:
            raise BusyPetException
        self.current_action = action

    def tick(self) -> None:
        """Advance the pet's current action by one tick."""
        if self.current_action is not None:
            self.current_action.tick(self)
            if self.current_action.is_complete():
                self.current_action = None


__all__ = ["Pet", "PetSpec", "PetDecayRates", "BusyPetException"]