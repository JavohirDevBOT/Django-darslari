import csv
import os

user_file = "user.csv"

def data_read(file_name):
    datas = []
    if os.path.exists(file_name):
        with open(file_name, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                datas.append(row)
    return datas

def data_write(datas):
    with open(user_file, "w", newline='') as file:
        fieldnames = ["id", "username", "password", "role"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for d in datas:
            writer.writerow(d)

def register():
    users = data_read(user_file)

    login = input("Login: ")
    parol = input("Parol: ")
    id_list = []

    for user in users:
        if user['username'] == login:
            print("Bu login bazada bor")
            return
        id_list.append(int(user['id']))

    id = max(id_list, default=0) + 1

    users.append({"id": str(id), "username": login, "password": parol, "role": "user"})
    print("Ro'yxatdan o'tdingiz")
    data_write(users)

def main():
    while True:
        try:
            menu = int(input("""Elektron do'kon:
            1. Register\n"""))
        except:
            print("Xato. 1-3 oraliqda son tanlang")
            continue

        if menu == 1:
            register()
            break
        else:
            print("Xato. 1-3 oraliqda son tanlang")

main()
