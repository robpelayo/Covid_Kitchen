from flask import render_template, request
from flask.views import MethodView
import json
import requests

class Food(MethodView):
    def get(self):
        url = "https://edamam-food-and-grocery-database.p.rapidapi.com/parser"

        querystring = {"ingr":"apple"}

        headers = {
            'x-rapidapi-host': "edamam-food-and-grocery-database.p.rapidapi.com",
            'x-rapidapi-key': "46668a7331msh0a4505972740a46p1779c5jsn20e20848e83b"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = response.json()

        print(json.dumps(data["hints"][0]['food'], indent=2))
        # ENERC_KCAL - KCALS
        # PROCNT - PROTEIN
        # FAT
        # CHOCDF - CARBS
        # FIBTG - FIBER
        return render_template('index.html', covid_data=None)
