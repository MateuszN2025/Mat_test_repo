from T15.practice_api.patterns import ItemBuilder, PricingStrategyFactory
from T15.practice_api.repositories import RepositoryFactory
from T15.practice_api.store import InMemoryStore


def test_healthcheck(api_page):
    response = api_page.health()

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_full_crud_flow_uses_builder_and_page_object(api_page):
    create_payload = (
        ItemBuilder()
        .with_name("Keyboard")
        .with_price(199.99)
        .with_tags("hardware", "qa")
        .build()
    )

    created = api_page.create_item(create_payload)
    assert created.status_code == 201
    created_body = created.json()
    item_id = created_body["id"]
    assert created_body["name"] == "Keyboard"
    assert created_body["display_price"] == 199.99

    vip_view = api_page.get_item(item_id, pricing="vip")
    assert vip_view.status_code == 200
    assert vip_view.json()["display_price"] == 179.99

    replace_payload = (
        ItemBuilder()
        .with_name("Mechanical Keyboard")
        .with_price(249.99)
        .with_tags("hardware", "premium")
        .build()
    )
    replaced = api_page.replace_item(item_id, replace_payload)
    assert replaced.status_code == 200
    assert replaced.json()["name"] == "Mechanical Keyboard"

    patched = api_page.patch_item(item_id, {"is_active": False, "tags": ["refurbished"]})
    assert patched.status_code == 200
    assert patched.json()["is_active"] is False
    assert patched.json()["tags"] == ["refurbished"]

    deleted = api_page.delete_item(item_id)
    assert deleted.status_code == 204

    missing = api_page.get_item(item_id)
    assert missing.status_code == 404


def test_singleton_store_is_shared_across_factory_instances():
    store = InMemoryStore()
    store.reset()
    repository_a = RepositoryFactory.create("memory")
    repository_b = RepositoryFactory.create("memory")

    created = repository_a.create_item(ItemBuilder().with_name("Shared Item").build())
    fetched = repository_b.get_item(created["id"])

    assert fetched is not None
    assert fetched["name"] == "Shared Item"


def test_strategy_factory_and_decorator_audit_log(api_page):
    assert PricingStrategyFactory.create("clearance").apply(100.0) == 70.0

    created = api_page.create_item(ItemBuilder().with_name("Desk").with_price(300.0).build())
    item_id = created.json()["id"]
    api_page.patch_item(item_id, {"price": 280.0})
    api_page.delete_item(item_id)

    audit_log = api_page.audit_log()
    assert audit_log.status_code == 200
    assert audit_log.json() == ["create_item", "patch_item", "delete_item"]
