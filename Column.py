"""
Sabit bir sütun sayısı seçilir. Sonra bu sütun sayısına göre metin 
yazılır. Sütun sayısına göre seçilen bir anahtar kelime ise 
sütunların okunma sırasını gösterir. Örn: sütun sayısı 3 kelime 
KOD olsun. (Sıra alfabetik: D:1 K:2 O:3) 2,3,1 yazılır.
"""

keyword = input()
girdi = input()
kw = []
chars = []
sutun = []
for c in keyword:
    chars.append(c)


for i in range(len(chars)):
    minelem = min(chars)
    kw.append(minelem)
    chars.remove(minelem)

for k in range(len(kw)):
    column = ""
    j = k
    while j < len(girdi):
        column = column + girdi[j]
        j = j + len(kw)
        if j >= len(girdi):
            break
    sutun.append(column)

res = ""
for c in keyword:
    index = kw.index(c)
    res = res + sutun[index] 

print(res)
