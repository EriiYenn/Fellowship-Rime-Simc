"""Module for the Character class."""

from abc import ABC, abstractmethod
from typing import Dict, List, TYPE_CHECKING
from enum import Enum


if TYPE_CHECKING:
    from .spell import BaseSpell


class BaseCharacter(ABC):
    """Abstract base class for all characters."""

    def __init__(self, intellect, crit, expertise, haste, spirit):
        self.intellect_points = intellect
        self.intellect = intellect * self.intellectPerPoint
        self.crit_points = crit
        self.crit = (crit * self.critPerPoint) + 5  # % chance (e.g., 5 for 5%)
        self.expertise_points = expertise
        self.expertise = (  # % increase to damage
            expertise * self.expertisePerPoint
        )
        self.haste_points = haste
        # % increase to cast speed
        self.haste = haste * self.hastePerPoint
        self.spirit = spirit * self.spiritPerPoint
        self.spirit_points = spirit
        # This will hold the character's available spells.
        self.spells: Dict[str, BaseSpell] = {}
        # This will hold the character's rotation.
        self.rotation: List[BaseSpell] = []
        # All the talents.
        self.talents: List[str] = []
        # Buffs
        self.buffs: Dict[str, BaseSpell] = {}

    @abstractmethod
    def add_spell_to_rotation(self, spell: Enum) -> None:
        """Adds a spell to the character's rotation."""

    @abstractmethod
    def add_talent(self, talent: str) -> None:
        """Adds a talent to the character's available talents."""

    @abstractmethod
    def update_stats(
        self,
        intellect: int,
        crit: int,
        expertise: int,
        haste: int,
        spirit: int,
    ) -> None:
        """Updates the character's stats."""
