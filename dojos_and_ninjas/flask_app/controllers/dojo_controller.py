import dataclasses

from flask_app import app

from flask import render_template, redirect, request
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo

@app.route('/')          
def index():
    return redirect('/dojos')
# just to be safe, always set this to redirect to home page(next route)

@app.route('/dojos')
# dojos is browser name (home page) this is the extension that a lot of routes will redirect to
def dojo():
    return render_template('index.html', dojos = Dojo.get_all())
    # get_all is linked to 

@app.route('/create', methods=['POST'])
def create():
    Dojo.create(request.form)
    print(request.form)
    return redirect('/dojos')

@app.route('/dojo_show/<int:id>')
def show(id):
    return render_template('new_ninja.html', dojos = Dojo.show(id))