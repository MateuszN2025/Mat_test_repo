from threading import Lock


class InMemoryStore:
    _instance = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance.items = {}
                    instance.audit_log = []
                    instance.next_id = 1
                    cls._instance = instance
        return cls._instance

    def reset(self):
        self.items.clear()
        self.audit_log.clear()
        self.next_id = 1
