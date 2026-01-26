from dataclasses import dataclass


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
        score += 5 - abs(matrix1.friendliness - matrix2.friendliness)
        score += 5 - abs(matrix1.playfulness - matrix2.playfulness)
        score += 5 - abs(matrix1.laziness - matrix2.laziness)
        score += 5 - abs(matrix1.curiosity - matrix2.curiosity)
        return score / 20.0  # Normalize to [-1, 1]


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
    happiness: float = 100
    energy: float = 100
    social: float = 100
    hunger: float = 100
    health: float = 100

    def clamp_stats(self):
        """Ensure all stats are within the range 0-100."""
        for stat in Stats.__dataclass_fields__: # noqa
            value = getattr(self, stat)
            clamped_value = max(0, min(100, value))
            setattr(self, stat, clamped_value)

    def add_stats(self, other: 'Stats'):
        """Add another PetStats to this one.

        Args:
            other (Stats): The other Stats to add.

        Returns:
            Stats: The delta of the addition for reference.
        """
        for stat in Stats.__dataclass_fields__: # noqa
            current_value = getattr(self, stat)
            addition_value = getattr(other, stat)
            setattr(self, stat, current_value + addition_value)

        self.clamp_stats()
        # Return delta for reference
        return Stats(
            happiness=self.happiness - other.happiness,
            energy=self.energy - other.energy,
            social=self.social - other.social,
            hunger=self.hunger - other.hunger,
        )
