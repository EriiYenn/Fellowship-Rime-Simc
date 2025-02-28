"""Test the parser."""

from base import Character
from simfell_parser.condition_parser import SimFileConditionParser
from simfell_parser.simfile_parser import SimFileParser


parser = SimFileParser("test.simfell")
configuration = parser.parse()
# print(configuration.parsed_json)

character = Character(
    intellect=100,
    crit=100,
    expertise=100,
    haste=100,
    spirit=100,
)


print(f"Character Anima: {character.anima}\n")

for action in configuration.actions:
    for condition in action.conditions:
        result = SimFileConditionParser.map_to_character_attribute(
            condition, character
        )
        if result is not None:
            print(f"Condition: {condition}")
            print(f"Result: {result}\n")
