from dataclasses import dataclass

from homeostasis.common import PersonalityMatrix, Stats
from homeostasis.items.base import Item


@dataclass(kw_only=True)
class PlayItem(Item):
    """Represents a play item that can be given to the pet."""
    name: str
    description: str = ""
    personality: PersonalityMatrix
    max_durability: int

    social: int  # Scale -10 to 10
    energy: int # Scale -10 to 10

    def play(self, personality: PersonalityMatrix) -> Stats:
        """Let the pet play with the item and return its fun effect.

        Args:
            personality (PersonalityMatrix): The pet's personality matrix.
        Returns:
            int: The fun effect on the pet.
        """
        status = self.use()
        compatibility = PersonalityMatrix.get_compatibility(self.personality, personality)
        return Stats(
            happiness=int(compatibility * 5),
            hunger=0,
            health=0,
            social=self.social * 5,
            energy=self.energy * 5,
        )

    def get(self) -> "PlayItem":
        """Get a copy of the play item."""
        return PlayItem(
            name=self.name,
            description=self.description,
            personality=self.personality,
            max_durability=self.max_durability,
            social=self.social,
            energy=self.energy,
        )

PLAY_ITEMS = {}
def register_play_item(play_item: PlayItem):
    """Registers a play item in the global play items list."""
    PLAY_ITEMS[play_item.name] = play_item

register_play_item(PlayItem(
    name="Squeaky Ball",
    description="A colorful squeaky ball that makes fun noises when squeezed.",
    personality=PersonalityMatrix(
        friendliness=8,
        playfulness=10,
        laziness=3,
        curiosity=7,
    ),
    max_durability=5,
    social=2,
    energy=-3,
))

register_play_item(PlayItem(
    name="Book: Heated Rivalry",
    description="An engaging story about an ice-melting rivalry on the hockey rink. Perfect for curious pets!",
    personality=PersonalityMatrix(
        friendliness=8,
        playfulness=7,
        laziness=2,
        curiosity=9,
    ),
    max_durability=1,
    social=-2,
    energy=-1,
))

register_play_item(PlayItem(
    name="Movie: Girl Interrupted",
    description="A captivating movie that explores the complexities of the human mind. Ideal for thoughtful pets!",
    personality=PersonalityMatrix(
        friendliness=7,
        playfulness=6,
        laziness=5,
        curiosity=4,
    ),
    max_durability=1,
    social=-1,
    energy=-2,
))

register_play_item(PlayItem(
    name="Lissajous Pendulum",
    description="A mesmerizing pendulum that creates intricate Lissajous curves.",
    personality=PersonalityMatrix(
        friendliness=6,
        playfulness=3,
        laziness=4,
        curiosity=10,
    ),
    max_durability=10,
    social=0,
    energy=-1,
))

register_play_item(PlayItem(
    name="Chorus Node",
    description="A responsive toy that produces different sounds when played with. Great for social pets.",
    personality=PersonalityMatrix(
        friendliness=10,
        playfulness=9,
        laziness=2,
        curiosity=6,
    ),
    max_durability=6,
    social=3,
    energy=-4,
))

register_play_item(PlayItem(
    name="Marginalia Codex",
    description="A strange book filled with notes and diagrams. Ideal for curious pets who enjoy quiet activities.",
    personality=PersonalityMatrix(
        friendliness=2,
        playfulness=3,
        laziness=4,
        curiosity=10,
    ),
    max_durability=2,
    social=-3,
    energy=-1,
))

register_play_item(PlayItem(
    name="Inertial Cushion",
    description="A soft resting item designed for long periods of relaxation.",
    personality=PersonalityMatrix(
        friendliness=5,
        playfulness=2,
        laziness=10,
        curiosity=3,
    ),
    max_durability=12,
    social=-1,
    energy=3,
))

register_play_item(PlayItem(
    name="Curiosity Engine",
    description="A small mechanical object with moving parts that invites experimentation.",
    personality=PersonalityMatrix(
        friendliness=4,
        playfulness=6,
        laziness=1,
        curiosity=9,
    ),
    max_durability=4,
    social=0,
    energy=-5,
))

register_play_item(PlayItem(
    name="Stillness Sphere",
    description="A quiet object that encourages calm and solitary play.",
    personality=PersonalityMatrix(
        friendliness=1,
        playfulness=1,
        laziness=7,
        curiosity=4,
    ),
    max_durability=8,
    social=-3,
    energy=1,
))

register_play_item(PlayItem(
    name="Clockwork Skitterer",
    description="A fast-moving toy that keeps pets active and entertained.",
    personality=PersonalityMatrix(
        friendliness=3,
        playfulness=9,
        laziness=2,
        curiosity=6,
    ),
    max_durability=7,
    social=-1,
    energy=-4,
))

register_play_item(PlayItem(
    name="Standard Engagement Module",
    description="A general-purpose play item suitable for most pets.",
    personality=PersonalityMatrix(
        friendliness=5,
        playfulness=5,
        laziness=5,
        curiosity=5,
    ),
    max_durability=9,
    social=0,
    energy=-1,
))
