#Jövedelemszámítási feladat
print("Jövedelemszámítás\n")
kor = int(input("Hány éves vagy?"))
if kor > 25:
    gyerek = input("Van 3 gyereked és Nő vagy (igen/nem?)")
brutto = int(input("Mennyi a brutto jövedelmed?"))
if kor <= 25 or gyerek in["igen", "Igen", "i", "I"]:
    if brutto > 500000:
        szja = (brutto-500000) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15

print("SZJA:".ljust(20, "-"), str(int(szja)).rjust(10, "-"), sep="")
print("Nyugdíj:".ljust(20, "-"), str(int(brutto * 0.1)).rjust(10, "-"), sep="")
print("Eü:".ljust(20, "-"), str(int(brutto * 0.07)).rjust(10, "-"), sep="")
print("Munkan:".ljust(20, "-"), str(int(brutto * 0.015)).rjust(10, "-"), sep="")
print("\nNetto:".ljust(20, "-"), str(int(brutto - (brutto* 0.185) - szja)).rjust(10, "-"), sep="")
