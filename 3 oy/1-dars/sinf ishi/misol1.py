# royxat = [2,3,4]
# royxat2 = [10,20,30]
#
#
# def qiymat_qosh(qiymat):
#     royxat.append(qiymat)
#
# def boshiga_qosh(qiymat):
#     royxat.insert(0, qiymat)
#
# def test_func1(qiymat):
#     pass
#
#
# def qiymat_qosh1(qiymat):
#     royxat2.append(qiymat)
#
# def boshiga_qosh1(qiymat):
#     royxat2.insert(0, qiymat)
#
# def test_func2(qiymat):
#     pass
#
# royxat = 10
#
# print(royxat)
# 1. Har bir ma'lumotga alohida funksiya yozdik
# 2. Yangi ma'lumot qo'shasak, hamma metodlar yana qo'shiladi
# 3. Ma'lumot ochiq. Xavfsiz emas

class Test:

    def __init__(self, name, price, stock):
        self.name = name
        assert price > 0, "Narx >0 bo'lishi kerak"
        assert stock > 0, "Soni 0 dan katta emas"
        self.__price = price
        self.__stock = stock
    def get_stock(self):
        return self.__stock
    def set_stock(self, value):
        assert value > 0, "Narx >0 bo'lishi kerak"
        self.__stock = value
    def total_price(self):
        return self.__price * self.__stock

    # o'qish
    def  get_price(self):
        return self.__price

    def set_price(self, value):
        assert value > 0, "Narx >0 bo'lishi kerak"
        self.__price = value
