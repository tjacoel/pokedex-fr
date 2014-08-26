from app.models import EggGroup, PokemonType, Weakness

def main(data):
    for group in data["egg_groups"]:
        EggGroup.objects.get_or_create(name=group)
    
    for type_name in data["types"]:
        PokemonType.objects.get_or_create(name=type_name)
    
    for base_type, relation in data["weaknesses"].items():
        for receiving_type, weakness in relation.items():
            base_type = PokemonType.objects.get(name=base_type)
            receiving_type = PokemonType.objects.get(name=receiving_type)
            Weakness.objects.get_or_create(base_type=base_type, receiving_type=receiving_type, weakness=weakness)
    
data = {
    "egg_groups": [
        "egg_group_flying",
        "egg_group_amorphous",
        "egg_group_water1",
        "egg_group_water2",
        "egg_group_water3",
        "egg_group_dragon",
        "egg_group_fairy",
        "egg_group_humanlike",
        "egg_group_unknown",
        "egg_group_bug",
        "egg_group_ditto",
        "egg_group_mineral",
        "egg_group_monster",
        "egg_group_field",
        "egg_group_grass",
        "egg_group_no_egg",
    ],
    "types": [
        "NONE",
        "STEEL",
        "FIGHTING",
        "DRAGON",
        "WATER",
        "ELECTRIC",
        "FAIRY",
        "FIRE",
        "ICE",
        "BUG",
        "NORMAL",
        "GRASS",
        "POISON",
        "PSYCHIC",
        "ROCK",
        "GROUND",
        "GHOST",
        "DARK",
        "FLYING",
    ],
    "weaknesses": {
        'STEEL': {
            'STEEL': "STRONG",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "STRONG",
            'FIRE': "WEAK",
            'PSYCHIC': "STRONG",
            'FLYING': "STRONG",
            'FIGHTING': "WEAK",
            'DRAGON': "STRONG",
            'WATER': "NORMAL",
            'POISON': "IGNORE",
            'ICE': "STRONG",
            'DARK': "NORMAL",
            'ROCK': "STRONG",
            'FAIRY': "STRONG",
            'GRASS': "STRONG",
            'BUG': "STRONG",
            'GROUND': "WEAK"
        },
        'GHOST': {
            'STEEL': "NORMAL",
            'GHOST': "WEAK",
            'ELECTRIC': "NORMAL",
            'NORMAL': "IGNORE",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "IGNORE",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "STRONG",
            'ICE': "NORMAL",
            'DARK': "WEAK",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "STRONG",
            'GROUND': "NORMAL"
        },
        'ELECTRIC': {
            'STEEL': "STRONG",
            'GHOST': "NORMAL",
            'ELECTRIC': "STRONG",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "STRONG",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "NORMAL",
            'GROUND': "WEAK"
        },
        'NORMAL': {
            'STEEL': "NORMAL",
            'GHOST': "IGNORE",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "WEAK",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "NORMAL",
            'GROUND': "NORMAL"
        },
        'FIRE': {
            'STEEL': "STRONG",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "STRONG",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "WEAK",
            'POISON': "NORMAL",
            'ICE': "STRONG",
            'DARK': "NORMAL",
            'ROCK': "WEAK",
            'FAIRY': "STRONG",
            'GRASS': "STRONG",
            'BUG': "STRONG",
            'GROUND': "WEAK"
        },
        'PSYCHIC': {
            'STEEL': "NORMAL",
            'GHOST': "WEAK",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "STRONG",
            'FLYING': "NORMAL",
            'FIGHTING': "STRONG",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "WEAK",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "WEAK",
            'GROUND': "NORMAL"
        },
        'FLYING': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "WEAK",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "STRONG",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "WEAK",
            'DARK': "NORMAL",
            'ROCK': "WEAK",
            'FAIRY': "NORMAL",
            'GRASS': "STRONG",
            'BUG': "STRONG",
            'GROUND': "IGNORE"
        },
        'FIGHTING': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "WEAK",
            'FLYING': "WEAK",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "STRONG",
            'ROCK': "STRONG",
            'FAIRY': "WEAK",
            'GRASS': "NORMAL",
            'BUG': "STRONG",
            'GROUND': "NORMAL"
        },
        'DRAGON': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "STRONG",
            'NORMAL': "NORMAL",
            'FIRE': "STRONG",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "NORMAL",
            'DRAGON': "WEAK",
            'WATER': "STRONG",
            'POISON': "NORMAL",
            'ICE': "WEAK",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "WEAK",
            'GRASS': "STRONG",
            'BUG': "NORMAL",
            'GROUND': "NORMAL"
        },
        'WATER': {
            'STEEL': "STRONG",
            'GHOST': "NORMAL",
            'ELECTRIC': "WEAK",
            'NORMAL': "NORMAL",
            'FIRE': "STRONG",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "STRONG",
            'POISON': "NORMAL",
            'ICE': "STRONG",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "WEAK",
            'BUG': "NORMAL",
            'GROUND': "NORMAL"
        },
        'POISON': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "WEAK",
            'FLYING': "NORMAL",
            'FIGHTING': "STRONG",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "STRONG",
            'ICE': "NORMAL",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "STRONG",
            'GRASS': "STRONG",
            'BUG': "STRONG",
            'GROUND': "WEAK"
        },
        'ICE': {
            'STEEL': "WEAK",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "WEAK",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "WEAK",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "STRONG",
            'DARK': "NORMAL",
            'ROCK': "WEAK",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "NORMAL",
            'GROUND': "NORMAL"
        },
        'DARK': {
            'STEEL': "NORMAL",
            'GHOST': "STRONG",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "IGNORE",
            'FLYING': "NORMAL",
            'FIGHTING': "WEAK",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "STRONG",
            'ROCK': "NORMAL",
            'FAIRY': "WEAK",
            'GRASS': "NORMAL",
            'BUG': "WEAK",
            'GROUND': "NORMAL"
        },
        'ROCK': {
            'STEEL': "WEAK",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "STRONG",
            'FIRE': "STRONG",
            'PSYCHIC': "NORMAL",
            'FLYING': "STRONG",
            'FIGHTING': "WEAK",
            'DRAGON': "NORMAL",
            'WATER': "WEAK",
            'POISON': "STRONG",
            'ICE': "NORMAL",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "WEAK",
            'BUG': "NORMAL",
            'GROUND': "WEAK"
        },
        'FAIRY': {
            'STEEL': "WEAK",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "STRONG",
            'DRAGON': "IGNORE",
            'WATER': "NORMAL",
            'POISON': "WEAK",
            'ICE': "NORMAL",
            'DARK': "STRONG",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "NORMAL",
            'BUG': "STRONG",
            'GROUND': "NORMAL"
        },
        'GRASS': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "STRONG",
            'NORMAL': "NORMAL",
            'FIRE': "WEAK",
            'PSYCHIC': "NORMAL",
            'FLYING': "WEAK",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "STRONG",
            'POISON': "WEAK",
            'ICE': "WEAK",
            'DARK': "NORMAL",
            'ROCK': "NORMAL",
            'FAIRY': "NORMAL",
            'GRASS': "STRONG",
            'BUG': "WEAK",
            'GROUND': "STRONG"
        },
        'BUG': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "NORMAL",
            'NORMAL': "NORMAL",
            'FIRE': "WEAK",
            'PSYCHIC': "NORMAL",
            'FLYING': "WEAK",
            'FIGHTING': "STRONG",
            'DRAGON': "NORMAL",
            'WATER': "NORMAL",
            'POISON': "NORMAL",
            'ICE': "NORMAL",
            'DARK': "NORMAL",
            'ROCK': "WEAK",
            'FAIRY': "NORMAL",
            'GRASS': "STRONG",
            'BUG': "NORMAL",
            'GROUND': "STRONG"
        },
        'GROUND': {
            'STEEL': "NORMAL",
            'GHOST': "NORMAL",
            'ELECTRIC': "IGNORE",
            'NORMAL': "NORMAL",
            'FIRE': "NORMAL",
            'PSYCHIC': "NORMAL",
            'FLYING': "NORMAL",
            'FIGHTING': "NORMAL",
            'DRAGON': "NORMAL",
            'WATER': "WEAK",
            'POISON': "STRONG",
            'ICE': "WEAK",
            'DARK': "NORMAL",
            'ROCK': "STRONG",
            'FAIRY': "NORMAL",
            'GRASS': "WEAK",
            'BUG': "NORMAL",
            'GROUND': "NORMAL"
        }
    }
}


main(data)