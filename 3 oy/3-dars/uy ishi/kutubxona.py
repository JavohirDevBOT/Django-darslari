class Kitob:
    def __init__(self, muallifi, kitob_nomi):
        self.muallifi = muallifi
        self.kitob_nomi = kitob_nomi
        self.narxi = 10

    @property
    def narxi(self):
        return self.__price

    @narxi.setter
    def narxi(self, value):
        assert isinstance(value, (int, float))
        assert value > 0
        self.__price = value

    def __str__(self):
        return f"{self.muallifi} {self.kitob_nomi} {self.narxi}"


class Kutubhona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.__kitoblar = []

    def qosh(self, kitob):
        if isinstance(kitob, Kitob):
            self.__kitoblar.append(kitob)
        else:
            raise TypeError

    def qosh1(self, kitob):
        self.qosh(kitob)

    def kitob_ol(self, index):
        return self.__kitoblar[index]

    def __len__(self):
        return len(self.__kitoblar)

    def __getitem__(self, index):
        return self.__kitoblar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Kitob):
            self.__kitoblar[index] = value
        elif isinstance(value, str):
            self.__kitoblar[index] = Kitob("Noma'lum", value)
        else:
            raise TypeError

    def __delitem__(self, key):
        del self.__kitoblar[key]

    def __contains__(self, key):
        if isinstance(key, Kitob):
            return key in self.__kitoblar
        elif isinstance(key, str):
            for kitob in self.__kitoblar:
                if kitob.kitob_nomi.lower() == key.lower():
                    return True
            return False
        else:
            return False

    def __iter__(self):
        return iter(self.__kitoblar)

    def __str__(self):
        s = f"{self.nomi} kutubxonasi:\n"
        for kitob in sorted(self.__kitoblar, key=lambda k: k.kitob_nomi):
            s += str(kitob) + "\n"
        return s.strip()

    def __reversed__(self):
        return reversed(self.__kitoblar)

    def qidir_muallif(self, muallif):
        return [k for k in self.__kitoblar if k.muallifi.lower() == muallif.lower()]
