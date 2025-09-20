import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="Interação com banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "ola": "mundo" }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="Interação com banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "elem1": "aqui1" }, { "elem2": "aqui2" }, { "elem3": "aqui3" }]
    orders_repository.insert_list_of_documents(my_doc)

@pytest.mark.skip(reason="Interação com banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print()
        print(doc["itens"])
        print()

@pytest.mark.skip(reason="Interação com banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

@pytest.mark.skip(reason="Interação com banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = { "cupom": True }
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interação com banco")
def test_select_if_properties_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_properties_exists()
    print()
    print(response)
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interação com banco")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.refrigerante": { "$exists": True }
     } # Semelhante a uma busca com AND em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interação com banco")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            { "address":  { "$exists": True } },
            { "itens.doce.tipo": "chocolate" }
        ]
     } # Semelhante a uma busca com OR em SQL
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="Interação com banco")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "68c8aa410e462b92be077db4"
    response = orders_repository.select_by_object_id(object_id)
    print()
    print(response)

@pytest.mark.skip(reason="Interação com banco")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    object_id = "68a9c4825654e3483ac405b6"
    new_values = {
        "cupom": True,
    }
    orders_repository.edit_registry(object_id, new_values)

@pytest.mark.skip(reason="Interação com banco")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    filter_obj = {
        "itens.refrigerante": { "$exists": True }
    }
    new_values = {
        "itens.refrigerante.quantidade": 30,
    }
    orders_repository.edit_many_registries(filter_obj, new_values)

@pytest.mark.skip(reason="Interação com banco")
def test_edit_registry__with_increment():
    orders_repository = OrdersRepository(conn)
    object_id = "68a9c4825654e3483ac405b6"
    field = "itens.pizza.quantidade"
    increment_value = 5
    orders_repository.edit_registry_with_increment(
        object_id,
        field,
        increment_value
    )

def test_edit_registry__with_decrement():
    orders_repository = OrdersRepository(conn)
    object_id = "68a9c4825654e3483ac405b6"
    field = "itens.pizza.quantidade"
    decrement_value = 5
    orders_repository.edit_registry_with_decrement(
        object_id,
        field,
        decrement_value
    )
