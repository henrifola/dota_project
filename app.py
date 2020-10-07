# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

import getpass
import json
from flask import Flask, render_template, request, jsonify, g, redirect, url_for

# ----------------------------------------------------------------------------#
# Configs
# ----------------------------------------------------------------------------#

frontend_port = 5000
app = Flask(__name__, static_folder='static', template_folder='templates')

# TODO: Remove before prod
running_user = getpass.getuser()
if running_user == "baon":    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    debug_mode = True


# ----------------------------------------------------------------------------#
# Renders
# ----------------------------------------------------------------------------#

@app.route("/")
def index():
    return render_template("index.html")


# ----------------------------------------------------------------------------#
# API
# ----------------------------------------------------------------------------#

""" 
@app.route("/api/hero/avatar", methods=["GET"])
def surveys():
    pass
    return jsonify(False)
 """

if __name__ == '__main__':
    # Custom jinja functions
    # app.jinja_env.globals.update(prettify_float=prettify_float, prettify_label=prettify_label)

    app.run(debug=debug_mode, host='0.0.0.0', port=frontend_port)