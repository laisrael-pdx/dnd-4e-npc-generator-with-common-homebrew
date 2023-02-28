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
        output += (self.name + "\n")
        output += (self.race + "\n")
        output += (", ".join(self.rituals) + "\n")
        output += (", ".join(str(stat) for stat in self.stats) + "\n")
        output += (self.personality + "\n")
        output += ", ".join(self.powers)
        return output

def create_character():
    use_techniques = True
    use_backgrounds = True
    use_erachima = True
    name = name_gen()
    race = race_gen(use_backgrounds)
    rituals = ritual_gen(use_techniques)
    stats = stats_gen()
    personality = personality_gen()
    powers = powers_gen()
    return Character(name, race, rituals, stats, personality, powers)

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