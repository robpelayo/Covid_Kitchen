"""
A simple food truck flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from covid import Covid
from food import Food


app = flask.Flask(__name__)  # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=['GET'])

app.add_url_rule('/covid/',
                 view_func=Covid.as_view('covid'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
