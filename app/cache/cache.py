import pickle
from abc import ABC, abstractmethod

import redis


class AbstractCache(ABC):
    @abstractmethod
    def set(self, id, model):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def delete(self, id):
        pass


class Cache(AbstractCache):
    def __init__(self, config):
        self.cache = redis.StrictRedis(
            host=config['host'],
            port=config['port'],
            db=config['db'],
        )

    def set(self, id, model):
        cache_model = pickle.dumps(model)
        self.cache.set(id, cache_model)

    def get(self, id):
        cache_model = self.cache.get(id)
        if cache_model is None:
            return None

        return pickle.loads(cache_model)

    def delete(self, id):
        self.cache.delete(id)


def new_cache(config):
    return Cache(config=config)
