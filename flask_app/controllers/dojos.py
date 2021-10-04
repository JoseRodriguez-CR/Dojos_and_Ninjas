from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route( '/' )
def dojos():
    dojos = Dojo.get_all()
    return render_template("Dojos.html", dojos=dojos)

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    #print(dojo=Dojo.one_dojo_with_ninjas(data))
    return render_template('DojoShow.html', dojo=Dojo.one_dojo_with_ninjas(data))