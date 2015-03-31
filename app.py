# coding: utf-8

import os
from models import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask import (
    Flask, request, current_app, send_from_directory, render_template,
    jsonify, escape, url_for
)

app = Flask("bookstore")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:admin@localhost/bookstore"
db = SQLAlchemy(app)


@app.route("/")
def hello_world():
    return render_template('index.html', user_name='Convidado')


@app.route("/<name>")
def index(name):
    if name.lower() == 'gilmar' or name.lower() == 'test':
        return render_template('index.html', user_name=name)

    return "Not Found", 404


@app.route("/usuarios")
def users():
    return render_template('usuarios.html', users=User.query.all())

    return "Not Found", 404

@app.route("/<clientes>/json")
def json_api():
    clients = [
        {name: 'Gilmar Soares'},
        {name: 'Mari Agusta'},
        {name: 'Christian Soares'},
        {name: 'Fernanda Soares'}
    ]

    return jsonify(clients=clients, total=len(clients))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
