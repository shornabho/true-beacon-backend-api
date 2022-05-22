import os
from dotenv import load_dotenv

ROOT_PATH = os.getcwd()

dotenv_path = os.path.join(ROOT_PATH, '.env')
load_dotenv(dotenv_path=dotenv_path)

# JWT CONSTANTS

JWT_SECRET = os.environ.get('JWT_SECRET')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM')
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRE_MINUTES'))

# DATABASE CONSTANTS

SQLALCHEMY_DATABASE_URL = os.environ.get('SQLALCHEMY_DATABASE_URL')