# operasi yang dapat dilakukan dengan penyingkatan
# operasi diitambah assignment

a = 5 # adalah assignment
print('nilai a :', a)

a += 1 #artinya a = a + 1
print('nilai a += a + 1 :', a)

a -= 3 #artinya a = a - 1
print('nilai a -= a - 3 :', a)

a *= 5 #artinya a = a * 1
print('nilai a *= a * 5 :', a)

a /= 5 #artinya a = a / 1
print('nilai a /= a / 5 :', a)

#modulus floor fivision
b = 10
print('\nnilai b :', b)
b %= 3 #artinya b = b % 1 (sisa pembagian)
print('nilai b %= b % 3 :', b)

b = 10
print('\nnilai b :', b)
b //= 3 #artinya b = b // 1 (pembulatan pembagian)
print('nilai b //= b // 3 :', b)

#aritmatika pangkat eksponen
c = 10
print('\nnilai b :', c)
c **= 3 #artinya c = c ** 1 (perpangkatan)
print('nilai c **= c ** 3 :', c)

#operasi bitwise (|,&,^,~) geser(>>,<<)
x = True
print("\nnilai x :", x)
x |= False
print("nilai x |= false, nilai x menjadi", x)
x = False
print("nilai x =", x)
x |= False
print("nilai x |= False, nilai x menjadi", x)