import itertools
import fonksiyonlar

girdi= ""

print('#############################################')
print('+++++++++ SIFRE LISTE OLUSTURUCUSU ++++++++++')
print()
print('Lütfen Asagidaki modlardan seciminizi yapiniz:')
while girdi!="s":
    print("1) Isim-Soyisim bilgisi.")
    print("2) TC Bilgisi.")
    print("3) Nick bilgisi.")
    print("4) Telefon bilgisi.")
    print("5) Dogum Tarihi bilgisi.")
    print("6) Cep Telefonu Tus Takimina Bilgiyi Cevir.")
    print("7) Memleket bilgisi.")
    print("8) Evcil Hayvan bilgisi.")
    print("9) Noktalama bilgisi.")
    print("0) Diger bilgisi.")
    print("Baslatmak icin s'ye basiniz.")
    print()
    girdi = input("Seciminiz: ")

    if girdi == "1":
        fonksiyonlar.isim_soyisim()
    elif girdi == "2":
        fonksiyonlar.tc_bilgisi()
    elif girdi == "3":
        fonksiyonlar.nick_bilgisi()
    elif girdi == "4":
        fonksiyonlar.ceptelefonu_bilgisi()
    elif girdi == "5":
        fonksiyonlar.dogum_tarihi_bilgisi()
    elif girdi == "6":
        fonksiyonlar.cep_telefon_tipi()
    elif girdi == "7":
        fonksiyonlar.memleket_bilgisi()
    elif girdi == "8":
        fonksiyonlar.pet_bilgisi()
    elif girdi == "9":
        fonksiyonlar.noktalama()
    elif girdi == "0":
        fonksiyonlar.diger()

# Sifre Listesini olusturmaya basla:
print('+++++++++++++++++++++++++++++++++++++++++++++++++')
print("Sifre Listeniz olusturuluyor...")
print()
fonksiyonlar.olasilik()
print("#################################################")
print("+++++++++++ OLASILIKLAR HESAPLANDI ++++++++++++++")
fonksiyonlar.sifre_olustur()
