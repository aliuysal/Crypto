from random import randint

#with open("benioku.txt","r") as files:
#    print(files.read()
files =open("benioku.txt","r")

kelime=""
text = []
drt=[]
sayac=0
for i in files:
    text.append(i.replace('\n', '').replace(' ', ''))
    
for j in text:
    kelime=kelime+j
while(sayac<len(kelime)):
    drt.append(kelime[sayac:sayac+4])

    sayac=sayac+4

print(drt)
drt[::2],drt[1::2]=drt[1::2],drt[::2]

#''.join(drt)
print(drt)

'''klm=[]

sy=0


for a in drt:
    klm.insert(sy,a[::-1])
    sy=sy+1

print(klm)
'''

'''
yaz =open("BENIOKU.txt","w")

for l in drt:
    yaz.write(l)

'''




'''
while (len(num)<len(drt)):
    new =randint(0,len(drt))
    if new in num:
        continue
    else:
        num.append(new)

'''










