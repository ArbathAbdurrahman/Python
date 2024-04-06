print(20*"=")
print("kalkulator")
print(20*"=")

satu = float(input("masukan angka :"))
op = input("[+-*/] : ")
dua = float(input("masukan angka :"))

if op == "+":
    hasil = satu + dua
    print(f"hasil = {hasil}")
elif op == "-":
    hasil = satu - dua
    print(f"hasil = {hasil}")
elif op == "/":
    hasil = satu * dua
    print(f"hasil = {hasil}")
elif op == "*":
    hasil = satu * dua
    print(f"hasil = {hasil}")
else :
    print("format yanga anda masukan salah")
