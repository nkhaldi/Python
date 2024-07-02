"""Custom implementation of a timed cache."""

import threading
import time


class TimedCache:
    """Timed cache class."""

    def __init__(self):
        """Initialize cache and lock."""
        self.cache = {}
        self.lock = threading.Lock()

    def set(self, key, value, ttl):
        """Set value with TTL."""
        expiration_time = time.time() + ttl
        with self.lock:
            self.cache[key] = (value, expiration_time)
        # Запускаем поток для удаления элемента по истечении времени
        threading.Thread(target=self._remove_after_ttl, args=(key, ttl)).start()

    def get(self, key):
        """Get value by key."""
        with self.lock:
            if key in self.cache:
                value, expiration_time = self.cache[key]
                if time.time() < expiration_time:
                    return value
                else:
                    del self.cache[key]
                    return None
            return None

    def _remove_after_ttl(self, key, ttl):
        """Remove key after TTL."""
        time.sleep(ttl)
        with self.lock:
            if key in self.cache:
                value, expiration_time = self.cache[key]
                if time.time() >= expiration_time:
                    del self.cache[key]

    def __contains__(self, key):
        """Check if key is in cache and not expired."""
        with self.lock:
            if key in self.cache:
                _, expiration_time = self.cache[key]
                if time.time() < expiration_time:
                    return True
                else:
                    del self.cache[key]
            return False


# Пример использования
cache = TimedCache()
cache.set("foo", "bar", 5)  # Устанавливаем значение с TTL 5 секунд

print(cache.get("foo"))  # Вывод: bar

time.sleep(6)

print(cache.get("foo"))  # Вывод: None (значение истекло)
