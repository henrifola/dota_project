# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import getpass
import json
import os
import requests as req
from flask import Flask, render_template, request, jsonify, g, redirect, url_for, send_from_directory
from functools import lru_cache
package_directory = os.path.dirname(os.path.abspath(__file__))

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

# ----------------------------------------------------------------------------#
# Renders
# ----------------------------------------------------------------------------#


@app.route("/")
def index():
    return render_template("index.html", heroes=get_heroes())


@app.route("/explore")
def explore():
    return render_template("explore.html", heroes=get_heroes())


# ----------------------------------------------------------------------------#
# Oracle
# ----------------------------------------------------------------------------#

# <button 1>
@app.route("/suggest1", methods=["POST"])
def suggest1():
    r = request.get_json()



    return jsonify(r)

# <button 2>
@app.route("/suggest2", methods=["POST"])
def suggest2():
    r = request.get_json()



    return jsonify(r)


# <button 3>
@app.route("/suggest3", methods=["POST"])
def suggest3():
    r = request.get_json()



    return jsonify(r)

# ----------------------------------------------------------------------------#
# Explore
# ----------------------------------------------------------------------------#


@app.route("/stats/<int:heroid>", methods=["GET"])
def get_hero_stats(heroid):



    return jsonify(heroid)

# ----------------------------------------------------------------------------#
# Helpers
# ----------------------------------------------------------------------------#

@lru_cache(maxsize=32)
def get_heroes():
    print(os.getcwd())
    with open(os.path.join(package_directory, "data/heroes.json"), "r") as fp:
        heroes = json.load(fp)
    
    return heroes


if __name__ == '__main__':
    app.jinja_env.cache = {}
    app.run(debug=debug_mode, host='127.0.0.1', port=frontend_port)
