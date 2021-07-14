
from flask import request, json, Response, Blueprint
from ..models.personalModel import personalModel, personalSchema
from ..shared.Authentication import Auth

personal_api = Blueprint('personal', __name__)
personal_schema = personalSchema()

@personal_api.route('/', methods=['POST'])
def create():
  """
  Create person Function«
  """
  req_data = request.get_json()
  data, error = personal_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = personalModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  
  user = personalModel(data)
  user.save()

  ser_data = personal_schema.dump(user).data

  token = Auth.generate_token(ser_data.get('id'))

  return custom_response({'jwt_token': token}, 201)

@personal_api.route('/login', methods=['POST'])
def login():
  req_data = request.get_json()

  data, error = personal_schema.load(req_data, partial=True)

  if error:
    return custom_response(error, 400)
  
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  
  user = personalModel.get_user_by_email(data.get('email'))

  if not user:
    return custom_response({'error': 'invalid credentials'}, 400)
  
  if not user.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  
  ser_data = personal_schema.dump(user).data
  
  token = Auth.generate_token(ser_data.get('id'))

  return custom_response({'jwt_token': token}, 200)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )