isSick = False
temperature=float(input("masukan suhu : "))
maksimal = float(38)
minimal = float(35)
if temperature >= maksimal :
    print("Anda mengalami sakit demam.")
    isSick=True
elif temperature <= minimal :
    print("Anda terjangkit sakit hipotermia.")
    isSick = True
else :
    print("Suhu tubuh Anda normal.")

if isSick == True:
    print("Anda disarankan istirahat atau kunjungi dokter secepatnya.")