from flask import render_template, request
from flask.views import MethodView
from datetime import date, timedelta
import requests
import json

states = {
        '0': 'alabama',
        '1': 'alaska',
        '2': 'arizona',
        '3': 'arkansas',
        '4': 'california',
        '5': 'colorado',
        '6': 'connecticut',
        '7': 'delaware',
        '8': 'diamond princess',
        '9': 'district of columbia',
        '10': 'florida',
        '11': 'georgia',
        '12': 'grand princess',
        '13': 'guam',
        '14': 'hawaii',
        '15': 'idaho',
        '16': 'illinois',
        '17': 'indiana',
        '18': 'iwoa',
        '19': 'kansas',
        '20': 'kentucky',
        '21': 'louisiana',
        '22': 'maine',
        '23': 'maryland',
        '24': 'massachusetts',
        '25': 'michigan',
        '26': 'minnesota',
        '27': 'mississippi',
        '28': 'missouri',
        '29': 'montana',
        '30': 'nebraska',
        '31': 'nevada',
        '32': 'new hampshire',
        '33': 'new jersey',
        '34': 'new mexico',
        '35': 'new york',
        '36': 'north carolina',
        '37': 'north dakota',
        '38': 'northern mariana islands',
        '39': 'ohio',
        '40': 'oklahoma',
        '41': 'oregon',
        '42': 'pennsylvania',
        '43': 'puerto rico',
        '44': 'rhode island',
        '45': 'south carolina',
        '46': 'south dakota',
        '47': 'tennessee',
        '48': 'texas',
        '49': 'utah',
        '50': 'vermont',
        '51': 'virgin islands',
        '52': 'virginia',
        '53': 'washington',
        '54': 'west Virginia',
        '55': 'wisconsin',
        '56': 'wyoming'
}
class Covid(MethodView):
        def get(self):
                return render_template('covid.html')

        def post(self):
                url = "https://covid-19-data.p.rapidapi.com/report/country/name"
                yesterday = date.today() - timedelta(days=1)
                querystring = {"date-format": "YYYY-MM-DD", "format": "json", "date": yesterday, "name": "USA"}

                headers = {
                        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
                        'x-rapidapi-key': "46668a7331msh0a4505972740a46p1779c5jsn20e20848e83b"
                }
                try:
                        state = request.form['state'].lower()
                        response = requests.request("GET", url, headers=headers, params=querystring)
                        data = json.loads(response.text)
                        position = int(list(states.keys())[list(states.values()).index(state)])
                        state_data = data[0]["provinces"][position]
                        return render_template('index.html', covid_data=state_data)
                except:
                        return render_template('error.html')