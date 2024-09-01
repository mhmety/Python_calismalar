title = "python ile programlama dersleri"

print(len(title))
print(title[0:6])
print(title[:6] + title[25:])
print(title[::-1])
ilkNot = int(input("ilk notu giriniz: "))
ikinciNot = int(input("ikinci notu giriniz: "))
ort = (ilkNot + ikinciNot)/2
print(f"çınar turan isimli öğrencisin 1.notu {ilkNot} 2.notu {ikinciNot} ve not ortalaması {ort} olarak hesaplanmıştır.")