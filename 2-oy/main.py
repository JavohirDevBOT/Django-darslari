import json


def data_read():
    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        with open("users.json", "w") as file:
            users = [{"username": "admin", "password": "admin", "role": "admin"}]
            json.dump(users, file)
    return users


def data_write(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)


def register():
    users = data_read()

    login = input("Login: ")
    parol = input("Parol: ")
    for user in users:
        if user['username'] == login:
            print("Bu login bazada bor")
            return
    users.append({"username": login, "password": parol, "role": "user"})
    print("Ro'yxatdan o'tdingiz")
    data_write(users)


def login():
    users = data_read()

    login = input("Login: ")
    parol = input("Parol: ")
    for user in users:
        if user['username'] == login and user['password'] == parol:
            print("Do'konga hush kelibsiz")
            return login, user['role']

    print("Bazada bunday login yo'q")
    return None, None

def admin_menu():
    while True:
        menu = input(""" Admin menusi
        1. New orders (status: new)
        2. Accepted orders (status: accepted)
        3. Canceled orders (status: canceled)
        4. Add new product
        5. Delete product
        6. Logout\n""")
    print()
def main():
    while True:
        try:
            menu = int(input("""Elektron do'kon:
            1. Register
            2. Login
            3. Exit\n"""))
        except:
            print("Xato. 1-3 oraliqda son tanlang")
            continue

        if menu == 1:
            register()
        elif menu == 2:
            username, role = login()
        elif menu == 3:
            break
        else:
            print("Xato. 1-3 oraliqda son tanlang")


main()
