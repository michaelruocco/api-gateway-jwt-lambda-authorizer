import logging
import os
import json

from idv_jwt_auth_handler.idv_jwt_service import IdvJwtService

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handle(event, context):
    secret_key = os.environ['IDV_AUTH_JWT_SECRET_KEY']
    jwt_service = IdvJwtService(secret_key)
    logger.info('received event {}'.format(str(event)))
    body = json.loads(event['body'])
    subject = body['subject']
    seconds_to_live = body.get('secondsToLive', 300)
    logger.info('generating token for subject {} valid for {} seconds'.format(subject, seconds_to_live))
    token = jwt_service.create_expiring_token(subject, seconds_to_live).decode("utf-8")
    return {'statusCode': 200, 'headers':{}, 'body': json.dumps({'token': token})}
