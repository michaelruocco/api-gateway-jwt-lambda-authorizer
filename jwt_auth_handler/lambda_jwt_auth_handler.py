import logging


class LambdaJwtAuthHandler:

    def __init__(self, jwt_service, policy_loader):
        self.logger = logging.getLogger(__name__)
        self.jwt_service = jwt_service
        self.policy_loader = policy_loader

    def handle(self, event, context):
        self.logger.info('received event {}'.format(str(event)))
        self.logger.info('received context {}'.format(str(context)))
        token = event['authorizationToken']
        arn = event['methodArn']
        principal_id = self.extract_principal_id(token)
        return self.load_policy(principal_id, arn)

    def extract_principal_id(self, token):
        payload = self.jwt_service.decode(token)
        self.logger.info('converted token into payload {}'.format(payload))
        return payload['sub']

    def load_policy(self, principal_id, arn):
        self.logger.info('loading policy with principal id {} and arn {}'.format(principal_id, arn))
        return self.policy_loader.load(principal_id, arn)
