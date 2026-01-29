from homeostasis.common import Traits, Motives, MotivesModifier
from homeostasis.items.base import ItemDefinition, register_item

def register_food_items():
    """Registers food items in the global items list."""
    
    register_item(ItemDefinition(
        name="Fufu Sauce Graine",
        description="An exotic sauce made from ground fufu seeds.",
        max_durability=1,
        personality=Traits(9, 9, 2, 10),
        effects=Motives(happiness=6, hunger=35, health=50),
        tags=frozenset({"edible"}),
    ))

    register_item(ItemDefinition(
        name="Dirty Martini",
        description="A classic cocktail with gin and olive brine.",
        max_durability=1,
        personality=Traits(3, 8, 5, 7),
        effects=Motives(happiness=4, hunger=5, health=-5),
        tags=frozenset({"edible", "alcohol"}),
    ))

    register_item(ItemDefinition(
        name="Instant Spicy Ramen Noodles",
        description="Quick, spicy instant noodles.",
        max_durability=1,
        personality=Traits(7, 6, 8, 5),
        effects=Motives(happiness=4, hunger=20, health=-15),
        tags=frozenset({"edible"}),
    ))

    register_item(ItemDefinition(
        name="Vegan Cheese Platter",
        description="A selection of artisanal vegan cheeses.",
        max_durability=1,
        personality=Traits(8, 2, 4, 9),
        effects=Motives(happiness=5, hunger=30, health=25),
        tags=frozenset({"edible"}),
    ))

    register_item(ItemDefinition(
        name="Hummus and Pita Bread",
        description="A classic Middle Eastern snack.",
        max_durability=1,
        personality=Traits(2, 5, 7, 6),
        effects=Motives(happiness=4, hunger=40, health=40),
        tags=frozenset({"edible"}),
    ))

    register_item(ItemDefinition(
        name="Chocolate Lava Cake",
        description="A decadent dessert with molten centre.",
        max_durability=1,
        personality=Traits(9, 9, 3, 8),
        effects=Motives(happiness=8, hunger=25, health=-10),
        tags=frozenset({"edible", "dessert"}),
    ))

    register_item(ItemDefinition(
        name="Quinoa Salad with Avocado",
        description="A healthy salad with quinoa and avocado.",
        max_durability=1,
        personality=Traits(6, 4, 5, 9),
        effects=Motives(happiness=5, hunger=35, health=45),
        tags=frozenset({"edible", "healthy"}),
    ))

