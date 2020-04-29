from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], address=row[1], city=row[2],
                        state=row[3], zip=row[4], hours=row[5],
                        phone=row[6], rating=row[7],pricing=row[8],
                        parking=row[9], review=row[10]) for row in model.select()]
        # entries = [dict(name=row[0], email=row[1], signed_on=row[2], message=row[3] ) for row in model.select()]
        return render_template('index.html',entries=entries)
