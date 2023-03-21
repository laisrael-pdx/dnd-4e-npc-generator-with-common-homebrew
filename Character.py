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

def create_character(use_techniques=True, use_backgrounds=True):
    random.seed()
    #Optional inputs, replace existing features
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
        return ["Panoply Lore"]
    else:
        return ["Temporary Fix"]

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
        powers = ["Standard Action - Melee - Pummel - 1d20+4 vs. AC - 1d8+4 damage", "Standard Action - Melee - Shove - 1d20+4 vs. Reflex - 1d6+4 damage and push 2", "Standard Action - Melee - Gut Punch - 1d20+4 vs. Fortitude - 1d6+4 damage and target falls prone"]
    #Dexterity Primary
    elif (primary_stat == 1):
        powers = ["Standard Action - Ranged 5 - Pocket Sand - 1d20+4 vs. AC - 4 damage and the target is blinded until the end of their next turn.", "Standard Action - Melee - Quick Slash - 1d20+4 vs. AC - 1d4+4 damage and ongoing 2 damage (save ends)", "Immediate Reaction Trigger on an enemy moving adjacent - Personal - Split - The NPC may shift up to their speed, ending their movement further from the triggering enemy than they started."]
    #Constitution Primary
    elif (primary_stat == 2):
        powers = ["Standard Action - Melee - Wrestle - 1d20+4 vs. AC - 1d4+4 damage and the target is grabbed and prone.", "Standard Action against a prone enemy - Melee - Pin - 1d20+4 vs. Fortitude - 1d6+4 damage and the target cannot stand until the end of their next turn.", "No Action - Personal - Endure - If the NPC would fall unconscious due to being at 0 or fewer hitpoints, they remain conscious until the end of their next turn."]
    #Intelligence Primary
    elif (primary_stat == 3):
        powers = ["Standard Action - Ranged 20 - Magic Missile - 4 damage", "Standard Action - Ranged 10 - Fire Bolt - 1d20+4 vs. Reflex - 1d6+4 fire damage", "Minor Action - Anyone who can hear the NPC - Lecture - 1d20+4 vs. Will - 1d4+4 psychic damage and the target is slowed."]
    #Wisdom Primary
    elif (primary_stat == 4):
        powers = ["Standard Action - Ranged 10 - Invoke - 1d20+4 vs. Reflex - 1d4+4 radiant damage", "Standard Action - Melee - Find Opening - 1d20+4 vs. AC - 1d4+4 damage and the target grants combat advantage (save ends)", "No Action - Personal - Overcome - The NPC makes a saving throw against all conditions currently affecting them, even if that condition does not allow saving throws."]
    #Charisma Primary, catch-all
    else:
        powers = ["Standard Action - Ranged 5 - Insult - 1d20+4 vs. Will - 1d6+4 pyschic damage and target takes a -2 to attack rolls until the end of their next turn.", "Standard Action - Close Burst 2 - Pacify - 1d20+4 vs. Will - 1d4+4 damage and the target takes a -2 penalty to damage rolls until the end of their next turn.", "Minor Action - All enemies who can hear - Quick Talker - For this turn, the NPC does not provoke attacks of opportunity."]
    return powers

"""
References:

List -> String: https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string
Index of max in list: https://stackoverflow.com/questions/2474015/getting-the-index-of-the-returned-max-or-min-item-using-max-min-on-a-list
"""