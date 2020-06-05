import unittest
import json
from trackbasket_be.models.basemodel import db
from trackbasket_be.models.volunteer import Volunteer
from trackbasket_be.app import app

class TestVolunteer(unittest.TestCase):

    def setUp(self):
      self.test_app = app.test_client()
      self.volunteer = Volunteer(name='volunteer1', volunteer_id='1234', phone_number='(234) 543-5647')

    def test_volunteer(self):
      self.assertEqual(self.volunteer.name, 'volunteer1')
      self.assertEqual(self.volunteer.volunteer_id, '1234')
      self.assertEqual(self.volunteer.phone_number, '(234) 543-5647')

    def test_create_volunteer(self):
      response = self.test_app.post('/volunteer/1234', json={'name': 'volunteer1', 'phone_number': '(234) 543-5647'})
      self.assertEqual(response.status_code, 201)
      
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['id'], '1234')
      self.assertEqual(payload['data']['attributes']['name'], 'volunteer1')
      self.assertEqual(payload['data']['attributes']['phone number'], '(234) 543-5647')
    
      response = self.test_app.post('/volunteer/1234', json={'name': 'volunteer1', 'phone_number': '(234) 543-5647'})
      self.assertEqual(response.status_code, 400)
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['error'], 'Volunteer already exists')
      self.test_app.delete('/volunteer/1234')

    def test_read_volunteer(self):
      with app.app_context():
        db.session.add(self.volunteer)
        db.session.commit()

      response = self.test_app.get('/volunteer/4321')
      self.assertEqual(response.status_code, 400)
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['error'], 'Volunteer not found')

      response = self.test_app.get('/volunteer/1234')
      self.assertEqual(response.status_code, 200)
      payload = json.loads(response.data)
      
      self.assertEqual(payload['data']['attributes']['id'], '1234')
      self.assertEqual(payload['data']['attributes']['name'], 'volunteer1')
      self.assertEqual(payload['data']['attributes']['phone number'], '(234) 543-5647')
      with app.app_context():
        db.session.delete(self.volunteer)
        db.session.commit()

    def test_update_volunteer(self):
      with app.app_context():
        db.session.add(self.volunteer)
        db.session.commit()

      response = self.test_app.patch('/volunteer/1234', json={'name': 'new volunteer', 'phone_number': '(434) 721-8739'})
      self.assertEqual(response.status_code, 200)
      
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['id'], '1234')
      self.assertEqual(payload['data']['attributes']['name'], 'new volunteer')
      self.assertEqual(payload['data']['attributes']['phone number'], '(434) 721-8739')
    
      response = self.test_app.patch('/volunteer/4321', json={'name': 'new volunteer', 'phone_number': '(434) 721-8739'})
      self.assertEqual(response.status_code, 400)
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['error'], 'Volunteer not found')
      db.session.delete(self.volunteer)
      db.session.commit()

    def test_delete_volunteer(self):
      with app.app_context():
        db.session.add(self.volunteer)
        db.session.commit()
      response = self.test_app.delete('/volunteer/1234')
      self.assertEqual(response.status_code, 200)
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['message'], 'volunteer with id 1234 successfully deleted')

      response = self.test_app.delete('/volunteer/4321')
      self.assertEqual(response.status_code, 400)
      payload = json.loads(response.data)
      self.assertEqual(payload['data']['attributes']['error'], 'volunteer does not exist')

if __name__ == '__main__':
    unittest.main()