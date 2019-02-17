from file_content_loader.file_content_loader import load_file_content
from jwt_auth_handler.policy_loader import PolicyLoader


class IdvPolicyLoader(PolicyLoader):

    DEFAULT_POLICY_KEY = 'deny-all'

    def __init__(self):
        policies = IdvPolicyLoader.build_policies(IdvPolicyLoader.DEFAULT_POLICY_KEY)
        PolicyLoader.__init__(self, policies, IdvPolicyLoader.DEFAULT_POLICY_KEY)

    @staticmethod
    def build_policies(default_policy_key):
        return {
            default_policy_key: IdvPolicyLoader.load_file_content('policy_templates/deny-all-policy-template.json'),
            'allow-all': IdvPolicyLoader.load_file_content('policy_templates/allow-all-policy-template.json'),
            'get-only': IdvPolicyLoader.load_file_content('policy_templates/get-only-policy-template.json'),
        }

    @staticmethod
    def load_file_content(relative_path):
        return load_file_content(__name__, relative_path)
