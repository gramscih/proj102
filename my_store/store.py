from product import Product
import custom_exceptions


class Store:
    NAME = "GHC Store"

    def get_products(self):
        data = None
        try:
            data = Product.read()
        except custom_exceptions.InvalidURlException as err:
            print(err)
        return data
