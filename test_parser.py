"""Test the parser."""

from copy import deepcopy

from base import Character
from characters.Rime.spell import RimeSpell
from simfell_parser.condition_parser import SimFileConditionParser
from simfell_parser.simfile_parser import SimFileParser


parser = SimFileParser("test.simfell")
configuration = parser.parse()
# print(configuration.parsed_json)

character = Character(
    intellect=configuration.intellect,
    crit=configuration.crit,
    expertise=configuration.expertise,
    haste=configuration.haste,
    spirit=configuration.spirit,
)

test_spell = deepcopy(RimeSpell.COLD_SNAP.value)

print(f"Character Anima: {character.anima}\n")

print("Summary of actions and results:")
for action in configuration.actions:
    print(f"Action: '{action.name}', Conditions: {len(action.conditions)}")
    for condition in action.conditions:
        result = None  # pylint: disable=invalid-name

        if condition.left.startswith("character."):
            result = SimFileConditionParser.map_to_character_attribute(
                condition, character
            )
        elif condition.left.startswith("spell."):
            result = SimFileConditionParser.map_to_spell_attribute(
                condition, test_spell
            )

        if result is not None:
            print(f"\tCondition: {condition}")
            print(f"\tResult: {result}")
            print("\t--------------------")
