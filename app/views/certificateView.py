from flask import request, g, Blueprint, json, Response
from ..shared.authentication import Auth
from ..models.certificateModel import certificateModel, certificateSchema

certificate_api = Blueprint('certificate_api', __name__)
cert_schema = certificateSchema()

MAIL_SERVER : 'localhost'
MAIL_PORT : 25
MAIL_USE_TLS : False
MAIL_USE_SSL : False
MAIL_DEBUG : app.debug
MAIL_USERNAME : None
MAIL_PASSWORD : None
MAIL_DEFAULT_SENDER : None
MAIL_MAX_EMAILS : None
MAIL_SUPPRESS_SEND : app.testing
MAIL_ASCII_ATTACHMENTS : False

@certificate_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create certificate Function
  """
  req_data = request.get_json()
  req_data['owner_id'] = g.user.get('id')
  data = cert_schema.load(req_data)
  post = certificateModel(data)
  post.save()
  data = cert_schema.dump(post)
  return custom_response(data, 201)

@certificate_api.route('/', methods=['GET'])
def get_all():
  """
  Get All certificates
  """
  posts = certificateModel.get_all_certificates()
  data = cert_schema.dump(posts, many=True)
  return custom_response(data, 200)

@certificate_api.route('/<int:certificate_id>', methods=['GET'])
def get_one(certificate_id):
  """
  Get A Blogpost
  """
  post = certificateModel.get_one_certificate(certificate_id) 
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = cert_schema.dump(post)
  return custom_response(data, 200)

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )