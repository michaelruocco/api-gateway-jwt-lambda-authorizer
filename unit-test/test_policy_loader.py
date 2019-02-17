import unittest
import logging

from file_content_loader.file_content_loader import load_file_content
from jwt_auth_handler.policy_loader import PolicyLoader


class PolicyLoaderTest(unittest.TestCase):

    DEFAULT_POLICY_KEY = 'deny-all'
    METHOD_ARN = 'arn:aws:execute-api:eu-west-1:327122349051:8tu67utdf7/*/GET/verificationContexts/*'

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        policies = PolicyLoaderTest.build_policies( PolicyLoaderTest.DEFAULT_POLICY_KEY)
        self.loader = PolicyLoader(policies, PolicyLoaderTest.DEFAULT_POLICY_KEY)

    def test_should_load_deny_all_policy_if_principal_id_unknown(self):
        expected_policy = load_file_content(__name__, 'expected_policies/expected-unknown-principal-id-policy.json')

        policy = self.loader.load('unknown', PolicyLoaderTest.METHOD_ARN)

        self.assertEqual(expected_policy, policy)

    def test_should_load_allow_all_policy_for_allow_all_principal_id(self):
        expected_policy = load_file_content(__name__, 'expected_policies/expected-allow-all-policy.json')

        policy = self.loader.load('allow-all', PolicyLoaderTest.METHOD_ARN)

        self.assertEqual(expected_policy, policy)

    def test_should_load_get_only_policy_for_get_only_principal_id(self):
        expected_policy = load_file_content(__name__, 'expected_policies/expected-get-only-policy.json')

        policy = self.loader.load('get-only', PolicyLoaderTest.METHOD_ARN)

        self.assertEqual(expected_policy, policy)

    @staticmethod
    def build_policies(default_policy_key):
        return {
            default_policy_key: load_file_content(__name__, 'policy_templates/deny-all-policy-template.json'),
            'allow-all': load_file_content(__name__, 'policy_templates/allow-all-policy-template.json'),
            'get-only': load_file_content(__name__, 'policy_templates/get-only-policy-template.json'),
        }


if __name__ == '__main__':
    unittest.main()
