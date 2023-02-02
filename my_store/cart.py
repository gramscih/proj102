# id	1
# userId	1
# date	"2020-03-02T00:00:02.000Z"
# products	[…]

URL = "https://fakestoreapi.com/carts"


class Cart:
    def __init__(self, id, userId, date, products) -> None:
        self.id = id
        self.userId = userId
        self.date = date
        self.products = products

    def create(self):
        pass

    def read(self):
        result = []
        products = requests.get(URL)
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
