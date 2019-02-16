
class Arn:

    def __init__(self, raw_arn):
        self.raw_arn = raw_arn

        arn_partials = raw_arn.split(':')

        self.region = arn_partials[3]
        self.account_id = arn_partials[4]

        api_gateway_arn_partials = arn_partials[5].split('/')
        self.api_id = api_gateway_arn_partials[0]
        self.stage = api_gateway_arn_partials[1]
        self.http_method = api_gateway_arn_partials[2]
        self.resource = Arn.extract_resource(api_gateway_arn_partials)

    @staticmethod
    def extract_resource(api_gateway_arn_partials):
        return api_gateway_arn_partials[3]
