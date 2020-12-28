#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 18:11:33 2020

@author: josecarlos
"""

from wtforms import StringField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length

class SearchForm(FlaskForm):
    username = StringField('COMUNIDAD AUTÓNOMA:', validators=[DataRequired(), Length(min=2, max =50)])
    submit = SubmitField('Buscar')

