from dataclasses import dataclass

from homeostasis.common import PersonalityMatrix, Stats
from homeostasis.items.food import FoodItem
from homeostasis.items.play import PLAY_ITEMS, PlayItem


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


    def eat(self, food: FoodItem):
        """Feed the pet a food item, adjusting stats based on food properties."""
        stats = food.eat(self.personality)
        self.stats.add_stats(stats)

    def play(self, play_item: PlayItem):
        """Let the pet play with a play item, adjusting stats based on play item properties."""
        stats = play_item.play(self.personality)
        self.stats.add_stats(stats)

    def sleep(self):
        """Let the pet sleep, restoring energy."""
        self.stats.energy += 20
        self.stats.clamp_stats()

if __name__ == "__main__":
    pet = Pet(
        info=PetSpec(name="Buddy", age=3, style="Casual"),
        personality=PersonalityMatrix(friendliness=5, playfulness=5, laziness=5, curiosity=5),
        stats=Stats(
            happiness=50,
            energy=50,
            social=50,
            hunger=50,
            health=50,
        ),
    )

    from homeostasis.items.food import FOOD_ITEMS

    for food in FOOD_ITEMS.values():
        print(f"Feeding {pet.info.name} a {food.name}")
        pet.eat(food)
        print(f"New stats: {pet.stats}")
    print("-----")
    for toy in PLAY_ITEMS.values():
        print(f"Playing with {pet.info.name} using {toy.name}")
        pet.play(toy)
        print(f"New stats: {pet.stats}")