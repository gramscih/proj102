import consumer

# id	1
# title	"Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops"
# price	109.95
# description	"Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday"
# category	"men's clothing"
# image	"https://fakestoreapi.com…PKd-2AYL._AC_SL1500_.jpg"
# rating


class Product:
    def __init__(self, id, title, price, description, category, img, rating) -> None:
        self.id = id
        self.title = title
        self.price = price
        self.description = description
        self.category = category
        self.img = img
        self.rating = rating

    def create(self):
        pass

    @staticmethod
    def read():
        result = []
        products = consumer.read("products")
        for product in products.json():
            new_product = Product(
                product["id"],
                product["title"],
                product["price"],
                product["description"],
                product["category"],
                product["image"],
                product["rating"],
            )
            result.append(new_product)

        return result

    def update(self):
        pass

    def delete(self):
        pass
