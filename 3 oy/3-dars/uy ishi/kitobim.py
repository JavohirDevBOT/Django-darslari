import json
from kutubxona import Kitob, Kutubhona

def kitob_to_dict(kitob):
    return {
        "muallifi": kitob.muallifi,
        "kitob_nomi": kitob.kitob_nomi,
        "narxi": kitob.narxi
    }

def jsondan_kutubhona_yuklash(json_fayl_nomi, kutubxona):
    with open(json_fayl_nomi, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            k = Kitob(item["muallifi"], item["kitob_nomi"])
            k.narxi = item["narxi"]
            kutubxona.qosh(k)

kitob1 = Kitob("Abdullo Qodiriy", "Mehrobdan Chayon")
kitob2 = Kitob("ABC", "Python")
kitob3 = Kitob("ABC", "Java")

kutubhona = Kutubhona("Alisher Navoiy")
kutubhona.qosh(kitob1)
kutubhona.qosh(kitob2)
kutubhona.qosh(kitob3)

kutubhona[0] = "javohir ziyadullayev"

print(kutubhona[0])
print(len(kutubhona))
print("Java" in kutubhona)

for kitob in kutubhona:
    print(kitob)

kitoblar_list = [kitob_to_dict(k) for k in kutubhona]
with open("kitoblar.json", "w", encoding="utf-8") as f:
    json.dump(kitoblar_list, f, ensure_ascii=False, indent=4)

print("Kitoblar json faylga saqlandi.")
