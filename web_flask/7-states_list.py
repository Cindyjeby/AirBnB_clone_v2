#!/usr/bin/python3
"""start flask"""

from flask import Flash, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """display aHTMLpage with list of allstates"""
    states = storage.all(State)
    return render_template('7-state_list.htmls', states=states)

@app.tearedown_appcontext
def teardown(self):
    """removes thecurrent sqlalchemy"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

