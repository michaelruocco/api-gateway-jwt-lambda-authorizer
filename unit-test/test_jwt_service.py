import unittest
import uuid
import logging

from jwt_auth_handler.jwt_service import JwtService
from jwt import ExpiredSignatureError
from mock import patch
from freezegun import freeze_time
from unittest import TestCase


@freeze_time("2012-02-16")
class JwtServiceTest(TestCase):

    SECRET_KEY = 'my-secret'

    ISSUER = 'my-issuer'
    SUBJECT = 'my-subject'
    UUID = uuid.UUID('06335e84-2872-4914-8c5d-3ed07d2a2f16')

    EXPIRING_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAs' \
                     'Imp0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3QiL' \
                     'CJleHAiOjEzMjkzNTA0NjB9.XitpF0TSkrD0l1xtSg7CrLx0Jno43JACRP5HA35N9Lw'
    NON_EXPIRING_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAs' \
                         'Imp0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3Qif' \
                         'Q.0INZqTk20CFh6rbuFXcI1iy5OEVeFWQnCC21r5JXqos'

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.service = JwtService(JwtServiceTest.SECRET_KEY, JwtServiceTest.ISSUER)

    def test_should_generate_jwt_non_expiring_token(self):
        with patch('uuid.uuid4', return_value=JwtServiceTest.UUID):
            token = self.service.create_non_expiring_token(JwtServiceTest.SUBJECT)

            self.assertEqual(JwtServiceTest.NON_EXPIRING_TOKEN, token)

    def test_should_generate_jwt_expiring_token(self):
        with patch('uuid.uuid4', return_value=JwtServiceTest.UUID):
            seconds_to_live = 60

            token = self.service.create_expiring_token(JwtServiceTest.SUBJECT, seconds_to_live)

            self.assertEqual(JwtServiceTest.EXPIRING_TOKEN, token)

    def test_should_decode_non_expiring_token(self):
        with patch('uuid.uuid4', return_value=JwtServiceTest.UUID):
            payload = self.service.decode(JwtServiceTest.NON_EXPIRING_TOKEN)

            self.assertEqual(JwtServiceTest.expected_non_expiring_token_payload(), payload)

    def test_should_decode_expiring_token(self):
        with patch('uuid.uuid4', return_value=JwtServiceTest.UUID):
            payload = self.service.decode(JwtServiceTest.EXPIRING_TOKEN)

            self.assertEqual(JwtServiceTest.expected_expiring_token_payload(), payload)

    def test_should_return_error_if_token_expired_token(self):
        with patch('uuid.uuid4', return_value=JwtServiceTest.UUID):
            expired_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAsIm' \
                            'p0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3QiLCJle' \
                            'HAiOjEzMjkzNTAzNDB9.6RzKiz81ltH0zpYDs-NjoySji7Rz7e1XilwHwda6Otk'

            self.assertRaises(ExpiredSignatureError, self.service.decode, expired_token)

    @staticmethod
    def expected_non_expiring_token_payload():
        return {
            'jti': str(JwtServiceTest.UUID),
            'iss': JwtServiceTest.ISSUER,
            'sub': JwtServiceTest.SUBJECT,
            'iat': 1329350400
        }

    @staticmethod
    def expected_expiring_token_payload():
        payload = JwtServiceTest.expected_non_expiring_token_payload()
        payload['exp'] = 1329350460
        return payload


if __name__ == '__main__':
    unittest.main()
