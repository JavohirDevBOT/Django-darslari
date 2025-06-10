from PIL.FontFile import puti16


class Product:
    def __init__(self, nomi, narxi):
        self.nomi = nomi
        self.narxi = narxi

    def __repr__(self):
        return f"{self.nomi} - {self.narxi} so'm"

    def __eq__(self, other):
        return isinstance(other, Product) and self.nomi == other.nomi and self.narxi == other.narxi
class Savat:
    def __init__(self):
        self._mahsulotlar = []

    def __getitem__(self, index):
        return self._mahsulotlar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Product):
            self._mahsulotlar[index] = value
        else:
            raise ValueError("Faqat Product obyektlarini qo'shish mumkin.")

    def __reversed__(self):
        return reversed(self.savat)

    def __delitem__(self, index):
        del self._mahsulotlar[index]

    def __len__(self):
        return len(self._mahsulotlar)

    def __contains__(self, product):
        return product in self._mahsulotlar

    def __iter__(self):
        return iter(self._mahsulotlar)

    def __str__(self):
        if not self._mahsulotlar:
            return "Savat bo'sh."
        return "\n".join(str(p) for p in self._mahsulotlar)

    def __bool__(self):
        return bool(self._mahsulotlar)

    def __add__(self, product):
        if isinstance(product, Product):
            self._mahsulotlar.append(product)
            return self
        else:
            raise ValueError("Faqat Product obyektini qo‘shish mumkin.")

    def __call__(self):
        return sum(p.narxi for p in self._mahsulotlar)

    def __eq__(self, other):
        if not isinstance(other, Savat):
            return False
        return sorted(self._mahsulotlar, key=lambda x: x.nomi) == sorted(other._mahsulotlar, key=lambda x: x.nomi)

savat=Savat()

p1 = Product("olma", 5000)
p2 = Product("banan", 23333)
p3 = Product("chokolat", 33333)
savat + p1
savat + p2
savat + p3
print(savat)
print(p1 == p2)
print(p1 == p3)
print(p1)
print(len(savat))
print("olma" in savat)
for i in savat:
    print(i)
print(savat[0])
print(p1 in savat)
del savat[0]
print(savat[0])
print(reversed(savat))
