#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import psycopg2
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
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey, Text
from sqlalchemy.exc import SQLAlchemyError

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
class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    release_date  = db.Column(String(), nullable=False)


    def __init__(self, title, release_date):
        self.title= title
        self.release_date= release_date



class Actors(db.Model):
    __tablename__ = 'actor'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.Integer(), nullable=False)
    gender = db.Column(Text(), nullable=False)

    def __init__(self, name, age, gender):
        self.name= name
        self.age= age
        self.gender= gender

    def details(self):
        return{
        'id':self.id,
        'name':self.name,
        'age':self.age,
        'gender':self.gender
    }
    def update(self):
        db.session.commit()

db.create_all()
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
    data = Movie.query.all();
    return render_template('pages/movies.html', movies=data)


@app.route('/actors')
def actors():
    data = Actors.query.all();
    return render_template('pages/actors.html', actors=data)


#  Create Movie
#  ----------------------------------------------------------------
@app.route('/movies/create', methods=['GET'])
def create_movie_form():
    form = MovieForm()
    return render_template('forms/new_movie.html', form=form)


@app.route('/movies/create', methods=['POST'])
def create_movie_submission():
    try:
        New_movie = Movie(
        title=request.form['title'],
        release_date=request.form['release_date']
        )
        #insert new venue records into the db
        db.session.add(New_movie)
        db.session.commit()

        # on successful db insert, flash success
        flash('Movie ' + request.form['title'] + ' was successfully listed!')
    except SQLAlchemyError as e:
        # TODO: on unsuccessful db insert, flash an error instead
        flash('An error occurred. Movie ' + request.form['title'] + ' could not be listed.')
    return render_template('pages/home.html')

#  Delete Movie
#  ----------------------------------------------------------------

@app.route('/movies/<movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
	try:
		movie = Movie.query.get(movie_id)
		db.session.delete(movie)
		db.session.commit()
	except SQLAlchemyError as e:
		flash('error occur')
	return render_template('pages/home.html')



#  Create Actors
#  ----------------------------------------------------------------

@app.route('/actors/create', methods=['GET'])
def create_actors_form():
		form = ActorsForm()
		return render_template('forms/new_actors.html', form=form)

@app.route('/actors/create', methods=['POST'])
def create_actors_submission():
    try:
        New_actor= Actors(
        name=request.form['name'],
        age=request.form['age'],
        gender=request.form['gender']
        )

        db.session.add(New_actor)
        db.session.commit()


        flash('Actor ' + request.form['name'] + ' was successfully listed!')
    except SQLAlchemyError as e:
        flash('An error occurred. Actor ' + request.form['name'] + ' could not be listed.')
    return render_template('pages/home.html')

#  Delete Actor
#  ----------------------------------------------------------------

@app.route('/actor/<actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
	try:
		actor = Actors.query.get(actor_id)
		db.session.delete(actor)
		db.session.commit()
	except SQLAlchemyError as e:
		flash('error occur')
	return render_template('pages/home.html')

#  Edit Actor
#  ----------------------------------------------------------------
@app.route('/actors/<int:actor_id>/edit', methods=['GET'])
def edit_actor(actor_id):
		form = ActorsForm()
		actor_data = Actors.query.get(actor_id)
		if actor_data:
			actor_details = Actors.details(actor_data)
			form.name.data = actor_details['name']
			form.age.data = actor_details['age']
			form.gender.data = actor_details['gender']

		return render_template('forms/edit_actor.html', form=form, actor=actor_details)

@app.route('/actors/<int:actor_id>/edit', methods=['POST'])
def edit_actor_submission(actor_id):

    form = ActorsForm(request.form)
    actor_data =Actors.query.get(actor_id)

    try:
        setattr(actor_data, 'name', request.form['name'])
        setattr(actor_data, 'gender', request.form['gender'])
        setattr(actor_data, 'age', request.form['age'])

        Actors.update(actor_data)

        # on successful db insert, flash success
        flash('Actor ' + request.form['name'] + ' was successfully updated!')
    except SQLAlchemyError as e:
        # TODO: on unsuccessful db insert, flash an error instead
        flash('An error occurred. Actor ' + request.form['name'] + ' could not be updated.')
    return render_template('pages/home.html')




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
