from product import Product
import custom_exceptions


class Store:
    NAME = "GHC Store"

    def add_new_product(self, title, price, dsc, img, ctg, logger=None):
        new_product = Product(1, title, price, dsc, img, ctg)
        new_product.create(logger)

        # title: 'test product',
        # price: 13.5,
        # description: 'lorem ipsum set',
        # image: 'https://i.pravatar.cc',
        # category: 'electronic'

    def get_products(self, logger=None):
        logger.debug("Starting get product function...")
        data = None
        try:
            data = Product.read(logger)
        except custom_exceptions.InvalidURlException as err:
            logger.error(f"Something when wrong reading products [{err}]")
        return data
