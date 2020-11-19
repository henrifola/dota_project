import json
import shutil
import os
from os import listdir
from os.path import isfile, join
import numpy as np
import glob


class DataLoader:
    @staticmethod
    def hero_calc(folder):
        heroes_played = {}
        game = {}
        tot = 0
        for i in range(129):
            heroes_played[i + 1] = {'win': 0, 'lose': 0, 'times_played': 0, 'win_rate': None, 'pick_rate': None}
        for i, files in enumerate(glob.glob(folder)):
            tot += 1
            with open(files, "r") as file:
                data = json.load(file)
                for keys, value in data['result'].items():
                    game[keys] = value
            for player in game['players']:
                for key in [player['hero_id']]:
                    if (player['player_slot'] < 128 and game['radiant_win'] or
                            player['player_slot'] >= 128 and not game['radiant_win']):
                        heroes_played[key]['win'] += 1
                    else:
                        heroes_played[key]['lose'] += 1
                    heroes_played[key]['times_played'] += 1

                    heroes_played[key]['win_rate'] = '{0:.4g}'.format(
                        heroes_played[key]['win'] / heroes_played[key]['times_played'])
                    heroes_played[key]['pick_rate'] = '{0:.4g}'.format(heroes_played[key]['times_played'] / (i + 1))
        print("total games {}".format(tot))
        try:
            with open('data/heroes_data.json', 'w') as fp:
                json.dump(heroes_played, fp)
        except Exception as err:
            print("exeption hero data {}".format(err))

    @staticmethod
    def clean_data(folder, target):
        valid_games = 0
        total_games = 0

        for files in glob.glob(folder):
            invalid = False
            total_games += 1
            game = {}
            with open(files, "r") as file:
                data = json.load(file)
                for key, value in data['result'].items():
                    game[key] = value
            try:
                if game['duration'] < 420 or game['human_players'] != 10:
                    print("duration < 420")
                    invalid = True
                for q in (game['players']):
                    if q['leaver_status'] > 1 or not 0 < q['hero_id'] < 130:
                        print("leaver status {}, heroID {}".format(q['leaver_status'], q['hero_id']))
                        invalid = True
                if not invalid:
                    shutil.move(os.path.join(folder, files), target)
                    valid_games += 1
                    print("Moved {} from {} to {}. Valid games {}, totat games {}".format(files, folder, target,
                                                                                          valid_games, total_games))
            except Exception as err:
                print("Exeption load {}".format(err))
        print("loaded dataset, with {} out of {} valid games".format(valid_games, total_games))
        # 2069604 valid games
        return

    @staticmethod
    def skrt(file):
        heroes = {}
        with open(file, "r+") as f:
            data = json.load(f)

            for d in data:
                heroes[d['id']] = d
            f.seek(0)
            json.dump(heroes, f)


# 1
# DataLoader.skrt("data/heroes.json")

# 2
# DataLoader.clean_data('/home/henni/dota_games/*.json', '/home/henni/cleaned_games')
# DataLoader.clean_data('PATH /*.json', target for move)

# 3 already in data folder
#DataLoader.hero_calc('/home/henni/cleaned_games/*.json')

