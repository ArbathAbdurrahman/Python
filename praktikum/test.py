#bagaimana Quiz Dicoding berjalan

answer = input("Submit Kode : ")
key = "harus sama persis"

def submitKode(answer,key,/):
    if answer == key :
        step = True
    else:
        step = False
    return step

lanjutModulBerikutnya = submitKode(answer,key)
print(f"apakah saya bisa lanjut ke modul berikutnya? {lanjutModulBerikutnya}")