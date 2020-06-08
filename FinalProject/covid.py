from flask import render_template, request, redirect, url_for
from flask.views import MethodView
from datetime import date, timedelta
import gbmodel
import requests
import json
import os

covid_api_key = os.environ['COVID_KEY']

# state dictionary to track where in the JSON the state is
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
        '54': 'west virginia',
        '55': 'wisconsin',
        '56': 'wyoming'
}


class Covid(MethodView):
        def get(self):
                """
                Serve the page
                :return: covid.html
                """
                return render_template('covid.html')

        def post(self):
                """
                Uses API to get COVID data as of 2 days ago and enters into database
                :return: redirect to index page
                :exception: raises error on state not being in list and out of index error (wrong date or
                            data not returned from API
                """
                url = "https://covid-19-data.p.rapidapi.com/report/country/name"

                # Get the date
                today = date.today()
                yesterday = today - timedelta(2)
                querystring = {"date-format": "YYYY-MM-DD", "format": "json", "date": yesterday, "name": "USA"}

                headers = {
                        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
                        'x-rapidapi-key': covid_api_key
                }
                try:
                        state = request.form['state'].lower()
                        response = requests.request("GET", url, headers=headers, params=querystring)
                        # turn data into JSON
                        data = json.loads(response.text)
                        # Find the state in the dictionary
                        position = int(list(states.keys())[list(states.values()).index(state)])
                        # Hone in on the specific state
                        state_data = data[0]["provinces"][position]
                        # Add to database
                        model = gbmodel.get_model()
                        model.insert(str(state_data['province']),
                                     str(state_data['confirmed']),
                                     str(state_data['deaths']),
                                     str(state_data['active'])
                                     )
                        return redirect(url_for('index'))
                except IndexError:
                        # If we attempt to get to the state but there is no data yet for that day
                        return render_template('error.html')
                except:
                        # User most likely entered incorrect state (not in the state list)
                        return render_template('state_error.html')
