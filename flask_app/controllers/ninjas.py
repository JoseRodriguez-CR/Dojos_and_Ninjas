
from flask import render_template, redirect, request
from flask_app import app
from flask_app.models import dojo, ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('NewNinja.html',dojos= dojo.Dojo.get_all())


@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    print(request.form)
    dojoId = int(request.form["dojo_id"])
    print(dojoId)
    data = {
        "id": dojoId
    }
    print(data)
    return redirect(f'/dojo/{dojoId}')