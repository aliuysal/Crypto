alert=''' 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 -----WELCOME TO CRYPTO MENU-----
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
print(alert)

def RawInput():

    name=raw_input("Please entry to name:")

    print("Welcome to "+name)
    while(True):

         chs='''
             Make Your Choice :
                    1-)Caesar Cipher 
                    2-)Keyword Cipher
                    3-)Column Cipher
                    4-)Exit
                      '''
         print(chs)
         choise=int(raw_input("Choose Your Number:"))
         if choise==1:
              print("------------Starting encoding or decoding")
         elif choise==2:
              print("------------Starting encoding or decoding")
         elif choise==3:
              print("------------Starting encoding or decoding")
         elif choise==4:
              break
"""
def CaesarCipher():
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    cipherText=""
    plainText=""
    chose=raw_input("Please choose encrypt or decrypt data (encrypt data :E or decrypt data :D):")
    if chose=="E" or chose == "e":
        texte=raw_input("Please entry your Plain Text:")
        for i in texte:
            cipherText=cipherText+alphabet[(alphabet.index(i)+3)%len(alphabet)]

        print("Caesar Cipher Text : "+cipherText)
    elif chose=="D" or chose =="d":
        textd=raw_input("Please entry your Cipher Text:")
        for l in textd:
            plainText=plainText+alphabet[(alphabet.index(l)-3)%len(alphabet)]

        print("Caesar Plain Text :"+plainText)



"""

if __name__=="__main__":
    RawInput()

