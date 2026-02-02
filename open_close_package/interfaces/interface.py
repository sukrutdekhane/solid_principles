from abc import ABC, abstractmethod
from single_responsibility_package.single_responsibility import ShoppingCart

class db_persistence(ABC):
    @abstractmethod
    def save(self, cart: ShoppingCart) -> None:
        pass