from dataclasses import dataclass, field
from enum import Enum

from homeostasis.common import PersonalityMatrix, Stats, StatsWeights


class ItemStatus(Enum):
    NEW = "new"
    USED = "used"
    CONSUMED = "consumed"

    def is_usable(self) -> bool:
        return self != ItemStatus.CONSUMED

    @staticmethod
    def get_status(durability: int, max_durability: int) -> 'ItemStatus':
        if durability <= 0:
            return ItemStatus.CONSUMED
        elif durability < max_durability:
            return ItemStatus.USED
        else:
            return ItemStatus.NEW

@dataclass(frozen=True)
class ItemDefinition:
    """Definition of an item type.

    Attributes:
        name (str): The name of the item.
        description (str): A brief description of the item.
        max_durability (int): The maximum durability of the item.
        personality (PersonalityMatrix): The personality traits associated with the item.
        effects (Stats): The stat effects the item has when used. For example, food items may increase hunger and health.
        effect_weights (StatsWeights): The weights applied to the effects.
            For example, a Food subclass could primarily affect hunger and health, and affect other stats less.
            This allows for someone adding an item to set `effects` based on other items of the same type instead of all items.
        tags (frozenset[str]): What the item is. "edible", "playable", etc.
    """
    name: str
    description: str
    max_durability: int
    personality: PersonalityMatrix
    effects: Stats
    effect_weights: StatsWeights = field(default_factory=StatsWeights)
    tags: frozenset[str] = field(default_factory=frozenset)

    def effect(self, pet_personality: PersonalityMatrix) -> Stats:
        """Calculate the effect of the item based on pet's personality.

        Args:
            pet_personality (PersonalityMatrix): The personality matrix of the pet.
        """
        compatibility = PersonalityMatrix.get_compatibility(self.personality, pet_personality)
        # Apply effect weights scaled by compatibility
        weighted_effects = self.effect_weights.apply(self.effects, scale=compatibility)
        return weighted_effects

    def spawn(self) -> 'ItemInstance':
        """Create a new instance of the item."""
        return ItemInstance(definition=self)

@dataclass
class ItemInstance:
    definition: ItemDefinition
    durability: int = field(init=False)

    def __post_init__(self):
        self.durability = self.definition.max_durability

    def is_usable(self) -> bool:
        """Check if the item instance is still usable."""
        return self.durability > 0

    def use(self, amount: int = 1) -> ItemStatus:
        """Use the item instance, reducing its durability.

        Args:
            amount (int): The amount to reduce durability by.
        """
        for _ in range(amount):
            if not self.is_usable():
                raise ValueError(f"Item '{self.definition.name}' is not usable.")

            self.durability -= 1

        return self.status

    @property
    def status(self) -> ItemStatus:
        """Get the current status of the item instance."""
        return ItemStatus.get_status(self.durability, self.definition.max_durability)

ITEMS = {}
def register_item(item: ItemDefinition):
    """Registers an item in the global items list."""
    ITEMS[item.name] = item
