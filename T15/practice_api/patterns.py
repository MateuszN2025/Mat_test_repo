from functools import wraps
from typing import Protocol


# ---------------------------------------------------------------------------
# Decorator: audit_action
# ---------------------------------------------------------------------------
# A decorator is a function that wraps another function to add behaviour
# without changing its code.
#
# audit_action is a "decorator factory" — it takes a parameter (event_name)
# and returns the actual decorator. This is why there are three nested functions:
#
#   audit_action(event_name)   ← you call this with the event name
#     decorator(func)          ← receives the method being decorated
#       wrapper(self, ...)     ← runs every time the method is called
#
# Usage in services.py:
#   @audit_action("create_item")
#   def create_item(self, payload):
#       ...
#
# What it does at runtime:
#   1. Calls the original method (create_item).
#   2. If it succeeds, writes "create_item" to the audit log.
#   3. Returns the result unchanged.
#   Note: if the method raises an exception the audit line is NOT written
#   (because the exception skips the lines after func(...)).
# ---------------------------------------------------------------------------
def audit_action(event_name: str):
    def decorator(func):
        # @wraps(func) copies the original function's name, docstring, etc.
        # onto the wrapper. Without it, func.__name__ would be "wrapper"
        # instead of "create_item", which makes debugging harder.
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)   # call the original method
            self.store.append_audit_log(event_name)  # write to audit log
            return result

        return wrapper

    return decorator


# ---------------------------------------------------------------------------
# Strategy pattern
# ---------------------------------------------------------------------------
# The Strategy pattern lets you swap an algorithm at runtime without changing
# the code that uses it.
#
# Here the "algorithm" is how to calculate the display price.
# All strategy classes have the same interface (an apply() method), so the
# service layer can call strategy.apply(price) without knowing which class it has.
#
# Protocol (from typing) is Python's way of defining an interface.
# A class "satisfies" the Protocol if it has the required methods — no need
# to inherit from it explicitly (this is called structural subtyping / duck typing).
# ---------------------------------------------------------------------------
class PricingStrategy(Protocol):
    def apply(self, price: float) -> float:
        ...  # The "..." means "no body required here" — it is just a declaration.


class RegularPricing:
    def apply(self, price: float) -> float:
        return round(price, 2)  # No discount — just clean rounding.


class VipPricing:
    def apply(self, price: float) -> float:
        return round(price * 0.9, 2)  # 10% off for VIP customers.


class ClearancePricing:
    def apply(self, price: float) -> float:
        return round(price * 0.7, 2)  # 30% off for clearance.


# ---------------------------------------------------------------------------
# Factory pattern for pricing strategies
# ---------------------------------------------------------------------------
# The Factory centralises object creation. Instead of writing:
#   if pricing == "vip":
#       strategy = VipPricing()
#   elif pricing == "clearance":
#       strategy = ClearancePricing()
#   ...
# everywhere, you call PricingStrategyFactory.create("vip") and it does it for you.
# Adding a new strategy means adding one entry to _strategies — nothing else changes.
# ---------------------------------------------------------------------------
class PricingStrategyFactory:
    # Class-level dict mapping strategy name → class (not instance).
    # The class is only instantiated inside create() when actually needed.
    _strategies = {
        "regular": RegularPricing,
        "vip": VipPricing,
        "clearance": ClearancePricing,
    }

    @classmethod
    def create(cls, name: str) -> PricingStrategy:
        # @classmethod receives the class (cls) instead of an instance (self).
        # It is used here because create() works on the class dict _strategies,
        # not on any particular instance.
        try:
            return cls._strategies[name]()   # look up the class and instantiate it
        except KeyError as exc:
            supported = ", ".join(sorted(cls._strategies))
            raise ValueError(f"Unknown pricing strategy '{name}'. Use one of: {supported}.") from exc


# ---------------------------------------------------------------------------
# Builder pattern
# ---------------------------------------------------------------------------
# The Builder pattern provides a readable way to construct complex objects
# step by step, especially in tests.
#
# Instead of:
#   item = {"id": 5, "name": "Sale TV", "price": 200.0, "tags": ["sale"], "is_active": True}
# you write:
#   item = ItemBuilder().with_id(5).with_name("Sale TV").with_price(200.0).with_tags("sale").build()
#
# Each "with_*" method returns self so you can chain calls (fluent interface).
# build() returns a plain dict copy so the builder's internal state is not shared.
# ---------------------------------------------------------------------------
class ItemBuilder:
    def __init__(self):
        # Sensible defaults so you only need to override what matters for each test.
        self._payload = {
            "id": 1,
            "name": "Training Item",
            "price": 99.99,
            "tags": ["practice"],
            "is_active": True,
        }

    def with_id(self, item_id: int):
        self._payload["id"] = item_id
        return self   # return self to allow chaining: builder.with_id(2).with_name("X")

    def with_name(self, name: str):
        self._payload["name"] = name
        return self

    def with_price(self, price: float):
        self._payload["price"] = price
        return self

    def with_tags(self, *tags: str):
        # *tags collects any number of positional arguments into a tuple.
        # list() converts it to a list for storage.
        self._payload["tags"] = list(tags)
        return self

    def inactive(self):
        self._payload["is_active"] = False
        return self

    def build(self) -> dict:
        # dict(self._payload) creates a shallow copy so calling build() twice
        # returns two independent dicts.
        return dict(self._payload)
