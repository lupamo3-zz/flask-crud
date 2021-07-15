
from flask import request, json, Response, Blueprint, g
from ..models.personalModel import personalModel, personalSchema
from ..shared.authentication import Auth

personal_api = Blueprint('personal', __name__)
personal_schema = personalSchema()

@personal_api.route('/', methods=['POST'])
def create():
  """
  Create person Function«
  """
  req_data = request.get_json()
  data = personal_schema.load(req_data)

  # check if user already exist in the db
  user_in_db = personalModel.get_user_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User already exist, please supply another email address'}
    return custom_response(message, 400)
  
  user = personalModel(data)
  user.save()

  ser_data = personal_schema.dump(user)

  token = Auth.generate_token(ser_data.get('id'))

  return custom_response({'jwt_token': token}, 201)

@personal_api.route('/', methods=['GET'])
# @Auth.auth_required
def get_all():
  users = personalModel.get_all_students()
  ser_users = personal_schema.dump(users, many=True)
  return custom_response(ser_users, 200)

@personal_api.route('/<int:user_id>', methods=['GET'])
# @Auth.auth_required
def get_a_user(user_id):
  """
  Get a single user
  """
  user = personalModel.get_one_student(user_id)
  if not user:
    return custom_response({'error': 'user not found'}, 404)
  
  ser_user = personal_schema.dump(user)
  return custom_response(ser_user, 200)

@personal_api.route('/me', methods=['PUT'])
# @Auth.auth_required
def update():
  """
  Update me
  """
  req_data = request.get_json()
  data, error = personal_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)

  user = personalModel.get_one_student(g.user.get('id'))
  user.update(data)
  ser_user = personal_schema.dump(user)
  return custom_response(ser_user, 200)

@personal_api.route('/me', methods=['DELETE'])
# @Auth.auth_required
def delete():
  """
  Delete a user
  """
  user = personalModel.get_one_student(g.user.get('id'))
  user.delete()
  return custom_response({'message': 'deleted'}, 204)

@personal_api.route('/me', methods=['GET'])
# @Auth.auth_required
def get_me():
  """
  Get me
  """
  user = personalModel.get_one_student(g.user.get('id'))
  ser_user = personal_schema.dump(user)
  return custom_response(ser_user, 200)

@personal_api.route('/login', methods=['POST'])
def login():
  req_data = request.get_json()
  try:
    data = personal_schema.load(req_data, partial=True)
    print(data)
  except ValidationError as err:
        return custom_response(err, 400)
  
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  
  user = personalModel.get_user_by_email(data.get('email'))

  if not user:
    return custom_response({'error': 'invalid credentials'}, 400)
  
  if not user.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  
  ser_data = personal_schema.dump(user)
  print("show se", ser_data)
  
  # token = '304566'
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