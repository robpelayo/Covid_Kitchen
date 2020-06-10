from flask import render_template, request, redirect, url_for
from flask.views import MethodView
import gbmodel


class Remove_State(MethodView):
    def get(self):
        return render_template('remove_state.html')

    def post(self):
        state_to_remove = request.form['state'].title()
        model = gbmodel.get_model()
        if model.delete(state_to_remove):
            return redirect(url_for('index'))
        else:
            return render_template('error.html')
