data = "ini adalah string"
print(data)
print(type(data))

# single quote
data = 'single quote'
print(data)

# double quote
data = "double quote"
print(data)

# dua-duanya
data = '"dua quote"'
print(data)
data = "'dua quote'"
print(data)

#tanda \
print('mari shalat jum\'at')
print("C:\\user\\usin")
print("udin\t\t\ttab")
print("udin\bhapus1")
print("udin\nenter") #LF Line Feed (mac,linux,unix) bisa juga dengan """Enter"""
print("udin\rremove udin") #CR Carriage Return (commodore,acorn,lisp)
print("udin\r\ncombo") #CRLF(windows)
#String literal atau raw
print(r'C:\new \t\r\b\\Folder')
#multiline literal string
print("""
nama : udin
ras  : demonlord
umur : 8000th
""")
#multiline literal string dan raw
print(r"""
nama : udin
ras  : demonlord
umur : 8000th
wesite : www.udin/demonlord.com
""")