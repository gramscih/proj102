import consumer

# id	1
# email	"john@gmail.com"
# username	"johnd"
# password	"m38rmF$"


class User:
    def __init__(self, id, email, username, password):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def create(self):
        pass

    @staticmethod
    def read():
        result = []
        users = consumer.read("users")
        for user in users.json():
            new_user = User(
                user["id"], user["email"], user["username"], user["password"]
            )
            result.append(new_user)
        return result

    def update(self):
        pass

    def delete(self):
        pass


print(User.read())
