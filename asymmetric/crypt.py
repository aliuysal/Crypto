import os,random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

def encrypt(key,filename):
    size=64*1024
    ofile="ENC"+filename
    fsize=str(os.path.getsize(filename)).zfill(16)
    IV=''

    for i in range(16):
        IV+=chr(random.randint(0,0xFF))
    encryptor=AES.new(key,AES.MODE_CBC,IV)
    with open(filename,'rb') as ifile:
        with open(ofile,'wb') as efile:
            efile.write(fsize)
            efile.write(IV)

            while True:
                chn=ifile.read(size)

                if len(chn)==0:
                    break
                elif len(chn)%16 !=0:
                    chn += ' '*(16-(len(chn)%16))
                efile.write(encryptor.encrypt(chn))



def decrypt(key,filename):
    size=64*1024
    ofile=filename[3:]


    with open(filename,'rb') as ifile:
        size1=long(ifile.read(16))
        IV=ifile.read(16)

        decryptor=AES.new(key,AES.MODE_CBC,IV)

        with open(ofile,'wb') as efile:
            while True:
                chn=ifile.read(size)
                if len(chn)==0:
                    break
                efile.write(decryptor.decrypt(chn))
            efile.truncate(size1)
def getKey(password):
    hasher=SHA256.new(password)
    return hasher.digest()


def Main():
    choice=raw_input("Encrypt file (E/e) or decryptfile(D/d):")

    if choice=='E' or choice=='e':
        try:
            
            filename=raw_input("encrypt file:")
            password=raw_input("password:")
            encrypt(getKey(password),filename)
            print "Done."
        except:
            pass
    elif choice=='D' or choice=='d':
        try:

            filename=raw_input("decrypt file:")
            password=raw_input("password:")
            decrypt(getKey(password),filename)
            print "Done."
        except:
            pass
    else:
        print "no selected.."


if __name__=='__main__':
    Main()







