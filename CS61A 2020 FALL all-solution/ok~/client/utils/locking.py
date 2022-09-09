"""Used for locking answers in tests."""

import hmac

def lock(key, text):
    """Locks the given text using the given key and returns the result"""
    return hmac.new(key.encode('utf-8'), text.encode('utf-8'), digestmod='md5').hexdigest()
