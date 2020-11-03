import random
import json

class HeroStats:
    def __init__(self):
        pass

    def get_winrate(self, hero_id):
        try:
            with open('data/heroes_data.json', 'r') as fp:
                data = json.load(fp)
                return data[hero_id]['win_rate']
        except:
            return None

    def get_pickrate(self, hero_id):
        return random.random()

    def get_best_paired_with_hero(self, hero_id):
        return random.randint(0, 120)

    @staticmethod
    def load(path_to_model: str):
        print("loading model from: {}".format(path_to_model))
        return HeroStats()

