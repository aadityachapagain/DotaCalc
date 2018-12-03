import json
from flask import abort

def get_data():
    with open('dota_hero.jp','r') as file_read:
        Heros = json.load(file_read)

    return Heros

# Create a handler for our get Heros
def read_all():
    """
     This function responds to a request for /api/hero
    with the complete lists of Heros
    :return: list of heros with their roles and counter
    """
    return get_data()

def read_one(Heroname):
    Heroname = Heroname.replace('_',' ').lower()
    Heros = get_data()
    hero = list(filter(lambda hero: hero["name"].lower() == Heroname,Heros))
    if len(hero):
        return hero[0]
    else:
        abort(
            404,f"hero with name {Heroname} not found !"
        )