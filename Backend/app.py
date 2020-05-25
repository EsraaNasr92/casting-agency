from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
from flask_cors import CORS
from models import setup_db, Actors, Movie



DEFAULT_OFFSET = 1
DEFAULT_LIMIT = 30
# Get a list of paginated questions
def paginate_response(request, selection):
  offset = request.args.get('offset', DEFAULT_OFFSET, type=int)
  limit = request.args.get('limit', DEFAULT_LIMIT, type=int)
  start =  (offset - 1) * limit
  end = start + limit

  formatted_selection = [item.format() for item in selection]
  paginated_selection = formatted_selection[start:end]

  return paginated_selection

def create_app(test_config=None):
  # Create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.route('/')
  def index():
    return jsonify ({'message': 'Hello'})

  """
  GET Movies and Actors
  """

  @app.route('/actors')
  def get_actors():
    try:
      return jsonify({
        'success': True,
        'actors': paginate_response(request, Actors.query.order_by(Actors.id).all())
        })
    except:
      abort(422)



  @app.route('/movies')
  def get_movies():
    return jsonify({
      'success': True,
      'movies': paginate_response(request, Movie.query.order_by(Movie.id).all())
    })

  """
  DELETE Movie and actor functions
  """

  @app.route('/movies/<movie_id>', methods=['DELETE'])
  def delete_movie(movie_id):
    movie = Movie.query.get(movie_id)

    if movie is None:
      abort(404)

    movie.delete()

    return jsonify({
      'success': True,
      'delete': movie_id
    })


  @app.route('/actors/<actor_id>', methods=['DELETE'])
  def delete_actor(actor_id):
    actor = Actor.query.get(actor_id)

    if actor is None:
      abort(404)

    actor.delete()

    return jsonify({
      'success': True,
      'delete': actor_id
    })


    """
    POST new movie and actor
    """
  @app.route('/actors', methods=['POST'])
  def add_new_actor():
    name = request.get_json().get('name')
    age = request.get_json().get('age')
    gender = request.get_json().get('gender')

    try:
      data = name and age
      if not data:
        abort(400)
    except (TypeError, KeyError):
      abort(400)

    try:
      new_actor = Actors(name=name, age=age, gender=gender).insert()
      return jsonify({
        'success': True,
        'actors': name
      }), 200
    except:
      abort(422)

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
      new_movie = Movie(title=title, release_date=release_date).insert()
      return jsonify({
        'success': True,
        'movie': title
      }), 200
    except:
      abort(422)



  @app.route('/actors/<actor_id>', methods=['PATCH'])
  def update_actor(actor_id):
    actor = Actors.query.get(actor_id)

    # Abort 404 if the actor was not found
    if actor is None:
      abort(404)

    body = request.json
    name = body.get('name', None)
    age = body.get('age', None)
    gender = body.get('gender', None)

    # Abort 400 if any fields are missing
    if any(arg is None for arg in [name, age, gender]) or '' in [name, age, gender]:
      abort(400, 'name, age and gender are required fields.')

    # Update the actor with the requested fields
    actor.name = name
    actor.age = age
    actor.gender = gender
    actor.update()

    # Return the updated actor
    return jsonify({
      'success': True,
      'actors': [Actors.query.get(actor_id).format()]
    })



  @app.route('/movies/<movie_id>', methods=['PATCH'])
  def update_movie(movie_id):
    movie = Movie.query.get(movie_id)

    # Abort 404 if the movie was not found
    if movie is None:
      abort(404)

    body = request.json
    title = body.get('title', None)
    release_date = body.get('release_date', None)

    # Abort 400 if any fields are missing
    if any(arg is None for arg in [title, release_date]) or '' in [title, release_date]:
      abort(400, 'title and release_date are required fields.')

    # Update the movie with the requested fields
    movie.title = title
    movie.release_date = release_date
    movie.update()

    # Return the updated movie
    return jsonify({
      'success': True,
      'movies': [Movie.query.get(movie_id).format()]
    })







 #----------------------------------------------------------------------------#
  # Error Handling.
  #----------------------------------------------------------------------------#
  # Unprocessable Entity
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False,
      "error": 422,
      "message": "Unable to process your request. Please try again later."
    }), 422

  # Not Found
  @app.errorhandler(404)
  def not_found_error(error):
    return jsonify({
      "success": False,
      "error": 404,
      "message": "Resource not found."
    }), 404

  # Bad Request
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "error": 400,
      "message": str(error)
    }), 400


  return app

app = create_app()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
