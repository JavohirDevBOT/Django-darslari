class Bank:
    def __init__(self, ism, summa):
        self.ism = ism
        self.balance = summa

    def pul_qoshish(self, miqdor):
        if miqdor > 0:
            self.balance += miqdor
        else:
            print("Pul manfiy bo'lishi mumkin emas")

    def pul_olish(self, miqdor):
        if miqdor <= 0:
            print("Pul manfiy bo'lishi mumkin emas")
        elif miqdor > self.balance:
            print("Hisobda yetarli pul yo'q")
        else:
            self.balance -= miqdor

    def balansni_korish(self):
        return self.balance

    def pul_otkazish(self, boshqa, miqdor):
        if not isinstance(boshqa, Bank):
            print("Noto‘g‘ri hisob")
            return
        if miqdor <= 0:
            print("Pul miqdori noto‘g‘ri")
            return
        if miqdor > self.balance:
            print("Yetarli pul yo'q")
            return
        self.balance -= miqdor
        boshqa.balance += miqdor
        print(f"{miqdor} so‘m {boshqa.ism} ga o'tkazildi")


a1 = Bank("Ali", 500)
a2 = Bank("Vali", 300)

a1.pul_qoshish(200)
a1.pul_olish(100)
print(a1.balansni_korish())

a1.pul_qoshish(-50)
a1.pul_olish(1000)

a1.pul_otkazish(a2, 200)
print(a1.balansni_korish())
print(a2.balansni_korish())
