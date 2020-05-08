# This environment is to develop with flask development server
# the database host is 127.0.0.1
from config.default import MONGO_DB

MONGO_URL = f"mongodb://root:123456@127.0.1:27017/{MONGO_DB}?authSource=admin"
