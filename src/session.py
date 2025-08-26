storage = {}


def store(user_id, key, value):
    user_storage = storage.get(user_id, {})
    user_storage[key] = value


def retrieve(user_id, key, default=None):
    return storage.get(user_id, {}).get(key, default)


def delete(user_id, key=None):
    if key is None:
        storage.pop(user_id, None)
    else:
        storage.get(user_id, {}).pop(key, None)
