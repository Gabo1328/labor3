#Jövedelemszámítási feladat
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
gyerek = input("Van 3 gyereked és Nő vagy (igen/nem?)")
brutto = int(input("Mennyi a brutto jövedelmed?"))
if kor <= 25 or gyerek in["igen", "Igen", "i", "I"]:
    if brutto > 500000:
        szja = (brutto-500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print(f"SZJA: {szja}")
