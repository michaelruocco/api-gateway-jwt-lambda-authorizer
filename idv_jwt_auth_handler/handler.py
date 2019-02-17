import json
import logging
import os

from idv_jwt_auth_handler.idv_lambda_jwt_auth_handler import IdvLambdaJwtAuthHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    secret_key = os.environ['IDV_AUTH_JWT_SECRET_KEY']
    handler = IdvLambdaJwtAuthHandler(secret_key)
    policy_json = handler.handle(event, context)
    return json.loads(policy_json)
