from data import *


def get_hero_name(hero_id):
    data = get_hero_data(hero_id)
    data = convert_data(data)
    for hero in data:
        if hero.id == hero_id:
            return hero.localized_name
