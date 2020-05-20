#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
import psycopg2
import json
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from forms import *
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey, Text
from sqlalchemy.exc import SQLAlchemyError
from flask_cors import CORS

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
CORS(app)
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

    def details(self):
        return{
        'id':self.id,
        'title':self.title,
        'release_date':self.release_date,
    }
    def update(self):
        db.session.commit()

    def format(self):
        return {
        'id': self.id,
        'title': self.title,
        'release_date': self.release_date,
    }
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    def insert(self):
        db.session.add(self)
        db.session.commit()

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

    def format(self):
        return {
        'id': self.id,
        'name': self.name,
        'age':self.age,
        'gender': self.gender
    }
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def insert(self):
        db.session.add(self)
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
    try:
        movies = Movie.query.all()
        movies = [movie.format() for movie in movies]
        return jsonify({
            'success': True,
            'movies': movies
        })
    except:
        abort(422)



@app.route('/actors')
def actors():
    try:
        actors = Actors.query.all()
        actors = [actor.format() for actor in actors]
        return jsonify({
            'success': True,
            'actors': actors
        })
    except:
        abort(422)


#  Create Movie
#  ----------------------------------------------------------------
@app.route('/movies/create', methods=['GET'])
def create_movie_form():
    form = MovieForm()
    return render_template('forms/new_movie.html', form=form)


@app.route('/movies', methods=['POST'])
def add_new_movie():
    title = request.get_json().get('title')
    release_date = request.get_json().get('release_date')
    try:
        data = title and release_date
        if not data:
            abort(400)
    except (TypeError, KeyError):
        abort(400)

    try:
        Movie(title=title, release_date=release_date).insert()
        return jsonify({
            'success': True,
            'movie': title
        }), 201
    except:
        abort(422)

# Update Movies
# -----------------------------------------------------------------

@app.route('/movies/<int:movie_id>', methods=['PATCH'])
def update_movie(movie_id):
    title = request.get_json().get('title')
    release_date = request.get_json().get('release_date')


    try:
        data = title or release_date
        if not data:
            abort(400)
    except (TypeError, KeyError):
        abort(400)


    movie = Movie.query.filter_by(id=movie_id).first()
    if not movie:
        abort(404)


    try:
        if title:
            movie.title = title
        if release_date:
            movie.release_date = release_date
        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200
    except Exception:
        abort(422)

#  Delete Movie
#  ----------------------------------------------------------------

@app.route('/movies/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = Movie.query.filter_by(id=movie_id).first()
    if not movie:
        abort(404)

    try:
        movie.delete()
        return jsonify({
            'success': True,
            'delete': movie_id
        }), 200
    except Exception:
        abort(422)

#  Edit Movie
#  ----------------------------------------------------------------
@app.route('/movies/<int:movie_id>/edit', methods=['GET'])
def edit_movie(movie_id):
		form = MovieForm()
		movie_data = Movie.query.get(movie_id)
		if movie_data:
			movie_details = Movie.details(movie_data)
			form.title.data = movie_details['title']
			form.release_date.data = movie_details['release_date']

		return render_template('forms/edit_movie.html', form=form, movie=movie_details)

@app.route('/movies/<int:movie_id>/edit', methods=['POST'])
def edit_movie_submission(movie_id):

    form = MovieForm(request.form)
    movie_data =Movie.query.get(movie_id)

    try:
        setattr(movie_data, 'title', request.form['title'])
        setattr(movie_data, 'release_date', request.form['release_date'])

        Movie.update(movie_data)

        flash('Movie ' + request.form['title'] + ' was successfully updated!')
    except SQLAlchemyError as e:

        flash('An error occurred. Movie ' + request.form['title'] + ' could not be updated.')
    return render_template('pages/home.html')

#  Create Actors
#  ----------------------------------------------------------------

@app.route('/actors/create', methods=['GET'])
def create_actors_form():
		form = ActorsForm()
		return render_template('forms/new_actors.html', form=form)

@app.route('/actors', methods=['POST'])
def add_actor():
    name = request.get_json().get('name')
    gender = request.get_json().get('gender')
    age = request.get_json().get('age')
    try:
        data = name and gender and age
        if not data:
            abort(400)
    except (TypeError, KeyError):
        abort(400)

    try:
        Actors(name=name, gender=gender, age=age).insert()
        return jsonify({
            'success': True,
            'actor': name
        }), 201
    except:
        abort(422)

#  Delete Actor
#  ----------------------------------------------------------------

@app.route('/actors/<int:actor_id>', methods=['DELETE'])
def delete_actor(actor_id):
    actor = Actor.query.filter_by(id=actor_id).first()
    if not actor:
        abort(404)

    try:
        actor.delete()
        return jsonify({
            'success': True,
            'delete': actor_id
        }), 200
    except Exception:
        abort(422)

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

# Update Actors
#---------------------------------------------------------------------------
@app.route('/actors/<int:actor_id>', methods=['PATCH'])
def update_actor(actor_id):
    name = request.get_json().get('name')
    age = request.get_json().get('age')
    gender = request.get_json().get('gender')

    try:
        data = name or gender or age
        if not data:
            abort(400)
    except (TypeError, KeyError):
        abort(400)


    actor = Actors.query.filter_by(id=actor_id).first()
    if not actor:
        abort(404)

    # update
    try:
        if name:
            actor.name = name
        if gender:
            actor.gender = gender
        if age:
            actor.age = age
        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200
    except Exception:
        abort(422)

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422
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
