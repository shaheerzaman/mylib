from mylib.client import set_credentials
from mylib.user import User


def main():
    # Initialize the API client with your API
    set_credentials(token="secret123")

    # create an save
    u = User(name="Shaheer", email="shaheer@gmail.com")
    u.save()

    # Change and save
    u.name = "Shaher Zaman"
    u.save()

    # Find all users
    users = User.find()
    print(users)


if __name__ == "__main__":
    main()
