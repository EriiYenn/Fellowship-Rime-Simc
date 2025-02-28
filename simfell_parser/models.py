"""Models for the SimFell file."""

from typing import Any, List

from pydantic import BaseModel


class Condition(BaseModel):
    """Class for a condition in a SimFell file."""

    left: str
    operator: str
    right: Any


class Action(BaseModel):
    """Class for an action in a SimFell file."""

    name: str
    conditions: List[Condition]

    def __str__(self):
        return f"{self.name} ({', '.join(self.conditions)})"


class SimFellConfiguration(BaseModel):
    """Class for a SimFell configuration."""

    name: str
    hero: str
    intellect: int
    crit: int
    expertise: int
    haste: int
    spirit: int
    talents: str
    trinket1: str
    trinket2: str
    duration: int
    enemies: int

    actions: List[Action]

    @property
    def parsed_json(self) -> str:
        """Convert the configuration to a JSON string."""

        return self.model_dump_json(indent=2)
