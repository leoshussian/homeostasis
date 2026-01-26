from dataclasses import dataclass, field
from enum import Enum

from homeostasis.common import PersonalityMatrix


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

class Item:
    """Base class for all items in the game."""
    def __init__(self, *, name: str, description: str, personality: PersonalityMatrix, max_durability: int) -> None:
        self.name: str = name
        self.description: str = description
        self.personality: PersonalityMatrix = personality
        self.max_durability: int = max_durability
        self.max_durability: int = max_durability

    def is_usable(self) -> bool:
        """Check if the item is still usable."""
        return self.max_durability > 0

    def use(self) -> ItemStatus:
        """Use the item, reducing its durability."""
        if not self.is_usable():
            raise ValueError(f"Item '{self.name}' is not usable.")

        if self.max_durability > 0:
            self.max_durability -= 1
        self.max_durability = max(0, self.max_durability)

        return ItemStatus.get_status(self.max_durability, self.max_durability)

    def get(self) -> "Item":
        """Get a copy of the item."""
        return Item(
            name=self.name,
            description=self.description,
            personality=self.personality,
            max_durability=self.max_durability,
        )