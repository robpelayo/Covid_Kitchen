"""
A simple food truck flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from add import Add

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/add/',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
