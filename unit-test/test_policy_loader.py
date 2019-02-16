import unittest
import logging

from util.file_content_loader import load_file_content

from policy_loader.policy_loader import PolicyLoader


class PolicyLoaderTest(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.loader = PolicyLoader()

    def test_should_load_deny_all_policy_if_principal_id_unknown(self):
        policy = self.loader.load('unknown', 'arn:aws:execute-api:eu-west-1:327122349051:8tu67utdf7/*/GET/verificationContexts/*')
        expected_policy = load_file_content(__name__, 'policies/expected-unknown-principal-id-policy.json')
        self.assertEqual(expected_policy, policy)


if __name__ == '__main__':
    unittest.main()
