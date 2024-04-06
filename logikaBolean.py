# not, or, and, xor

a = True
b = False
w = not a
x = a or b
y = a and b
z = a ^ b

print('data a = ', a)
print('not a =',w)
print(a, 'or',b, '=',x) #jika salah satu true maka true
print(a, 'and',b, '=',y) #jika salah satu false maka false
print(a, 'Xor',b,'=', z) #jika kedua nilai sama maka false jika beda maka true