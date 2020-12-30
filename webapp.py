#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:20:38 2020

@authors: josecarlos
"""

from flask import Flask, render_template, redirect, url_for
from forms import SearchForm
import requests
import json
import unicodedata
from datetime import date
import secrets

secret_key = secrets.token_hex(16)

app = Flask(__name__)
app.config['SECRET_KEY'] = secret_key
date2 = date.today()
# date2='2020-12-27'

@app.route('/', methods=['GET', 'POST'])
def home():
    global date2

    form = SearchForm()
    if form.validate_on_submit():
        date2 = date.today()
        return redirect(url_for('search', name=form.username.data))

    return render_template('search.html', form=form)

@app.route('/search/<name>')
def search(name):
    global date2

    info = requests.get('https://api.covid19tracking.narrativa.com/api/'+ str(date2) + '/country/spain/region/'+ name)
    info = unicodedata.normalize('NFKD', info.text).encode('ascii','ignore')
    info = json.loads(info)
    info = info['dates'][str(date2)]['countries']['Spain']['regions'][0]
    return render_template('show.html', info=info)

@app.route('/info')
def info():

    return render_template('info.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1234)
