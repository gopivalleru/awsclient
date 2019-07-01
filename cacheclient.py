import redis


class CacheClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = redis.Redis(host=self.host, port=self.port)

    def set(self, k, v):
        return self.client.set(k, v)

    def get(self, k):
        return self.client.get(k)
