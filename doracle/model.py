import random
import json

class HeroStats:
    def __init__(self):
        pass

    def get_winrate(self, hero_id):
        try:
            with open('/home/henni/ai_course/dota-oracle/doracle/data/heroes_data.json', 'r') as fp:
                data = json.load(fp)
                return data[str(hero_id)]['win_rate']
        except Exception as err:
            print(err)
            return None

    def get_pickrate(self, hero_id):
        try:
            with open('/home/henni/ai_course/dota-oracle/doracle/data/heroes_data.json', 'r') as fp:
                data = json.load(fp)
                return data[str(hero_id)]['pick_rate']
        except Exception as err:
            print(err)
            return None

    def get_best_paired_with_hero(self, hero_id):
        return random.randint(0, 120)

    @staticmethod
    def load(path_to_model: str):
        print("loading model from: {}".format(path_to_model))
        return HeroStats()

