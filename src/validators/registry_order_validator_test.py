import pytest
from .registry_order_validator import registry_order_validator

def test_registry_order_validator():
    valid_body = {
        "data": {
            "name": "Jhon Due",
            "address": "R teste",
            "cupom": False,
            "items": [
                {
                    "item": "Refrigerante",
                    "quantidade": 2
                },
                {
                    "item": "Pizza",
                    "quantidade": 3
                }
            ]
        }
    }

    registry_order_validator(valid_body)

def test_registry_order_validator_with_error():
    invalid_body = {
        "data": {
            "name": "Jhon Due",
            "address": "R teste",
            "cupom": "error",
            "items": [
                {
                    "item": "Refrigerante",
                    "quantidade": 2
                },
                {
                    "item": "Pizza",
                    "quantidade": 3
                }
            ]
        }
    }

    with pytest.raises(Exception):
        registry_order_validator(invalid_body)
