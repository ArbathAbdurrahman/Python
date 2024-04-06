a = 10
b = 7

hasil = a + b
print(a,'+',b,'=',hasil)

hasil = a - b
print(a,'-',b,'=',hasil)

hasil = a * b
print(a,'*',b,'=',hasil)

hasil = a / b
print(a,'/',b,'=',hasil)

#pangkat
hasil = a ** b
print(a,'**',b,'=',hasil)

#modulus % hasil sisa
hasil = a % b
print(a,'%',b,'=',hasil)

#floor division (pembagian tanpa koma)
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi kurung akan lebih dahulu
'''
1. ()
2. **
3. * / ** % //
4. + -
'''
x = 3
y = 2
z = 4
hasil = x ** (y + z) / y - x % z // y
print(x,'**',(y,'+',z),'/',y,'-',x,'%',z,'//',y,'=',hasil)