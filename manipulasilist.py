data = ["python","css","html","django"]
data_0 = data[0]
print(f"data pertama adalah {data_0}")
data_0 = data[-1]
print(f"data terakhir adalah {data_0}")
data_0 = len(data)
print(f"panjang data adalah {data_0}")

#manipulasi data list
print(f"data sebelum diambah : \n{data}")
data.insert(1,"shell")#menurut index [1]
print(f"data sesudah ditambah :\n{data}")
data.append("javascript")#menabah data di akhir list
print(f"data ditambah di akhir : \n{data}")

#menambah list dengan list
data_baru = ["ruby","laravel","react"]
data.extend(data_baru)
print(f"list ditambah list : \n{data}")

#mengubah data
data[5] = "php"
print(f"data setelah dirubah : \n {data}")
data.remove("python")#harus sesuai
print(f"data setelah dihapus : \n {data}")
data.pop()
print(f"data paling belakang dihapus : \n {data}")
data_0 = data.pop()
print(f"data terakhir adalah {data_0}")