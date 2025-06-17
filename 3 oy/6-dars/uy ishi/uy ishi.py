mahsulotlar = [
    {"nom": "olma", "tur": "oziq ovqat"},
    {"nom": "televizor", "tur": "texnika"},
]

def admin_panel():
    while True:
        print("[ADMIN PANEL]")
        print("1.mahsulot qushish")
        print("2.foydalanuvchi qushish")
        print("3.mahsulotlar royxati")
        print("4.chiqish")
        t = input(">> ")
        if t == "1":
            n = input("Mahsulot nomi: ")
            u = input("Mahsulot turi: ")
            mahsulotlar.append({"nom": n, "tur": u})
        elif t == "2":
            input("Foydalanuvchi ismi: ")
        elif t == "3":
            for m in mahsulotlar:
                print(m["nom"], "-", m["tur"])
        elif t == "4":
            break

def customer_panel():
    while True:
        print("[CUSTOMER PANEL]")
        print("1.mahsulotlar royxati")
        print("2.mahsulotlarni qidirish")
        print("3.oziq ovqat")
        print("4.texnika")
        print("5.chiqish")
        t = input(">> ")
        if t == "1":
            for m in mahsulotlar:
                print(m["nom"], "-", m["tur"])
        elif t == "2":
            n = input("Qidirilayotgan nom: ")
            for m in mahsulotlar:
                if m["nom"] == n:
                    print(m["nom"], "-", m["tur"])
        elif t == "3":
            for m in mahsulotlar:
                if m["tur"] == "oziq ovqat":
                    print(m["nom"])
        elif t == "4":
            for m in mahsulotlar:
                if m["tur"] == "texnika":
                    print(m["nom"])
        elif t == "5":
            break

while True:
    print("1.admin panel")
    print("2.customer panel")
    print("3.chiqish")
    t = input(">> ")
    if t == "1":
        admin_panel()
    elif t == "2":
        customer_panel()
    elif t == "3":
        break
