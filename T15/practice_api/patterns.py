from functools import wraps
from typing import Protocol


def audit_action(event_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self.store.append_audit_log(event_name)
            return result

        return wrapper

    return decorator


class PricingStrategy(Protocol):
    def apply(self, price: float) -> float:
        ...


class RegularPricing:
    def apply(self, price: float) -> float:
        return round(price, 2)


class VipPricing:
    def apply(self, price: float) -> float:
        return round(price * 0.9, 2)


class ClearancePricing:
    def apply(self, price: float) -> float:
        return round(price * 0.7, 2)


class PricingStrategyFactory:
    _strategies = {
        "regular": RegularPricing,
        "vip": VipPricing,
        "clearance": ClearancePricing,
    }

    @classmethod
    def create(cls, name: str) -> PricingStrategy:
        try:
            return cls._strategies[name]()
        except KeyError as exc:
            supported = ", ".join(sorted(cls._strategies))
            raise ValueError(f"Unknown pricing strategy '{name}'. Use one of: {supported}.") from exc


class ItemBuilder:
    def __init__(self):
        self._payload = {
            "id": 1,
            "name": "Training Item",
            "price": 99.99,
            "tags": ["practice"],
            "is_active": True,
        }

    def with_id(self, item_id: int):
        self._payload["id"] = item_id
        return self

    def with_name(self, name: str):
        self._payload["name"] = name
        return self

    def with_price(self, price: float):
        self._payload["price"] = price
        return self

    def with_tags(self, *tags: str):
        self._payload["tags"] = list(tags)
        return self

    def inactive(self):
        self._payload["is_active"] = False
        return self

    def build(self) -> dict:
        return dict(self._payload)
