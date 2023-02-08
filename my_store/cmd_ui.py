import logging

from store import Store

store = Store()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%F-%m-%d %H:%M:%S",
    filename="store.log",
)


def opt_processor(opt):
    if opt == "1":
        products = store.get_products(logging)
        print("------------------List of products------------------------")
        for product in products:
            print("_____________________________________")
            print(f"ID: {product.id}")
            print(f"Name: {product.title}")
            print(f"Price: {product.price}")
            # print(f"Description: {product.description}")
            print("-------------------------------------")
    elif opt == "2":
        print("------------------Add new product------------------------")
        title = input(f"Title: ")
        price = input(f"Price: ")
        description = input(f"Description: ")
        category = input(f"Category: ")
        store.add_new_product(title, price, description, "", category, logging)


def run_app():
    run = True
    while run:
        print("=================Well come to GHC Store=================")
        print("1. Show Products.")
        print("2. Add New Product.")
        opt = input("Your option is...: ")
        opt_processor(opt)


if __name__ == "__main__":
    run_app()
