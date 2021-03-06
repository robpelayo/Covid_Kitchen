from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Add(MethodView):
    def get(self):
        return render_template('add.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'],
                     request.form['address'],
                     request.form['city'],
                     request.form['state'],
                     request.form['zip'],
                     request.form['hours'],
                     request.form['phone'],
                     request.form['rating'],
                     request.form['pricing'],
                     request.form['parking'],
                     request.form['review'])
        return redirect(url_for('index'))
