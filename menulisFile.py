#ketika di run maka akan otomatis membuat file bernama data_1.txt
with open('data_1.txt','w',encoding='utf-8') as file:
    file.write("ahmad")#ini akan tertimpa jika kita membuat lagi

#agar bida menambahkan file bisa menggunakan awalan mode write 'w'
#lalu selanjutnya kita bisa menggunakan mode append 'a'
with open('data_2.txt','w',encoding='utf-8') as file:
    file.write("nanang\n")
with open('data_2.txt','a',encoding='utf-8') as file:
    file.write("fauzan\n")
with open('data_2.txt','a',encoding='utf-8') as file:
    file.write("supri\n")
