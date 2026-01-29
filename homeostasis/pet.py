from dataclasses import dataclass
from time import sleep

from homeostasis.action import EatAction
from homeostasis.common import Traits, Stats
from homeostasis.items.base import ItemInstance
from homeostasis.items.food import register_food_items
from homeostasis.items.play import register_play_items


@dataclass
class PetSpec:
    name: str
    age: int
    style: str

@dataclass
class PetDecayRates:
    """Rates at which the pet's stats decay over time."""
    happiness_decay: int = 1
    energy_decay: int = 1
    social_decay: int = 1
    hunger_decay: int = 1

class BusyPetException(Exception):
    """The pet is currently busy with another action."""
    pass

class Pet:
    def __init__(self, info: PetSpec, personality: Traits, stats: Stats) -> None:
        self.info: PetSpec = info
        self.stats: Stats = stats
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

if __name__ == "__main__":
    pet = Pet(
        info=PetSpec(name="Buddy", age=3, style="Casual"),
        personality=Traits(friendliness=5, playfulness=3, laziness=10, curiosity=7),
        stats=Stats(
            happiness=50,
            energy=50,
            social=50,
            hunger=50,
            health=50,
            fun=50,
        ),
    )

    from homeostasis.items.base import ITEMS, ItemInstance
    register_food_items()
    register_play_items()

    FOOD_ITEMS = [item for item in ITEMS.values() if "edible" in item.tags]

    PLAY_ITEMS = [item for item in ITEMS.values() if "playable" in item.tags]

    print("Initial pet stats:", pet.stats)
    print("=== Using Food Items ===")
    for food_item in FOOD_ITEMS:
        item_instance = food_item.spawn()
        action = EatAction(item_instance)
        pet.set_action(action)
        while pet.is_busy:
            print(f"Feeding {food_item.name}...")
            pet.tick()
            sleep(2) # Simulate time passing
        print(f"After eating {food_item.name}, pet stats: {pet.stats}")