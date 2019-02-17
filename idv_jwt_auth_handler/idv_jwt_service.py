from jwt_auth_handler.jwt_service import JwtService


class IdvJwtService(JwtService):

    ISSUER = "idv"

    def __init__(self, secret_key):
        JwtService.__init__(self, secret_key, IdvJwtService.ISSUER)
