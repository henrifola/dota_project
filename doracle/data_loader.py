import os
import json
from os import listdir
from os.path import isfile, join


class DataLoader:

    @staticmethod
    def hero_data(games: dict):
        heroes_played = {}
        for i in range(129):
            heroes_played[i + 1] = {'win': 0, 'lose': 0, 'times_played': 0, 'win_rate': None, 'pick_rate': None}
        for i, k in enumerate(games):
            for player in games[k]['players']:
                for key in [player['hero_id']]:
                    if (player['player_slot'] < 128 and games[k]['radiant_win'] or
                            player['player_slot'] >= 128 and not games[k]['radiant_win']):
                        heroes_played[key]['win'] += 1
                    else:
                        heroes_played[key]['lose'] += 1
                    heroes_played[key]['times_played'] += 1
                    heroes_played[key]['win_rate'] = '{0:.4g}'.format(heroes_played[key]['win'] / heroes_played[key]['times_played'])
                    heroes_played[key]['pick_rate'] = '{0:.4g}'.format(heroes_played[key]['times_played']/ (i+1))
        with open('data/heroes_data.json', 'w') as fp:
            json.dump(heroes_played, fp)
        return heroes_played

    @staticmethod
    def load_games(folder):
        onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
        full_data_set = {}
        for i, files in enumerate(onlyfiles):
            game = {}
            with open(folder + "/" + files, "r") as file:
                data = json.load(file)
                for key, value in data['result'].items():
                    game[key] = value
            left_game = False
            for q in (game['players']):
                if q['leaver_status'] > 1:
                    left_game = True
            if not left_game:
                full_data_set[files] = game
        print("loaded dataset, with {} out of {} valid games".format(len(full_data_set), (i + 1)))
        heroes_played = DataLoader.hero_data(full_data_set)
        return full_data_set, heroes_played


games, heroes_played = DataLoader.load_games("../data")

print()
