"""Module for parsing SimFell files."""

import re
from typing import List, Tuple

from simfell_parser.models import Action, SimFellConfiguration
from simfell_parser.condition_parser import SimFileConditionParser


class SimFileParser:
    """Class for parsing SimFell files."""

    def __init__(self, file_path: str):
        self._file_path = file_path

    def _handle_comments(self, line: str) -> str:
        """Handle comments in the line."""

        if "#" in line:
            return line[: line.index("#")]
        return line

    def parse(self) -> SimFellConfiguration:
        """Parse the SimFell file."""

        data = {"actions": []}

        with open(self._file_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue

                line = self._handle_comments(line)

                key, value = self._parse_line(line)

                if key.startswith("action") or key.startswith("actions"):
                    data["actions"].extend(value)
                else:
                    data[key] = value

        return SimFellConfiguration(**data)

    def _parse_list_like_line(self, list_line: str) -> List[Action]:
        """Parse a list-like line of the SimFell file into a list of Actions.

        Assumes that each action starts with "/" and that any conditions follow the action
        name, prefixed with ",if=", and multiple conditions are separated by " and ".
        """
        pattern = r'(?P<name>/[^,]+)(?:,if=(?P<conditions>[^,]+))?'
        actions = []
        
        for match in re.finditer(pattern, list_line):
            name = match.group("name").strip()
            conditions_str = match.group("conditions")
            conditions = []
            
            if conditions_str:
                conditions = [
                    SimFileConditionParser(cond.strip()).parse()
                    for cond in conditions_str.split(" and ")
                ]
                
            actions.append(Action(name=name, conditions=conditions))
        
        return actions

    def _parse_line(self, line: str) -> Tuple[str, str]:
        """Parse a line of the SimFell file."""

        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()

        # Handle "list-like" values for actions
        if key.startswith("action") or key.startswith("actions"):
            return key, self._parse_list_like_line(value)

        return key, value
