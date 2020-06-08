from flask import render_template, request, redirect, url_for
from flask.views import MethodView
import gbmodel

class Remove_Food(MethodView):
    def get(self):
        return render_template('remove_food.html')
    def post(self):
        food_to_remove = request.form['food']
        print(food_to_remove)
        model = gbmodel.get_model()
        if model.food_delete(food_to_remove):
            return redirect(url_for('index'))
        else:
            return render_template('error.html')
