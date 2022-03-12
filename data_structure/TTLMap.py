import time, functools


class Entry(object):
    def __init__(self, value, ttl):
        self._value = value
        self._ttl = ttl
        self._time_inserted = time.time()

    @property
    def expired(self):
        now = time.time()
        return now > self._time_inserted + self._ttl

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return str((self._value, self._ttl))


def runnable(self, unbound_func, interval):
    while 1:
        unbound_func(self)
        time.sleep(interval)


def daemonize(interval):
    from threading import Thread

    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            if not hasattr(self, "_clean_up_d"):
                self._clean_up_d = Thread(target=functools.partial(runnable, self, func, interval), daemon=True)
            return self._clean_up_d
        return wrapper

    return decorator


class TTLMap(object):

    def __init__(self, interval=1):

        self._map = {}
        self._interval = interval
        self.clean_up().start()

    def get(self, key, default=None):
        if key not in self._map:
            return default
        entry = self._map[key]
        if entry.expired:
            del self._map[key]
            return default
        return entry.value

    def put(self, key, value, ttl):
        self._map[key] = Entry(value, ttl)

    def delete(self, key):
        if key in self._map:
            del self._map[key]

    @daemonize(1)
    def clean_up(self):
        for k, v in list(self._map.items()):
            if v.expired:
                del self._map[k]

    def __str__(self):
        return str((self._clean_up, self._map.__str__()))


if __name__ == "__main__":
    m = TTLMap()
    m.put(1,2,1)
    print(m)
    time.sleep(1)
    print(m)
    time.sleep(2)
    print(m)
