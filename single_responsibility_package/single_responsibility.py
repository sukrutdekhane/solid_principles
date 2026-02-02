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

class DBStorage:
    def __init__(self, cart: ShoppingCart):
        self.cart = cart

    def save(self) -> None:
        # Simulate saving to a database
        print("Saving the products to the database.")


if __name__ == "__main__":
    product1 = Product("Laptop",1000)
    product2 = Product("Mouse",50)
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)

    printer = InvoicePrinter(cart)
    printer.print_invoice()

    storage = DBStorage(cart)
    storage.save() 