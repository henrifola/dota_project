import os
import json
from os import listdir
from os.path import isfile, join


class Data_loader:

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
            if left_game is False:
                full_data_set[files] = game
        print("loaded dataset, with {} out of {} valid games".format(len(full_data_set), (i + 1)))
        return full_data_set


games = Data_loader.load_games("../data")
