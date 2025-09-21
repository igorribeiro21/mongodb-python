from abc import ABC, abstractmethod

class OrdersRepositoryInterface(ABC):

    @abstractmethod
    def insert_document(self,document: dict) -> None:
        pass

    @abstractmethod
    def insert_list_of_documents(self, list_of_documents: list) -> None:
        pass

    @abstractmethod
    def select_many(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_one(self, doc_filter: dict) -> dict:
        pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter: dict) -> list:
        pass

    @abstractmethod
    def select_if_properties_exists(self) -> list:
        pass

    @abstractmethod
    def select_by_object_id(self, object_id: str) -> dict:
        pass

    @abstractmethod
    def edit_registry(self, object_id: str, new_values: dict) -> None:
        pass

    @abstractmethod
    def edit_many_registries(self, filter_obj: dict, new_values: dict) -> None:
        pass

    @abstractmethod
    def edit_registry_with_increment(self, object_id: str, field: str, increment_value: int)-> None:
        pass

    @abstractmethod
    def edit_registry_with_decrement(self, object_id: str, field: str, decrement_value: int)-> None:
        pass

    @abstractmethod
    def delete_registry(self, object_id: str) -> None:
        pass

    @abstractmethod
    def delete_many_registries(self, filter_obj: dict) -> None:
        pass
