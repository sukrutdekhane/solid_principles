from open_close_package.interfaces.interface import db_persistence

class Product:
    price: int
    name: str

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        self.products.remove(product)

    def total_price(self) -> int:
        return sum(product.price for product in self.products)

class InvoicePrinter:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart
    def print_invoice(self) -> None:
        print("Invoice:")

class SQLStorage(db_persistence):
    def save(self, cart: ShoppingCart) -> None:
        print("Saving the products to the SQL database.")

class NoSQLStorage(db_persistence):
    def save(self, cart: ShoppingCart) -> None:
        print("Saving the products to the NoSQL database.")

class FileStorage(db_persistence):
    def save(self, cart: ShoppingCart) -> None:
        print("Saving the products to a file.")


if __name__ == "__main__":
    product1 = Product("Laptop",1000)
    product2 = Product("Mouse",50)
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)

    printer = InvoicePrinter(cart)
    printer.print_invoice()

    sql_storage = SQLStorage()
    sql_storage.save(cart)

    nosql_storage = NoSQLStorage()
    nosql_storage.save(cart)    

    file_storage = FileStorage()
    file_storage.save(cart)