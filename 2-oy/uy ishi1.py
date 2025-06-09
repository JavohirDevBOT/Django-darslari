import csv
import os

FAYL = 'students.csv'

def yukla():
    if not os.path.exists(FAYL):
        return []
    with open(FAYL, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def saqla(talabalar):
    with open(FAYL, "w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'name', 'course', 'email', 'phone'])
        writer.writeheader()
        writer.writerows(talabalar)

def korish():
    talabalar = yukla()
    if not talabalar:
        print("Hech qanday talaba yo'q")
        return
    for t in talabalar:
        print(f"{t['id']}. {t['name']} - {t['course']} - {t['email']} - {t['phone']}")

def qoshish():
    talabalar = yukla()
    yangi_id = str(max([int(t['id']) for t in talabalar], default=0) + 1)
    ism = input("Ism kiriting: ")
    kurs = input("Kurs kiriting: ")
    email = input("Email kiriting: ")
    tel = input("Telefon kiriting: ")
    talabalar.append({'id': yangi_id, 'name': ism, 'course': kurs, 'email': email, 'phone': tel})
    saqla(talabalar)
    print("Talaba qo'shildi.")

def yangilash():
    talabalar = yukla()
    id_ = input("Qaysi ID talaba yangilanadi: ")
    for t in talabalar:
        if t['id'] == id_:
            ism = input(f"Ism ({t['name']}): ") or t['name']
            kurs = input(f"Kurs ({t['course']}): ") or t['course']
            email = input(f"Email ({t['email']}): ") or t['email']
            tel = input(f"Tel ({t['phone']}): ") or t['phone']
            t.update({'name': ism, 'course': kurs, 'email': email, 'phone': tel})
            saqla(talabalar)
            print("Yangilandi.")
            return
    print("Bunday ID topilmadi.")

def ochirish():
    talabalar = yukla()
    id_ = input("Qaysi ID talaba o'chirilsin: ")
    yangi = [t for t in talabalar if t['id'] != id_]
    if len(yangi) == len(talabalar):
        print("Bunday ID yo'q.")
    else:
        saqla(yangi)
        print("Talaba o'chirildi.")

def qidiruv():
    talabalar = yukla()
    soz = input("Ism yoki kurs kiriting: ").lower()
    topilgan = [t for t in talabalar if soz in t['name'].lower() or soz in t['course'].lower()]
    if topilgan:
        for t in topilgan:
            print(f"{t['id']}. {t['name']} - {t['course']}")
    else:
        print("Topilmadi.")

def statistika():
    talabalar = yukla()
    natija = {}
    for t in talabalar:
        kurs = t['course']
        natija[kurs] = natija.get(kurs, 0) + 1
    for kurs, soni in natija.items():
        print(f"{kurs} kursida {soni} ta talaba bor.")

def menyu():
    while True:
        print("""
TALABALAR BAZASI
1. Barcha talabalarni ko‘rish
2. Yangi talaba qo‘shish
3. Talabani yangilash
4. Talabani o‘chirish
5. Qidiruv
6. Kurs bo‘yicha statistika
0. Chiqish
""")
        tanlov = input("Tanlov: ")
        if tanlov == "1":
            korish()
        elif tanlov == "2":
            qoshish()
        elif tanlov == "3":
            yangilash()
        elif tanlov == "4":
            ochirish()
        elif tanlov == "5":
            qidiruv()
        elif tanlov == "6":
            statistika()
        elif tanlov == "0":
            print("Dastur tugadi.")
            break
        else:
            print("Noto‘g‘ri tanlov.")

menyu()
