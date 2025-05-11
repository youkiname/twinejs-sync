from dotenv import dotenv_values

config = dotenv_values("../.env")

print(config)

SERVER_HOST = config.get('SERVER_HOST', 'localhost')
SERVER_PORT = config.get('SERVER_PORT', '8000')
API_BASE_URL = config.get('API_BASE_URL', '/twine-api')
