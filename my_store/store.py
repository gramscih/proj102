from product import Product


class Store:
    NAME = "GHC Store"

    def get_products(self):
        return Product.read()
