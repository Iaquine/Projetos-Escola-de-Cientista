from flask_restplus import fields
from service.restplus import api

#entradas do swagger
INPUT_MAIN_SERVICE = api.model(
  'Insert: Age, Experience of the Singer in years, Rank position and Nationality( UK: 0, USA: 1, Others: 2)', {
    'textoMensagem': fields.List(fields.Integer(), required=True, description="Concert to be classified")})
