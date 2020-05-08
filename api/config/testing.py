from config.default import MONGO_DB

MONGO_URL = f"mongodb://root:123456@127.0.0.1:27017/{MONGO_DB}_test?authSource=admin"
MONGO_DB = f"{MONGO_DB}_test"
