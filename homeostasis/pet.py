from dataclasses import dataclass

from homeostasis.common import PersonalityMatrix, Stats
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


class Pet:
    def __init__(self, info: PetSpec, personality: PersonalityMatrix, stats: Stats) -> None:
        self.info: PetSpec = info
        self.stats: Stats = stats
        self.personality: PersonalityMatrix = personality

    def sleep(self):
        """Let the pet sleep, restoring energy."""
        self.stats.energy += 20
        self.stats.clamp_stats()

    def use(self, item: ItemInstance):
        """Use a generic item on the pet, adjusting stats based on item properties."""
        stats = item.definition.effect(self.personality)
        self.stats.add_stats(stats)
        item.use(1)

if __name__ == "__main__":
    pet = Pet(
        info=PetSpec(name="Buddy", age=3, style="Casual"),
        personality=PersonalityMatrix(friendliness=5, playfulness=3, laziness=10, curiosity=7),
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
        pet.use(item_instance)
        print(f"After using {food_item.name}, pet stats: {pet.stats}")

    print("=== Using Play Items ===")
    for play_item in PLAY_ITEMS:
        item_instance = play_item.spawn()
        pet.use(item_instance)
        print(f"After using {play_item.name}, pet stats: {pet.stats}")