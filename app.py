# coding: utf-8

import os
from werkzeug import secure_filename
from flask import (
    Flask, request, current_app, send_from_directory, render_template,
    jsonify, escape, url_for
)

app = Flask("bookstore")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')


@app.route("/")
def hello_world():
    return '<h1>Bem vindo à Biblioteca digital</h1>', 200


@app.route("/<name>")
def index(name):
    if name.lower() == 'gilmar' or name.lower() == 'test':
        return render_template('index.html', user_name=name)

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
