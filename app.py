#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)

# TODO: connect to a local postgresql database

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')


@app.route('/movies')
def movies():
    return render_template('pages/movies.html')


@app.route('/actors')
def actors():
    return render_template('pages/actors.html')


#  Create Movie
#  ----------------------------------------------------------------
@app.route('/movies/create', methods=['GET'])
def create_movie_form():
    form = MovieForm()
    return render_template('forms/new_movie.html', form=form)


@app.route('/movies/create', methods=['POST'])
def create_movie_submission():
    return "create movie"


#  Create Actors
#  ----------------------------------------------------------------

@app.route('/actors/create', methods=['GET'])
def create_actors_form():
		form = ActorsForm()
		return render_template('forms/new_actors.html', form=form)

@app.route('/actors/create', methods=['POST'])
def create_actors_submission():
        return "Create Actor"
#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
