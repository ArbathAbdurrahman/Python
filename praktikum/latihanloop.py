# a:int=1
# b:int=2
# n:int=int(input("masukan angka : "))

# for i in range(1, n + 1):
#     Un = a + (i - 1) * b
#     print(Un, end=' ')
# print()


# a:int=4
# r:int=3
# n:int=int(input("masukan angka : "))

# for i in range(1, n + 1):
#     Un = a * (r ** (i - 1))
#     print(Un, end=' ')
# print()

a:int = 1
b:int = 2

n: int = int(input("suku yang ingin diketahui adalah : "))

for i in range(n,n+1) :
  un = a +(i-1)*b
  print(un,end ='')
  
print()