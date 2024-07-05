"""Get all values from Reis database."""

import redis


def try_decode(byte_data: bytes):
    """Try to decode byte data, return hex representation if decode fails."""
    try:
        print(type(byte_data))
        return byte_data.decode("utf-8")
    except UnicodeDecodeError:
        return f"Binary data: {byte_data.hex()}"


def get_redis_value(key: str):
    """Get value from redis bd by key."""
    key_type = r.type(key).decode("utf-8")
    if key_type == "string":
        # Fetch value for string key
        value = r.get(key)
        value = try_decode(value)
    elif key_type == "list":
        # Fetch list items
        value = r.lrange(key, 0, -1)
        value = [item.decode("utf-8") if isinstance(item, bytes) else item for item in value]
    elif key_type == "set":
        # Fetch set members
        value = r.smembers(key)
        value = {item.decode("utf-8") if isinstance(item, bytes) else item for item in value}
    elif key_type == "hash":
        # Fetch hash fields and values
        value = r.hgetall(key)
        value = {k.decode("utf-8"): try_decode(v) for k, v in value.items()}
    else:
        value = f"Data type '{key_type}' not handled in this script"


if __name__ == "__main__":
    redis_host = input("Redis host: ")
    redis_port = input("Redis port: ")
    redis_base = input("Redis base: ")

    try:
        # Connect to Redis
        r = redis.Redis(host=redis_host, port=redis_port, db=redis_base)

        # Get all keys and create a dictionary to store key-value pairs
        keys = r.keys()
        print(f"Keys: {keys}")
        redis_data = dict()

        for key in keys:
            value = get_redis_value(key)
            redis_data[key.decode("utf-8")] = value

        # Print the dictionary with key-value pairs
        print("Redis Key-Value Pairs:")
        for key, value in redis_data.items():
            print(f"{key}: {value}")

    except Exception as err:
        print(f"An error occurred: {err}")
