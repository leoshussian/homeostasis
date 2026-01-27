from dataclasses import dataclass
from typing import Union


@dataclass
class PersonalityMatrix:
    """Personality traits affecting pet behavior."""
    friendliness: int = 5
    playfulness: int = 5
    laziness: int = 5
    curiosity: int = 5

    @staticmethod
    def get_compatibility(matrix1, matrix2) -> float:
        """Calculates compatibility score between two personality matrices."""
        score = 0
        fields = 0
        for trait in PersonalityMatrix.__dataclass_fields__:  # noqa
            value1 = getattr(matrix1, trait)
            value2 = getattr(matrix2, trait)
            score += 10 - abs(value1 - value2)  # Max difference is 10
            fields += 1

        # score now ranges from 0 to 10 * number of fields
        # Normalize to [-1, 1]
        score = (score / (10 * fields)) * 2 - 1 # [0, fields*10] -> [0, 1] -> [0, 2] -> [-1, 1]
        return score

@dataclass
class Stats:
    """Represents the core stats of the pet.

    Attributes:
        happiness (int): The pet's happiness level (0-100).
        energy (int): The pet's energy level (0-100).
        social (int): The pet's social interaction level (0-100).
        hunger (int): The pet's hunger level (0-100).
        health (int): The pet's health level (0-100).
    """
    happiness: float = 0
    health: float = 0
    hunger: float = 0
    energy: float = 0
    social: float = 0
    fun: float = 0

    def clamp_stats(self):
        """Ensure all stats are within the range 0-100."""
        for stat in Stats.__dataclass_fields__: # noqa
            value = getattr(self, stat)
            clamped_value = max(0, min(100, value))
            setattr(self, stat, clamped_value)

    def add_stats(self, other: 'Stats', weights: Union['StatsWeights', None] = None) -> None:
        """Add another PetStats to this one and apply weights.

        Args:
            other (Stats): The other Stats to add.
            weights (StatsWeights): The weights to apply to the addition.
        """
        if weights is None:
            weights = StatsWeights(1, 1, 1, 1, 1, 1)

        for stat in Stats.__dataclass_fields__: # noqa
            current_value = getattr(self, stat)
            addition_value = getattr(other, stat)
            weight = getattr(weights, stat)
            setattr(self, stat, current_value + (addition_value * weight))

        self.clamp_stats()

@dataclass
class StatsWeights:
    happiness: float = 1
    energy: float = 1
    social: float = 1
    hunger: float = 1
    health: float = 1
    fun: float = 1

    def apply(self, stats: Stats, scale: float = 1.0) -> Stats:
        """Apply weights to a scale factor and return as Stats.

        Args:
            stats (Stats): The base stats to apply weights to.
            scale (float): The scale factor to apply.

        Returns:
            Stats: The resulting Stats after applying weights and scale.
        """
        values = {}
        for stat in Stats.__dataclass_fields__: # noqa
            # Get the current value of stat, multiply by weight, and scale
            value = getattr(stats, stat) * getattr(self, stat) * scale
            values[stat] = value

        return Stats(**values)