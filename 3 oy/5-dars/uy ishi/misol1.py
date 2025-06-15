class Kitob:
    def __init__(self, nom, muallif, bet):
        self.nom = nom
        self.muallif = muallif
        self._bet = 1
        self.bet = bet

    @property
    def bet(self):
        return self._bet

    @bet.setter
    def bet(self, qiymat):
        if qiymat > 0:
            self._bet = qiymat

    def __eq__(self, boshqa):
        return isinstance(boshqa, Kitob) and self.nom == boshqa.nom and self.muallif == boshqa.muallif

    def __hash__(self):
        return hash((self.nom, self.muallif))
class Foyda:
    def __init__(self, nom, pochta):
        self.nom = nom
        self.pochta = pochta
        self.olgan = []

    def ol(self, kitob):
        self.olgan.append(kitob)

    def __eq__(self, boshqasi):
        return isinstance(boshqasi, Foyda) and self.pochta == boshqasi.pochta

    def __hash__(self):
        return hash(self.pochta)

    def __len__(self):
        return len(self.olgan)

    def __getitem__(self, i):
        return self.olgan[i]
class Kutub:
    def __init__(self):
        self.kitoblar = []
        self.foydalar = []

    def qosh(self, kitob):
        self.kitoblar.append(kitob)

    def foyda_qosh(self, foyda):
        self.foydalar.append(foyda)

    def __contains__(self, nom):
        for k in self.kitoblar:
            if k.nom == nom:
                return True
        return False

    def __getitem__(self, nom):
        for k in self.kitoblar:
            if k.nom == nom:
                return k
        return None

    def __bool__(self):
        return len(self.kitoblar) > 0

    def ochir(self, nom):
        for k in self.kitoblar:
            if k.nom == nom:
                self.kitoblar.remove(k)
                break

    @property
    def soni(self):
        return len(self.kitoblar)

    @soni.deleter
    def soni(self):
        self.kitoblar = []
kutub = Kutub()
k1 = Kitob("Python", "Ali", 250)
f1 = Foyda("ali", "ali@mail.com")

kutub = Kutub()
kutub.qosh(k1)
kutub.foyda_qosh(f1)

f1.ol(k1)

k = f1[0]
bor = "Python" in kutub
kit = kutub["Python"]
n = len(f1)

print(k.nom)
print(bor)
print(kit.muallif)
print(n)
