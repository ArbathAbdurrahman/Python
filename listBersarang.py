#list besarang
listA = ["A",80,"lu"]
listB = ["B",50,"li"]
listC = ["C",30,"la"]
print(f"list biasa : {listA}")
bersarang = [listA,listB,listC]
print(f"Bersarang : {bersarang}")

#kegunaan list bersarang
i=0
panjang = len(bersarang)
data = ["agus",1,2,3,"bagus"]
for list in bersarang:
    print(f"nama\t : {list[0]}")
    print(f"nomor\t : {list[1]}")
    print(f"init\t : {list[2]}\n")
while i < panjang:
    print(f"data\t : {bersarang[i]}\n")
    i+=1

#simple loop
[print(f"simpel\t : {i}") for i in data]
#masalah dengan reference