import unittest
import logging

from mock import MagicMock
from file_content_loader.file_content_loader import load_file_content
from jwt_auth_handler.lambda_jwt_auth_handler import LambdaJwtAuthHandler


class LambdaJwtAuthHandlerTest(unittest.TestCase):

    TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJteS1pc3N1ZXIiLCJpYXQiOjEzMjkzNTA0MDAsIm' \
            'p0aSI6IjA2MzM1ZTg0LTI4NzItNDkxNC04YzVkLTNlZDA3ZDJhMmYxNiIsInN1YiI6Im15LXN1YmplY3QifQ.0I' \
            'NZqTk20CFh6rbuFXcI1iy5OEVeFWQnCC21r5JXqo'
    METHOD_ARN = 'arn:aws:execute-api:eu-west-1:327122349051:8tu67utdf7/*/GET/verificationContexts/*'

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_should_load_deny_all_policy_if_principal_id_unknown(self):
        expected_policy = load_file_content(__name__, 'expected_policies/expected-allow-all-policy.json')
        mock_jwt_service = LambdaJwtAuthHandlerTest.mock_decoded_token_is_valid()
        mock_policy_loader = LambdaJwtAuthHandlerTest.mock_policy_returned(expected_policy)
        handler = LambdaJwtAuthHandler(mock_jwt_service, mock_policy_loader)
        event = self.build_event(LambdaJwtAuthHandlerTest.TOKEN, LambdaJwtAuthHandlerTest.METHOD_ARN)

        policy = handler.handle(event, None)

        self.assertEqual(expected_policy, policy)

    @staticmethod
    def mock_decoded_token_is_valid():
        valid_decoded_token = {
            'jti': '06335e84-2872-4914-8c5d-3ed07d2a2f16',
            'iss': 'my-issuer',
            'sub': 'my-subject',
            'iat': 1329350400
        }
        mock_decode = MagicMock(return_value=valid_decoded_token)
        mock_jwt_service = MagicMock(return_value=mock_decode)
        mock_jwt_service.decode = mock_decode
        return mock_jwt_service

    @staticmethod
    def mock_policy_returned(policy):
        mock_load = MagicMock(return_value=policy)
        mock_policy_loader = MagicMock(return_value=mock_load)
        mock_policy_loader.load = mock_load
        return mock_policy_loader

    @staticmethod
    def build_event(authorization_token, method_arn):
        return {
            'authorizationToken': authorization_token,
            'methodArn': method_arn
        }
