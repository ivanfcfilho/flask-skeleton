# This environment is to run the application with docker-compose
# the database host is the name of service: mongo
from config.default import MONGO_DB

MONGO_URL = f"mongodb://root:123456@mongo:27017/{MONGO_DB}?authSource=admin"
