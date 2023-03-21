import unittest
import Character
from UserInterface import run_gui

class Testing(unittest.TestCase):

    def test_name(self):
        name = Character.name_gen()
        self.assertIsInstance(name, str, "name_gen did not produce a string.")

    def test_race(self):
    	race = Character.race_gen(True)
    	self.assertIsInstance(race, str, "race_gen did not produce a string.")
    	race = Character.race_gen(False)
    	self.assertIsInstance(race, str, "race_gen did not produce a string.")

    def test_rituals(self):
    	rituals = Character.ritual_gen(True)
    	self.assertIsInstance(rituals, list, "ritual_gen did not produce a list.")
    	rituals = Character.ritual_gen(False)
    	self.assertIsInstance(rituals, list, "ritual_gen did not produce a list.")

    def test_stats(self):
    	stats = Character.stats_gen()
    	self.assertIsInstance(stats, list, "stats_gen did not produce a list.")

    def test_personality(self):
    	personality = Character.personality_gen()
    	self.assertIsInstance(personality, list, "personality_gen did not produce a list.")

    def test_powers(self):
    	stats = [10, 11, 12, 13, 14, 15]
    	powers = Character.powers_gen(stats)
    	self.assertIsInstance(powers, list, "powers_gen did not produce a list.")

    def test_character_creation(self):
    	new_character = Character.create_character()
    	self.assertIsInstance(new_character, Character.Character, "create_character did not produce a character.")

    #Not technically a unit test, but worth insisting we check...
    def test_gui(self):
    	run_gui()

if __name__ == '__main__':
    unittest.main()

'''

References:
Python unittest library walkthrough: https://www.digitalocean.com/community/tutorials/python-unittest-unit-test-example
unittest type assertions: https://www.geeksforgeeks.org/python-unittest-assertisinstance-function/

'''