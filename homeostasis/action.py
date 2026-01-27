from __future__ import annotations
from typing import TYPE_CHECKING

from homeostasis.common import Stats
from homeostasis.items.base import ItemInstance

if TYPE_CHECKING:
    from homeostasis.pet import Pet

class ActionInterruptException(Exception):
    """The action was interrupted."""
    pass

class Action:
    def __init__(self, name: str, remaining_ticks: int) -> None:
        self.name = name
        self.remaining_ticks = remaining_ticks

    def tick(self, pet: Pet) -> None:
        """Advance the action by one tick."""
        if self.is_complete():
            return

        self.remaining_ticks -= 1
        self.on_tick(pet)

        if self.is_complete():
            self.on_complete(pet)

    def on_tick(self, pet: Pet) -> None:
        """Hook for performing effects on the pet each tick."""
        raise NotImplementedError()

    def on_complete(self, pet: Pet) -> None:
        """Hook for performing effects on the pet when the action is complete."""
        raise NotImplementedError()

    def interrupt(self, pet: Pet) -> None:
        """Interrupt the action."""
        raise ActionInterruptException(f"The action '{self.name}' was interrupted.")

    def is_complete(self) -> bool:
        """Check if the action is complete."""
        return self.remaining_ticks <= 0

class SleepAction(Action):
    MAX_SLEEP_TICKS = 100
    def __init__(self) -> None:
        super().__init__("sleep", self.MAX_SLEEP_TICKS)

    def on_tick(self, pet: Pet) -> None:
        """Increase energy stat each tick."""
        pet.stats.add_stats(Stats(energy=2))
        if pet.stats.energy >= 100:
            self.remaining_ticks = 0

    def on_complete(self, pet: Pet) -> None:
        pass

class PlayAction(Action):
    PLAY_TICKS = 2
    def __init__(self, play_item: ItemInstance) -> None:
        super().__init__("play", self.PLAY_TICKS)
        if "playable" not in play_item.definition.tags:
            raise ValueError("Item is not playable.")
        self.play_item = play_item

    def on_tick(self, pet: Pet) -> None:
        """Increase fun and social stats each tick."""
        # Decrease item durability
        try:
            self.play_item.use(1)
        except ValueError:
            raise ActionInterruptException(f"{self.play_item.definition.name} cannot be used as it has been consumed.")
        # Increase pet stats
        effects = self.play_item.definition.effect(pet.personality)
        pet.stats.add_stats(effects)

    def on_complete(self, pet: Pet) -> None:
        pass

class EatAction(Action):
    EAT_TICKS = 1
    def __init__(self, food_item: ItemInstance) -> None:
        super().__init__("eat", self.EAT_TICKS)
        if "edible" not in food_item.definition.tags:
            raise ValueError("Item is not edible.")
        self.food_item = food_item

    def on_tick(self, pet: Pet) -> None:
        """Increase hunger and health stats each tick."""
        # Decrease item quantity
        try:
            self.food_item.use(1)
        except ValueError:
            raise ActionInterruptException(f"{self.food_item.definition.name} cannot be used as it has been consumed.")
        # Increase pet stats
        effects = self.food_item.definition.effect(pet.personality)
        pet.stats.add_stats(effects)

    def on_complete(self, pet: Pet) -> None:
        pass