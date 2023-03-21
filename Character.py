import random

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
        output += (", ".join(trait for trait in self.personality) + "\n")
        output += ", ".join(self.powers)
        return output

def create_character():
    random.seed()
    #Optional inputs, replace existing features
    use_techniques = True
    use_backgrounds = True
    use_erachima = True
    name = name_gen()
    race = race_gen(use_backgrounds)
    rituals = ritual_gen(use_techniques)
    stats = stats_gen()
    personality = personality_gen()
    powers = powers_gen(stats)
    character = Character(name, race, rituals, stats, personality, powers)
    return character

def name_gen():
    name_list = ["Kosha", "Courtenay", "Hackett", "Layton", "Jorden", "Deverel", "Karlis", "Peppin", "Samson", "Theobald"]
    return random.choice(name_list)

def race_gen(use_backgrounds):
    if (use_backgrounds):
        background_list = ["Archeologist", "Arcane Squire", "Outlander", "Soldier", "Charlatan", "Criminal", "Sailor", "Sage", "Reborn", "Noble"]
        return random.choice(background_list)
    else:
        race_list = ["Human", "Elf", "Half-Elf", "Dwarf", "Revenant", "Dragonborn", "Halfling", "Tiefling", "Eladrin", "Deva", "Half-Orc", "Goliath"]
        return random.choice(race_list)

def ritual_gen(use_techniques):
    if (use_techniques):
        return ["Ritual Gen set to use Techniques."]
    else:
        return ["Ritual Gen set to default, to use Rituals."]

def stats_gen():
    stats = [18, 17, 13, 12, 10, 8]
    random.shuffle(stats)
    return stats

def personality_gen():
    personalities = ["Contemptible", "Jealous", "Irritating", "Ferocious", "Cruel", "Resentful", "Bitter", "Grumpy", "Horrifying", "Unsettling", "Anxious", "Tense", "Worried", "Amusing", "Cheerful", "Content", "Captivating", "Optimistic", "Proud", "Calm", "Enthusiastic", "Zealous", "Affectionate", "Caring", "Compassionate", "Loving", "Sentimental", "Tender", "Passionate", "Attractive", "Disdainful", "Neglectful", "Dejected", "Embarrassed", "Lonely", "Gloomy", "Melancholic", "Guilty", "Regretful", "Remorseful", "Ashamed", "Suffering", "Pitiable"]
    personality = random.sample(personalities, 3)
    return personality

def powers_gen(stats):
    primary_stat = max(range(len(stats)), key=stats.__getitem__)
    #Strength Primary
    if (primary_stat == 0):
        #Stuff happens
        pass
    #Dexterity Primary
    elif (primary_stat == 1):
        #Stuff happens
        pass
    #Constitution Primary
    elif (primary_stat == 2):
        #Stuff happens
        pass
    #Intelligence Primary
    elif (primary_stat == 3):
        #Stuff happens
        pass
    #Wisdom Primary
    elif (primary_stat == 4):
        #Stuff happens
        pass
    #Charisma Primary, catch-all
    else:
        #Stuff happens
        pass
    return ["Test Power 1", "Test Power 2", "Test Power 3"]

"""
References:

List -> String: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
Index of max in list: https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
"""