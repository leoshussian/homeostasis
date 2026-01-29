"""Temporary main module for homeostasis package."""
from time import sleep

from homeostasis.simulation.action import EatAction, PlayAction
from homeostasis.common import Traits, Motives
from homeostasis.items.food import register_food_items
from homeostasis.items.play import register_play_items
from homeostasis.pet import *
from homeostasis.items.base import ITEMS


def main():
    pet = Pet(
        info=PetSpec(name="Buddy", age=3, style="Casual"),
        personality=Traits(friendliness=5, playfulness=3, laziness=10, curiosity=7),
        motives=Motives(
            happiness=50,
            energy=50,
            social=50,
            hunger=50,
            health=50,
            fun=50,
        ),
    )

    register_food_items()
    register_play_items()

    FOOD_ITEMS = [item for item in ITEMS.values() if "edible" in item.tags]
    PLAY_ITEMS = [item for item in ITEMS.values() if "playable" in item.tags]

    print("Initial pet motives:", pet.motives)
    print("=== Using Food Items ===")
    for food_item in FOOD_ITEMS:
        item_instance = food_item.spawn()
        action = EatAction(item_instance)
        pet.set_action(action)
        while pet.is_busy:
            print(f"Feeding {food_item.name}...")
            pet.tick()
            sleep(2)  # Simulate time passing
        print(f"After eating {food_item.name}, pet motives: {pet.motives}")

    print("=== Using Play Items ===")
    for play_item in PLAY_ITEMS:
        item_instance = play_item.spawn()
        action = PlayAction(item_instance)
        pet.set_action(action)
        while pet.is_busy:
            print(f"Playing with {play_item.name}...")
            pet.tick()
            sleep(2)  # Simulate time passing
        print(f"After playing with {play_item.name}, pet motives: {pet.motives}")

if __name__ == "__main__":
    main()