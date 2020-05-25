import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movie



class CastingAgencyTestCase(unittest.TestCase):
  """This class represents the Casting Agency test case"""

  def setUp(self):
    """Define test variables and initialize app."""
    self.app = create_app()
    self.client = self.app.test_client
    self.database_name = "postgres"
    self.database_path = "postgres://{}/{}".format('postgres:123456@localhost:5432', self.database_name)
    setup_db(self.app, self.database_path)



    # binds the app to the current context
    with self.app.app_context():
      self.db = SQLAlchemy()
      self.db.init_app(self.app)
      # create all tables
      self.db.create_all()


    self.new_movie = {
      'title': 'Avengers 2',
      'release_date': '2021-10-1 04:22'
    }
    self.new_actor = {
      'name': 'John Doe',
      'age': 20,
      'gender': 'Male'
    }

    self.update_movie = {
      'title': 'Toy Story 12',
      'release_date': '2021-10-1 04:22'
    }


  def tearDown(self):
    """Executed after reach test"""
    pass


  def test_get_actors (self):
    res = self.client().get('/actors')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertTrue(len(data['actors']) >= 0)

  def test_get_movies (self):
    res = self.client().get('/movies')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertTrue(data['success'])
    self.assertTrue(len(data['movies']) >= 0)



  def test_create_movies (self):
    res = self.client().post('/movies', json=self.new_movie)
    data = json.loads(res.data)

    self.assertTrue(data['success'])
    #self.assertTrue(len(data['movies']) == 13)

  def test_create_actors (self):
    res = self.client().post('/actors', json=self.new_actor)
    data = json.loads(res.data)

    self.assertTrue(data['success'])
    #self.assertTrue(len(data['actors']) == 1)


  def test_update_movies (self):
    #self.client().post('/movies', json=self.new_movie)
    res = self.client().patch('/movies/22', json=self.update_movie)
    data = json.loads(res.data)

    self.assertTrue(data['success'])
    #self.assertTrue(len(data['movies']) == 22)





  def test_delete_actors (self):
    self.client().post('/actors', json=self.new_actor)
    
    res = self.client().delete('/actors/22')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['delete'], '22')
    self.assertTrue(data['success'])

  def test_delete_movies (self):
    self.client().post('/movies', json=self.new_movie)
    res = self.client().delete('/movies/32')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 200)
    self.assertEqual(data['delete'], '32')
    self.assertTrue(data['success'])



  #  ----------------------------------------------------------------
  #  Error behavior tests
  #  ----------------------------------------------------------------

  def test_401_get_actors (self):
    res = self.client().get('/actors')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])

  def test_401_get_movies (self):
    res = self.client().get('/movies')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])
  
  def test_401_create_actors (self):
    res = self.client().post('/actors', json=self.new_actor)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])

  def test_401_create_movies (self):
    res = self.client().post('/movies', json=self.new_movie)
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 401)
    self.assertFalse(data['success'])

  def test_404_update_actors (self):
    res = self.client().patch('/actors/1000')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])

  def test_404_update_movies (self):
    res = self.client().patch('/movies/1000')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])
  
  def test_404_delete_actors (self):
    res = self.client().delete('/actors/1000')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])
  
  def test_404_delete_movies (self):
    res = self.client().delete('/movies/1000')
    data = json.loads(res.data)

    self.assertEqual(res.status_code, 404)
    self.assertFalse(data['success'])





# Make the tests conveniently executable
if __name__ == "__main__":
  unittest.main()