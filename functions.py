import itertools

bilgiler = []
sifreler = []

def isim_soyisim():
    isim = input("Kurban'in ismini giriniz (Kücük harflerle): ")
    soyisim = input("Kurban'in soyismini giriniz (Kücük harflerle): ")
    if isim != "":
        bilgiler.append(isim)
        B_isim = isim.upper()
        bilgiler.append(B_isim)
    if soyisim != "":
        bilgiler.append(soyisim)
        B_soyisim = soyisim.upper()
        bilgiler.append(B_soyisim)

def tc_bilgisi():
    tc_bilgi = input("Kurban'in tcsini giriniz : ")
    bilgiler.append(tc_bilgi)

def nick_bilgisi():
    nick = input("Kurban'in Nick'ini giriniz: ")
    bilgiler.append(nick)

def ceptelefonu_bilgisi():
    cep_no = input("Kurban'in Cep Telefon Numarasini giriniz: ")
    bilgiler.append(cep_no)

def takim_bilgisi():
    takim = input("Kurban'in Takimini giriniz (gs/bjk/fb/ts): ")
    if takim == "gs":
        bilgiler.append(takim)
        bilgiler.append("galatasaray")
        bilgiler.append("GALATASARY")
    elif takim == "fb":
        bilgiler.append(takim)
        bilgiler.append("FENERBAHCE")
        bilgiler.append("fenerbahce")
    elif takim == "bjk":
        bilgiler.append(takim)
        bilgiler.append("BESIKTAS")
        bilgiler.append("besiktas")
    elif takim == "ts":
        bilgiler.append(takim)
        bilgiler.append("TRABZONSPOR")
        bilgiler.append("trabzonspor")
    else:
        bilgiler.append(takim)

def dogum_tarihi_bilgisi():
    dtbilgi = input('Kurban\'in Dogum Tarihini giriniz: (GG.AA.YY)')
    dtbilgi.replace(".", "")
    bilgiler.append(dtbilgi)

def araba_bilgisi():
    pass

def memleket_bilgisi():
    pass

def cep_telefon_tipi():
    tus = []

    cevap = input("Isim, Soyisim ve Nick Cep Telefonu tus formatina cevrilsin? (e/h)\n")
    if cevap == "e":
        str_bilgiler = ''.join(map(str, bilgiler))
        for i in range(len(str_bilgiler)):
            harf = str_bilgiler[i].lower()
            if harf == "a" or harf == "b" or harf == "c" or harf == "ç":
                tus.append("2")
            if harf == "d" or harf == "e" or harf == "f":
                tus.append("3")
            if harf == "g" or harf == "ğ" or harf == "h" or harf == "ı" or harf == "i":
                tus.append("4")
            if harf == "j" or harf == "k" or harf == "l":
                tus.append("5")
            if harf == "m" or harf == "n" or harf == "o" or harf == "ö":
                tus.append("6")
            if harf == "q" or harf == "p" or harf == "r" or harf == "s" or harf == "ş":
                tus.append("7")
            if harf == "t" or harf == "u" or harf == "ü" or harf == "v":
                tus.append("8")
            if harf == "w" or harf == "x" or harf == "y" or harf == "z":
                tus.append("9")
    bilgiler.extend(tus)

def pet_bilgisi():
    nick = input("Kurban'in Evcil Hayvan'inin adini giriniz: ")
    bilgiler.append(nick)

def noktalama():
    noktalama = input("Kullanmak istediginiz noktalama isaretlerini giriniz: ")
    bilgiler.append(noktalama)

def diger():
    diger = input("Girmek istediginiz diger bilgileri giriniz: ")
    bilgiler.append(diger)

def olasilik():
    min = int(input("Minimum sifre uzunlugunu giriniz: "))
    max = int(input("Maximum sifre uzunlugunu giriniz: "))
    if max < 5:
        for i in range(min, max + 1):
            veri = list(itertools.combinations(bilgiler, i))
            sifreler.extend(veri)
    elif 10> max > 5:
        pass # Düzenlenmesi gerek 5ten sonra RAM kullanimi cok fazla!!!!

def sifre_olustur():
    d_isim = input("Yazdirmak istediginiz dosya adini girin: ")
    duzenlenmis_bilgi = "\n".join(map(str, sifreler))
    d1 = duzenlenmis_bilgi.replace('(', '')
    d2 = d1.replace('\'', '')
    d3 = d2.replace('[', '')
    d4 = d3.replace(']', '')
    d5 = d4.replace(')', '')
    d6 = d5.replace(',', '')
    d7 = d6.replace(' ', '')
    with open(f"{d_isim}.txt", "w+") as d:
        print(d7, file=d)
