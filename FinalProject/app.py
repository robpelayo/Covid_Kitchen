"""
A simple food truck flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from covid import Covid
from remove_food import Remove_Food
from remove_state import Remove_State

app = flask.Flask(__name__)  # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET', 'POST'])

app.add_url_rule('/covid/',
                 view_func=Covid.as_view('covid'),
                 methods=['GET', 'POST'])

app.add_url_rule('/remove_food/',
                 view_func=Remove_Food.as_view('remove_food'),
                 methods=['GET', 'POST'])

app.add_url_rule('/remove_state/',
                 view_func=Remove_State.as_view('remove_state'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
