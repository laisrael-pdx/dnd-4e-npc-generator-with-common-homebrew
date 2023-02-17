class Character:
    def __init__(self, name, race, rituals, stats, personality, powers):
        self.name = name
        self.race = race
        self.rituals = rituals
        self.stats = stats
        self.personality = personality
        self.powers = powers
    def __str__(self):
        output = ""
        output += (self.name + ";")
        output += (self.race + ";")
        output += ", ".join(self.rituals)
        output += (", ".join(str(stat) for stat in self.stats) + ";")
        output += (self.personality + ";")
        output += ", ".join(self.powers)
        return output

def create_character():
    options = user_prompts()
    use_techniques = options[0]
    use_backgrounds = options[1]
    use_erachima = options[2]
    name = name_gen()
    race = race_gen(use_backgrounds)
    rituals = ritual_gen(use_techniques)
    stats = stats_gen()
    personality = personality_gen()
    powers = powers_gen()
    return Character(name, race, rituals, stats, personality, powers)

def user_prompts():
    done = False
    while (not done):
        techniques = input("Would you like to use Techniques instead of Rituals? (Y/N)\n")
        if (techniques.upper() == "Y"):
            use_techniques = True
            done = True
        elif (techniques.upper() == "N"):
            use_techniques = False
            done = True
        else:
            print('Please enter "Y" or "N".\n')
    done = False
    while (not done):
        backgrounds = input("Would you like to use Backgrounds instead of Races? (Y/N)\n")
        if (backgrounds.upper() == "Y"):
            use_backgrounds = True
            done = True
        elif (backgrounds.upper() == "N"):
            use_backgrounds = False
            done = True
        else:
            print('Please enter "Y" or "N".\n')
    done = False
    while(not done):
        erachima = input("Would you like to use some of Erachima's classes and feats? (Y/N)\n")
        if (erachima.upper() == "Y"):
            use_erachima = True
            done = True
        elif (erachima.upper() == "N"):
            use_erachima = False
            done = True
        else:
            print('Please enter "Y" or "N".\n')
    return [use_techniques, use_backgrounds, use_erachima]

def name_gen():
    return "Name Gen created."

def race_gen(use_backgrounds):
    if (use_backgrounds):
        return "Race Gen set to use Backgrounds."
    else:
        return "Race Gen set to default, to use Races."

def ritual_gen(use_techniques):
    if (use_techniques):
        return ["Ritual Gen set to use Techniques."]
    else:
        return ["Ritual Gen set to default, to use Rituals."]

def stats_gen():
    return [17, 16, 13, 12, 10, 8]

def personality_gen():
    return "Personality Gen created."

def powers_gen():
    return ["Test Power 1", "Test Power 2", "Test Power 3"]

"""
References:

List -> String: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
"""