from flask import request, g, Blueprint, json, Response
from ..shared.authentication import Auth
from ..models.certificateModel import certificateModel, certificateSchema

certificate_api = Blueprint('certificate_api', __name__)
cert_schema = certificateSchema()

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
  data = cert_schema.dump(post).data
  return custom_response(data, 201)


def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )