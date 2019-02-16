import jwt
import uuid
import datetime
import logging

from datetime import timedelta


class JwtService:

    def __init__(self, issuer, secret):
        self.logger = logging.getLogger(__name__)
        self.issuer = issuer
        self.secret = secret

    def create_non_expiring_token(self, subject):
        issued_at = datetime.datetime.now()
        payload = self.build_non_expiring_payload(subject, issued_at)
        return self.encode(payload)

    def create_expiring_token(self, subject, seconds_to_live):
        payload = self.build_expiring_payload(subject, seconds_to_live)
        return self.encode(payload)

    def decode(self, token):
        self.logger.info('decoding token {}'.format(token))
        payload = jwt.decode(token, self.secret)
        self.logger.info('decoded token into payload {}'.format(payload))
        return payload

    def build_expiring_payload(self, subject, seconds_to_live):
        issued_at = datetime.datetime.now()
        payload = self.build_non_expiring_payload(subject, issued_at)
        return JwtService.append_expiry(payload, issued_at, seconds_to_live)

    def build_non_expiring_payload(self, subject, issued_at):
        jti = uuid.uuid4()
        payload = {
            'jti': str(jti),
            'iss': self.issuer,
            'sub': subject,
            'iat': issued_at
        }
        return payload

    def encode(self, payload):
        self.logger.info('creating jwt_service token with payload {}'.format(payload))
        token = jwt.encode(payload, self.secret, algorithm='HS256')
        self.logger.info('returning token {}'.format(token))
        return token

    @staticmethod
    def append_expiry(payload, issued_at, seconds_to_live):
        payload['exp'] = issued_at + timedelta(seconds=seconds_to_live)
        return payload
