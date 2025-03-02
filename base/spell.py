"""Module for the Spell class."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .character import BaseCharacter


class BaseSpell(ABC):
    """Abstract base class for all spells."""

    def __init__(
        self,
        name="",
        cast_time=0,
        cooldown=0,
        damage_percent=0,
        hits=1,
        channeled=False,
        ticks=0,
        is_debuff=False,
        debuff_duration=0,
        do_debuff_damage=False,
        is_buff=False,
        min_target_count=1,
        max_target_count=1000,
    ):
        self.name = name
        self.base_cast_time = cast_time
        self.cooldown = cooldown
        self.damage_percent = damage_percent / 100  # Convert to multiplier
        self.hits = hits  # Number of hits per cast
        self.remaining_cooldown = 0  # Tracks cooldown time remaining
        self.channeled = channeled
        self.is_debuff = is_debuff
        self.debuff_duration = debuff_duration
        self.remaining_debuff_duration = 0
        self.ticks = ticks
        self.next_tick_time = 0
        self.do_debuff_damage = do_debuff_damage
        self.is_buff = is_buff
        self.total_damage_dealt = 0
        self.min_target_count = (
            min_target_count  # Minimum Needed Targets to cast this on.
        )
        self.max_target_count = (
            max_target_count  # Maximum Needed Targets to cast this on.
        )

    @property
    def simfell_name(self) -> str:
        """Returns the name of the spell in the simfell file."""

        return self.name.lower().replace(" ", "_")

    @abstractmethod
    def effective_cast_time(self, character: "BaseCharacter") -> float:
        """Returns the effective cast time of the spell."""

    @abstractmethod
    def is_ready(self, character: "BaseCharacter", enemy_count: int) -> bool:
        """Returns True if the spell is ready to be cast."""

    @abstractmethod
    def damage(self, character: "BaseCharacter") -> float:
        """Returns the damage of the spell."""

    @abstractmethod
    def set_cooldown(self) -> None:
        """Sets the cooldown of the spell."""

    @abstractmethod
    def reset_cooldown(self) -> None:
        """Resets the cooldown of the spell."""

    @abstractmethod
    def update_cooldown(self, delta_time: int) -> None:
        """Decreases the remaining cooldown by the delta time."""

    @abstractmethod
    def apply_debuff(self) -> None:
        """Applies the debuff to the target."""

    @abstractmethod
    def update_remaining_debuff_duration(self, delta_time: int) -> None:
        """Decreases the remaining debuff duration by the delta time."""
