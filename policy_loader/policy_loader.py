import logging

from arn import Arn
from util.file_content_loader import load_file_content


class PolicyLoader:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.policies = {
            'deny-all': load_file_content(__name__, 'policies/deny-all-policy.json')
        }

    def load(self, principal_id, arn_value):
        template = self.load_template(principal_id)
        self.logger.info('loaded template {} for principal id {}'.format(template, principal_id))
        policy = PolicyLoader.apply(principal_id, arn_value, template)
        self.logger.info('returning populated policy {}'.format(policy))
        return policy

    def load_template(self, principal_id):
        if principal_id in self.policies:
            return self.policies[principal_id]
        return self.policies['deny-all']

    @staticmethod
    def apply(principal_id, arn_value, template):
        arn = Arn(arn_value)
        return template\
            .replace('%PRINCIPAL_ID%', principal_id)\
            .replace('%REGION%', arn.region)\
            .replace('%ACCOUNT_ID%', arn.account_id)\
            .replace('%API_ID%', arn.api_id)\
            .replace('%STAGE%', arn.stage)
