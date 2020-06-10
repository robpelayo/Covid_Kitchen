from flask import render_template, redirect, url_for, request
from flask.views import MethodView
import gbmodel
import requests
import json
import os

food_api_key = os.environ['FOOD_KEY']


class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        state_entries = [dict(state=row[0], confirmed=row[1], deaths=row[2], active=row[3]) for row in model.select()]
        food_entries = [dict(name=row[0], calories=row[1], protein=row[2], fat=row[3], carbs=row[4], fiber=row[5]) for
                        row in model.food_select()]
        print(len(food_entries))
        calSum = 0
        proteinSum = 0
        fatSum = 0
        carbSum = 0
        fiberSum = 0
        for x in range(len(food_entries)):
            calSum += food_entries[x]['calories']
            proteinSum += food_entries[x]['protein']
            fatSum += food_entries[x]['fat']
            carbSum += food_entries[x]['carbs']
            fiberSum += food_entries[x]['fiber']
        food_totals = dict(calories=calSum, protein=proteinSum, fat=fatSum, carbs=carbSum, fiber=fiberSum)
        return render_template('index.html', entries=state_entries, fentries=food_entries, food_totals=food_totals)

    def post(self):
        url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"
        food = request.form['food']
        querystring = {"ingr": food}

        headers = {
            'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com",
            'x-rapidapi-key': food_api_key
        }
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            data = response.json()
            food_data = data["hints"][0]['food']
            model = gbmodel.get_model()
            model.food_insert(food_data['label'],
                              int(food_data['nutrients']['ENERC_KCAL']),
                              int(food_data['nutrients']['PROCNT']),
                              int(food_data['nutrients']['FAT']),
                              int(food_data['nutrients']['CHOCDF']),
                              int(food_data['nutrients']['FIBTG']))
            return redirect(url_for('index'))
        except:
            return render_template('error.html')
