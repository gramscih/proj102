from store import Store

store = Store()


def opt_processor(opt):
    if opt == "1":
        products = store.get_products()
        print("------------------List of products------------------------")
        for product in products:
            print("_____________________________________")
            print(f"ID: {product.id}")
            print(f"Name: {product.title}")
            print(f"Price: {product.price}")
            # print(f"Description: {product.description}")
            print("-------------------------------------")


def run_app():
    run = True
    while run:
        print("=================Well come to GHC Store=================")
        print("1. Show Products.")
        opt = input("Your option is...: ")
        opt_processor(opt)


if __name__ == "__main__":
    run_app()
