print("cek piton")
# comment
"""multi
coment"""
#cara compile pthon agar lebih cepat
#buka cmd tulis python -m py_compile piton.py

#variabel
a = 5
b = 10
panjang = 100
print("Nilai a =", a + b * panjang)

#Tipe data angka satuan (integer)
data_integer = 1
print("data = ", data_integer)
print("data =", data_integer, ", bertipe =", type(data_integer))

# tipe data angka dengan koma (float)
data_float = 3.8
print("data =", data_float)
print("tipe data", type(data_float))

# tipe data karakter (string)
data_string = "piton"
print("data = ", data_string)
print("tipe", type(data_string))

# tipe data biner true/false (boolean) akan false jika 0 atau string kosong
data_bool = True 
print("data = ", data_bool)
print("tipe", type(data_bool))

# tipe data khusus 
# bilangan kompleks
data_complex = complex(3,7)
print("data = ", data_complex)
print("tipe", type(data_complex))

#tipe data dari bahasa C

from ctypes import c_double, c_char

data_c_double = c_double(5.5)
print("data =", data_c_double)
print("tipe=", type(data_c_double))

#cara merubah tipe data(casting)
print("====Casting float====")
data_float = 1.9
print("data= ", data_float, "type=",type(data_float))

data_int = int(data_float) #akan dibulatkan kebawah
data_str = str(data_float)
data_bool = bool(data_float)#akan False jika data_float = 0
print("data =",data_int, ",type=",type(data_int))
print("data =",data_str, ",type=",type(data_str))
print("data =",data_bool, ",type=",type(data_bool))