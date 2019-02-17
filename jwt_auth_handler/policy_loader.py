import logging

from jwt_auth_handler.arn import Arn


class PolicyLoader:

    def __init__(self, policies, default_policy_key):
        self.logger = logging.getLogger(__name__)
        self.policies = policies
        self.default_policy_key = default_policy_key

    def load(self, principal_id, arn_value):
        self.logger.info('loading policy for principal id {}'.format(principal_id))
        template = self.load_template(principal_id)
        self.logger.info('loaded policy template {}'.format(template))
        policy = PolicyLoader.apply(principal_id, arn_value, template)
        self.logger.info('returning populated policy {}'.format(policy))
        return policy

    def load_template(self, principal_id):
        if principal_id in self.policies:
            return self.policies[principal_id]
        return self.policies[self.default_policy_key]

    @staticmethod
    def apply(principal_id, arn_value, template):
        arn = Arn(arn_value)
        return template\
            .replace('%PRINCIPAL_ID%', principal_id)\
            .replace('%REGION%', arn.region)\
            .replace('%ACCOUNT_ID%', arn.account_id)\
            .replace('%API_ID%', arn.api_id)\
            .replace('%STAGE%', arn.stage)
