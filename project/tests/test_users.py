import json

def test_add_user(test_app, test_database):
  client = test_app.test_client()
  resp = client.post(
    '/users',
    data=json.dumps({
      'username':'Kevin',
      'email': 'kevin@example.com'
    }),
    content_type='application/json',
  )

  data = json.loads(resp.data.decode())
  assert resp.status_code == 201
  assert 'kevin@example.com was added!' in data['message']