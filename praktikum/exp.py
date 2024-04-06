da = (float (input("a : ")))
db = (float (input("b : ")))

def kekurangan(a,b):
    if a>b:
        return a-b
    else:
        a+b

data = kekurangan(da,db)
print(f"a = {da} b = {db}")
print(f"kekurangan = {data}")