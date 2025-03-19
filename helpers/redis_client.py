import redis
import json
import functools

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

USER_TOKEN_KEY_FOR_REDIS = "user_auth_token"
USER_TOKEN_EXPIRE_DURATION_IN_HOURS = 2


# from config.common import REDIS_HOST, REDIS_PORT, REDIS_DB

# Initialize Redis client
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)

def cached_in_redis(key: str, expire_hours: int):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = key  
            cached_value = redis_client.get(cache_key)

            if cached_value:
                return cached_value  
            
            result = func(*args, **kwargs)

            if result:
                redis_client.setex(cache_key, expire_hours * 3600, result)  
                # redis_client.setex(cache_key, expire_hours , result)  
            return result

        def invalidate_cache():
            """Manually clear the cache."""
            redis_client.delete(key)

        wrapper.invalidate_cache = invalidate_cache
        return wrapper

    return decorator

#%%

# %%
