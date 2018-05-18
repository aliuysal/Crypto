from cryptography.fernet import Fernet
from random import randint 

'''
key = Fernet.generate_key()

print (key)

cypher=Fernet(key)

text=cypher.encrypt("Ali naber")

print (text)

plaintext=cypher.decrypt(text)

print (plaintext)
'''

adver='''
    Simetrik sifreleme icin secim yapiniz
    1-)Metni Sifreleyin
    2-)Sifreli Metni Cozme


'''
adver2='''
    Sifrelemek istediginiz metnin keyini belirleyiniz:
    (Key Seciminiz 0-10 arasinda olmalidir)

'''
adver3='''
    Sifreli metni cozmek icin secim yaptiginiz anahtari tekrar seciniz:
    sectiginiz anahtar 0-10 arasinda olmali...
'''


#def DosyaIslemi():
#    files2=open("keys.txt","w")
#    for i in range(0,10):
#        key=Fernet.generate_key()
#        files2.write(key)
#        files2.write("\n")
#DosyaIslemi()
def CypherText():
    print(adver)
    chose=int(raw_input("Seciminizi yapiniz:"))
    if chose==1:
        print(adver2)
        chose2=int(raw_input("Key seciminiz yapiniz:"))
        chs=[]
        files=open("keys.txt","r")
        for i in files:
            chs.append(i.replace('\n',''))
        
        if chose2 in range(0,10):
            cypher=Fernet(chs[chose2])
            strn=""
            files2=open("BENIOKU.txt","r")
            for k in files2:
                strn=strn+k
            cypher_text=cypher.encrypt(strn)
            files3=open("cypher.txt","w")
            files3.write(cypher_text)
        else:
            print("lutfen gecerli aralikta sayi giriniz..")
    elif chose==2:
        print(adver3)
        ch_keys=int(raw_input("Key secimini yapiniz:"))
        chs2=[]
        files4=open("keys.txt","r")
        for z in files4:
            chs2.append(z.replace('\n',''))
        if ch_keys in range(0,10):
            decs=Fernet(chs2[ch_keys])
            strn2=""
            files5=open("cypher.txt","r")
            for o in files5:
                strn2=strn2+o
            
            plain_text=decs.decrypt(strn2)
            files6=open("plain.txt","w")
            files6.write(plain_text)
    else:
        print("Farkli sayi girdiniz.. ")





CypherText()














