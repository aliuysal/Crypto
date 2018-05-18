#Ali Erdogan 14253027
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint


adver='''
    1-)Karmasiklastirma
    2-)Dagitma
    3-)Once Karistir Sonra Dagitma
    4-)Once Dagit Sonra Karistir
'''

def DosyaIslemi():
    files=open("benioku.txt","r")
    kelime=""
    text=[]
    drt=[]
    sayac=0
    for i in files:
        text.append(i.replace('\n','').replace(' ',''))
    for j in text:
        kelime=kelime+j
    while (sayac<len(kelime)):
        drt.append(kelime[sayac:sayac+4])
        sayac=sayac+4
    
    return drt

def Karistirma(kl):
    dlm=[]
    sy=0
    for l in kl:
        dlm.insert(sy,l[::-1])
        sy=sy+1
    return dlm

def Dagitma(mn):
    mn[::2],mn[1::2]=mn[1::2],mn[::2]
    ''.join(mn)
    c=mn
    return c



if __name__ =="__main__":
    print(adver)
    text=int(raw_input("Seciminizi yapiniz:"))
    if text==1:
        yaz=open("BENIOKU.txt","w")
        kl=DosyaIslemi()
        for i in Karistirma(kl):
            yaz.write(i)
    elif text==2:
        yaz2=open("BENIOKU.txt","w")
        sn=DosyaIslemi()
        for j in Dagitma(sn):
            yaz2.write(j)
    elif text==3:
        yaz3=open("BENIOKU.txt","w")
        ml=DosyaIslemi()
        tl=Karistirma(ml)
        for k in Dagitma(tl):
            yaz3.write(k)
    elif text==4:
        yaz4=open("BENIOKU.txt","w")
        sn=DosyaIslemi()
        for z in Dagitma(Karistirma(sn)):
            yaz4.write(z)
    else:
        print("Yanlis secim yaptiniz..")











#dl=DosyaIslemi()
#kl=Karistirma(dl)
#print(Karistirma(dl))
#print(Dagitma(dl))
#print(Dagitma(kl))
#print(Dagitma(Karistirma(dl)))




