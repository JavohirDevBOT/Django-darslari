class Film:
    def __init__(self, nomi, janr, reyting):
        self.nomi = nomi
        self.janr = janr
        self.reyting = reyting

    def __eq__(self, boshqa):
        return self.nomi == boshqa.nomi and self.janr == boshqa.janr and self.reyting == boshqa.reyting

    def __repr__(self):
        return f"{self.nomi} ({self.janr}) - {self.reyting}"

    def __int__(self):
        return int(self.reyting)

    def __hash__(self):
        return hash((self.nomi, self.janr, self.reyting))


class FilmLibrary:
    def __init__(self):
        self.filmlar = []

    def __add__(self, film):
        self.filmlar.append(film)
        return self

    def __iadd__(self, film):
        self.filmlar.append(film)
        return self

    def __len__(self):
        return len(self.filmlar)

    def __contains__(self, film):
        if isinstance(film, str):
            return any(f.nomi == film for f in self.filmlar)
        return film in self.filmlar

    def __getitem__(self, index):
        return self.filmlar[index]

    def __setitem__(self, index, yangi):
        self.filmlar[index] = yangi

    def __delitem__(self, index):
        del self.filmlar[index]

    def __repr__(self):
        return '\n'.join([str(f) for f in self.filmlar])

    def __iter__(self):
        return iter(self.filmlar)

    def __call__(self, janr=None):
        if janr is None:
            return self.filmlar
        else:
            return [f for f in self.filmlar if f.janr == janr]

    def __eq__(self, boshqa):
        return self.filmlar == boshqa.filmlar

    def __reversed__(self):
        return reversed(self.filmlar)

    def __bool__(self):
        return bool(self.filmlar)

    def __gt__(self, boshqa):
        return self.ortalacha_reyting() > boshqa.ortalacha_reyting()

    def __lt__(self, boshqa):
        return self.ortalacha_reyting() < boshqa.ortalacha_reyting()

    def eng_yuqori(self):
        if self.filmlar:
            return max(self.filmlar, key=lambda f: f.reyting)
        return None

    def ortalacha_reyting(self):
        if self.filmlar:
            return sum(f.reyting for f in self.filmlar) / len(self.filmlar)
        return 0
f1 = Film("oshiq", "nmadir", 9)
f2 = Film("nmadi1", "nmadir 3", 8)
f3 = Film("nma edi", "qaysi", 9)

print(f1 == f2)
print(f1 == f3)
print(f1)
kutubxona = FilmLibrary()

kutubxona + f1
kutubxona + f2

print(kutubxona)
print(len(kutubxona))
print(f1 in kutubxona)

for f in kutubxona:
    print(f)

print(kutubxona[0])
kutubxona[0] = f3
print(kutubxona[0])
del kutubxona[0]
print(len(kutubxona))
print(bool(kutubxona))

barcha = kutubxona()
print(barcha)

faqat_fan = kutubxona("Fantastika")
print(faqat_fan)

yangi = FilmLibrary()
yangi + f2

print(kutubxona == yangi)

for f in reversed(kutubxona):
    print(f)

kutubxona += f1
print(len(kutubxona))


