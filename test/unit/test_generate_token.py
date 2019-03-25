from idv_jwt_auth_handler.idv_jwt_service import IdvJwtService

secret_key = 'my-secret'
jwt_service = IdvJwtService(secret_key)

allow_token = jwt_service.create_non_expiring_token('allow-all')
print('allow_token ' + allow_token)
print

deny_token = jwt_service.create_non_expiring_token('deny-all')
print('deny_token ' + deny_token)
print
