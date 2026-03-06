user = input("Please input your username: ")
password = input("Please input your password: ")

def check(user, password):
    if len(user) == 6:
        print("User name is valid")
    else: print("Invalid user")
    if len(password) >= 8:
        print("Password is valid")
    else: ("Invalid password")


def test():
    check(user, password)

    user = "1"
    print(user + password)

    check(user, password)

    user = "123456"
    password = "1"
    print(user + password)

    check(user, password)

check(user, password)
test()