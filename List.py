data_a = [1,2,3,4,5]
print(data_a)

data_s = ["udin","supri","priscilla"]
print(data_s)

data_b = [True,False,True,False]
print(data_b)

#alternatif membuat list
data_r = range(1,10)
data_list = list(data_r)
print(data_list)

#list dengan for
listfor = [i for i in range(0,10)]
print(listfor)
listfor = [i**2 for i in range(0,10)]
print(listfor)
#list dengan for if
listif = [i for i in range(0,10) if i != 5]
print(listif)

listifz = [i for i in range(0,10) if i%2 == 0 ]
print(listifz)
listifx = [i for i in range(0,10) if i%2 == 1 ]
print(listifx)
listifx = [i**2 for i in range(0,10) if i%2 != 1 ]
print(listifx)