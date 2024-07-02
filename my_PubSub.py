"""Cunsom PubSub implementation."""


class PubSub:
    """Custom PubSub class."""

    def __init__(self):
        """Initialize subscribers dictionary."""
        self.subscribers = {}

    def subscribe(self, event_name):
        """Subscribe to event_name."""

        def decorator(func):
            """Add function to subscribers list."""
            if event_name not in self.subscribers:
                self.subscribers[event_name] = []
            self.subscribers[event_name].append(func)

            return func

        return decorator

    def emit(self, event_name, data):
        """Emit event_name with data."""
        if event_name in self.subscribers:
            for func in self.subscribers[event_name]:
                func(data)

    def off(self, event_name, func):
        """Unsubscribe from event_name."""
        if event_name in self.subscribers:
            self.subscribers[event_name] = [f for f in self.subscribers[event_name] if f != func]


# Пример использования
pubSub = PubSub()


@pubSub.subscribe("event1")
def log1(data):
    """Test function 1."""
    print("event1", data)


@pubSub.subscribe("event2")
def log2(data):
    """Test function 2."""
    print("event2", data)


@pubSub.subscribe("event1")
def log3(data):
    """Test function 3."""
    print("event1-1111", data)


# Эмитим событие до отписки
pubSub.emit("event1", "hello")
pubSub.emit("event2", "hello")

# Отписываем log3 от event1
pubSub.off("event1", log3)

# Эмитим событие после отписки
pubSub.emit("event1", "hello again")
pubSub.emit("event2", "hello again")
