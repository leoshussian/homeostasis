from dataclasses import dataclass, field

from homeostasis.common import PersonalityMatrix, Stats
from homeostasis.items.base import Item


@dataclass(kw_only=True)
class FoodItem(Item):
    """Represents a food item that can be given to the pet."""
    name: str
    description: str = ""
    personality: PersonalityMatrix # How well this food matches the pet's personality

    nutrition: int
    satiety: int  # Scale from 1 to 10

    max_durability: int = field(default=1, init=False)

    def eat(self, personality: PersonalityMatrix) -> Stats:
        """Give the food to the pet and return its effects.

        Args:
            personality (PersonalityMatrix): The pet's personality matrix.
        Returns:

        """
        status = self.use()
        compatibility = PersonalityMatrix.get_compatibility(self.personality, personality)
        return Stats(
            happiness=compatibility * 10,
            hunger=self.satiety*5,
            health=self.nutrition*5,
            social=0,
            energy=0,
        )

    def get(self) -> "FoodItem":
        """Get a copy of the food item."""
        return FoodItem(
            name=self.name,
            description=self.description,
            personality=self.personality,
            nutrition=self.nutrition,
            satiety=self.satiety,
        )

FOOD_ITEMS = {}
def register_food_item(food_item: FoodItem):
    """Registers a food item in the global food items list."""
    FOOD_ITEMS[food_item.name] = food_item

register_food_item(FoodItem(
    name="Fufu Sauce Graine",
    nutrition=10,
    satiety=7,
    personality=PersonalityMatrix(
        friendliness=9,
        playfulness=9,
        laziness=2,
        curiosity=10,
    ),
    description = "An exotic sauce made from ground fufu seeds, known for its rich flavor and nutritional benefits.")
)

register_food_item(FoodItem(
    name="Dirty Martini",
    nutrition=-1,
    satiety=1,
    personality=PersonalityMatrix(
        friendliness=3,
        playfulness=8,
        laziness=5,
        curiosity=7,
    ),
    description = "A classic cocktail made with gin and a splash of olive brine, garnished with olives. Perfect for a sophisticated palate.",
))

register_food_item(FoodItem(
    name="Instant Spicy Ramen Noodles",
    nutrition=-3,
    satiety=4,
    personality=PersonalityMatrix(
        friendliness=7,
        playfulness=6,
        laziness=8,
        curiosity=5,
    ),
    description = "A quick and easy meal with a spicy kick, these instant ramen noodles are perfect for a fast and flavorful dining experience.",
))

register_food_item(FoodItem(
    name="Vegan Cheese Platter",
    nutrition=5,
    satiety=6,
    personality=PersonalityMatrix(
        friendliness=8,
        playfulness=2,
        laziness=4,
        curiosity=9,
    ),
    description = "A selection of artisanal vegan cheeses made from nuts and plant-based ingredients, served with crackers and fruit.",
))

register_food_item(FoodItem(
    name="Hummus and Pita Bread",
    nutrition=8,
    satiety=8,
    personality=PersonalityMatrix(
        friendliness=2,
        playfulness=5,
        laziness=7,
        curiosity=6,
    ),
    description = "A classic Middle Eastern snack featuring creamy hummus served with warm pita bread for dipping.",
))

register_food_item(FoodItem(
    name="Chocolate Lava Cake",
    nutrition=-2,
    satiety=5,
    personality=PersonalityMatrix(
        friendliness=9,
        playfulness=9,
        laziness=3,
        curiosity=8,
    ),
    description = "A decadent dessert with a rich chocolate exterior and a gooey molten center, perfect for satisfying your sweet tooth.",
))

register_food_item(FoodItem(
    name="Quinoa Salad with Avocado",
    nutrition=9,
    satiety=7,
    personality=PersonalityMatrix(
        friendliness=6,
        playfulness=4,
        laziness=5,
        curiosity=9,
    ),
    description = "A healthy and refreshing salad made with quinoa, fresh vegetables, and creamy avocado, dressed with a light vinaigrette.",
))

