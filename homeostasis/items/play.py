from homeostasis.common import Traits, Stats, StatsWeights
from homeostasis.items.base import ItemDefinition, register_item

def register_play_items():
    """Registers play items in the global items list."""

    register_item(ItemDefinition(
        name="Squeaky Ball",
        description="A colorful squeaky ball that makes fun noises when squeezed.",
        max_durability=5,
        personality=Traits(8, 10, 3, 7),
        effects=Stats(happiness=5, social=10, energy=-15),
        tags=frozenset({"playable"}),
    ))

    register_item(ItemDefinition(
        name="Book: Heated Rivalry",
        description="An engaging story about an ice-melting rivalry on -- and off -- the hockey rink.",
        max_durability=1,
        personality=Traits(8, 7, 2, 9),
        effects=Stats(happiness=4, social=-10, energy=-5, fun=10),
        tags=frozenset({"playable", "quiet"}),
    ))

    register_item(ItemDefinition(
        name="Movie: Girl Interrupted",
        description="A captivating movie exploring the human mind.",
        max_durability=1,
        personality=Traits(7, 6, 5, 4),
        effects=Stats(happiness=4, social=-5, energy=-10),
        tags=frozenset({"playable", "quiet"}),
    ))

    register_item(ItemDefinition(
        name="Lissajous Pendulum",
        description="A mesmerizing pendulum creating intricate curves.",
        max_durability=10,
        personality=Traits(6, 3, 4, 10),
        effects=Stats(happiness=3, energy=-5),
        tags=frozenset({"playable", "quiet"}),
    ))

    register_item(ItemDefinition(
        name="Chorus Node",
        description="A responsive toy producing different sounds.",
        max_durability=6,
        personality=Traits(10, 9, 2, 6),
        effects=Stats(happiness=6, social=15, energy=-20),
        tags=frozenset({"playable"}),
    ))

    register_item(ItemDefinition(
        name="Marginalia Codex",
        description="A strange book filled with notes and diagrams.",
        max_durability=2,
        personality=Traits(2, 3, 4, 10),
        effects=Stats(happiness=3, social=-15, energy=-5),
        tags=frozenset({"playable", "quiet"}),
    ))

    register_item(ItemDefinition(
        name="Inertial Cushion",
        description="A soft resting item designed for relaxation.",
        max_durability=12,
        personality=Traits(5, 2, 10, 3),
        effects=Stats(happiness=2, energy=15, social=-5),
        tags=frozenset({"playable", "rest"}),
    ))

    register_item(ItemDefinition(
        name="Curiosity Engine",
        description="A mechanical object inviting experimentation.",
        max_durability=4,
        personality=Traits(4, 6, 1, 9),
        effects=Stats(happiness=4, energy=-25),
        tags=frozenset({"playable"}),
    ))

    register_item(ItemDefinition(
        name="Stillness Sphere",
        description="A quiet object encouraging calm and solitude.",
        max_durability=8,
        personality=Traits(1, 1, 7, 4),
        effects=Stats(happiness=2, energy=5, social=-15),
        tags=frozenset({"playable", "quiet"}),
    ))

    register_item(ItemDefinition(
        name="Clockwork Skitterer",
        description="A fast-moving toy that keeps pets active.",
        max_durability=7,
        personality=Traits(3, 9, 2, 6),
        effects=Stats(happiness=5, energy=-20, social=-5),
        tags=frozenset({"playable"}),
    ))

    register_item(ItemDefinition(
        name="Standard Engagement Module",
        description="A general-purpose play item suitable for most pets.",
        max_durability=9,
        personality=Traits(5, 5, 5, 5),
        effects=Stats(happiness=3, energy=-5, fun=10),
        tags=frozenset({"playable"}),
    ))