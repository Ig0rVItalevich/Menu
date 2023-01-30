import redis
import pickle


class Cache():
    def __init__(self, config):
        self.cache = redis.StrictRedis(
            host=config["host"],
            port=config["port"],
            db=config["db"]
        )

    def set(self, id, model):
        cacheModel = pickle.dumps(model)
        self.cache.set(id, cacheModel)

    def get(self, id):
        cacheModel = self.cache.get(id)
        if cacheModel is None:
            return None
        
        return pickle.loads(cacheModel)

    def delete(self, id):
        self.cache.delete(id)
