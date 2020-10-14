# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import getpass
import json
import requests as req
from flask import Flask, render_template, request, jsonify, g, redirect, url_for
from functools import lru_cache

# ----------------------------------------------------------------------------#
# Configs
# ----------------------------------------------------------------------------#

frontend_port = 5000
app = Flask(__name__, static_folder='static', template_folder='templates')

# TODO: Remove before prod
running_user = getpass.getuser()

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.jinja_env.auto_reload = True
debug_mode = True
api_key = "651D11ADABD8BB56A3A79190F32BFE61"

# ----------------------------------------------------------------------------#
# Renders
# ----------------------------------------------------------------------------#

@app.route("/")
def index():
    return render_template("index.html", heroes=get_heroes())


# ----------------------------------------------------------------------------#
# API
# ----------------------------------------------------------------------------#


@app.route("/hero", methods=["GET"])
def hero():
    list_of_heroes = get_heroes()
    return jsonify(list_of_heroes)


# ----------------------------------------------------------------------------#
# Helpers
# ----------------------------------------------------------------------------#

@lru_cache(maxsize=32)
def get_heroes():
    img_size = "sb.png" #sb.png lg.png full.png vert.jpg
    resp = req.get("http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1?key={}".format(api_key))
    heroes = resp.json()["result"]["heroes"]

    # remove prefix from name, add avatar url
    for hero in heroes:
        hero["name"] = str(hero["name"]).replace("npc_dota_hero_", "")
        hero["pretty_name"] = hero["name"].replace("_", " ").title()
        hero["url"] = "http://cdn.dota2.com/apps/dota2/images/heroes/{}_{}".format(hero["name"], img_size)

    print(heroes)

    return heroes
    

if __name__ == '__main__':
    # Custom jinja functions
    # app.jinja_env.globals.update(prettify_float=prettify_float, prettify_label=prettify_label)

    app.run(debug=debug_mode, host='0.0.0.0', port=frontend_port)