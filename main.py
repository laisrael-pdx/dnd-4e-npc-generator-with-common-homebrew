#Need to move to new file, and generate each attribute in its own file too
class Character:
    def __init__(self, name, race, backgrounds, rituals, techniques, stats, personality, powers):
        self.name = name
        self.race = race
        self.backgrounds = backgrounds
        self.rituals = rituals
        self.techniques = techniques
        self.stats = stats
        self.personality = personality
        self.powers = powers
    def __str__(self):
        output = ""
        output += (self.name + ";")
        output += (self.race + ";")
        if self.backgrounds:
            output += "Backgrounds - Y;"
        else:
            output += "Backgrounds - N;"
        if self.rituals:
            output += "Rituals - Y;"
        else:
            output += "Rituals - N;"
        if self.techniques:
            output += "Techniques - Y;"
        else:
            output += "Techniques - N"
        output += (", ".join(str(stat) for stat in self.stats) + ";")
        output += (self.personality + ";")
        output += ", ".join(self.powers)
        return output


if (__name__ == "__main__"):
    #Should switch to a loop re-asking for valid input
    techniques = input("Would you like to use Techniques instead of Rituals? (Y/N)\n")
    if (techniques.upper() == "Y"):
        use_techniques = True
        use_rituals = False
    backgrounds = input("Would you like to use Backgrounds instead of Races? (Y/N)\n")
    if (backgrounds.upper() == "Y"):
        use_backgrounds = True
    erachima = input("Would you like to use some of Erachima's classes and feats? (Y/N)\n")
    if (erachima.upper == "Y"):
        use_erachima = True
    new_character = Character("Test Character", "Test Race/BG", use_backgrounds, use_rituals, use_techniques, [17, 16, 13, 12, 10, 8], "Test Personality", ["Test Power 1", "Test Power 2", "Test Power 3"])
    print("Your character is: ")
    print(new_character)

"""
References:

List -> String: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
"""