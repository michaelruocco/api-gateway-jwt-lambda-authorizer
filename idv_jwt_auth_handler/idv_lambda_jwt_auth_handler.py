import os

from idv_jwt_auth_handler.idv_jwt_service import IdvJwtService
from idv_jwt_auth_handler.idv_policy_loader import IdvPolicyLoader
from jwt_auth_handler.lambda_jwt_auth_handler import LambdaJwtAuthHandler


class IdvLambdaJwtAuthHandler(LambdaJwtAuthHandler):

    def __init__(self, secret_key):
        LambdaJwtAuthHandler.__init__(self, IdvJwtService(secret_key), IdvPolicyLoader())
