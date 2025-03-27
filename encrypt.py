#!/usr/bin/env python3
import os
import string
import time
def encrypt(message):
    letter1=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation+" "
    letter2=string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation+" "

    letter1=list(letter1)
    letter2=list(letter2)
    letter2.reverse()

    
    encrypt_mess=list()
    

    for mess in message:
        messa=""
        encrypted=list()
        for i in range(len(mess)):
            for j in range(len(letter2)):
                if mess[i]==letter1[j]:
                    encrypted.append(letter2[j])
        
        for i in range(len(encrypted)):
            messa+=encrypted[i]
        encrypt_mess.append(messa)
    with open("encrypt","w") as file:
        for word in encrypt_mess:
            file.write(word+'\n')
    print('Encrypt Successfully')

print("")
print(r"""                                                        ███╗░░░███╗███████╗░██████╗██╗░░░░░░█████╗░██╗░░██╗
                                                        ████╗░████║██╔════╝██╔════╝██║░░░░░██╔══██╗╚██╗██╔╝
                                                        ██╔████╔██║█████╗░░╚█████╗░██║░░░░░██║░░██║░╚███╔╝░
                                                        ██║╚██╔╝██║██╔══╝░░░╚═══██╗██║░░░░░██║░░██║░██╔██╗░
                                                        ██║░╚═╝░██║███████╗██████╔╝███████╗╚█████╔╝██╔╝╚██╗
                                                        ╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚══════╝░╚════╝░╚═╝░░╚═╝""")
print("")
print(r"""  _____                                         _     _                 
 | ____|  _ __     ___   _ __   _   _   _ __   | |_  (_)   ___    _ __  
 |  _|   | '_ \   / __| | '__| | | | | | '_ \  | __| | |  / _ \  | '_ \ 
 | |___  | | | | | (__  | |    | |_| | | |_) | | |_  | | | (_) | | | | |
 |_____| |_| |_|  \___| |_|     \__, | | .__/   \__| |_|  \___/  |_| |_|
                                |___/  |_|""")

n=0
while True:
    if n>3:
        print('')
        print('Wait 30 sec')
        for i in range(31):
            print(f'\r{i}',end="")
            time.sleep(1)
    password=input("\nPassword : ")
    while True:
        if password=='p455w0rd':
        
            message=list()
            with open('encrypt','r') as file:
                for line in file:
                    message.append(line.strip())
            encrypt(message)
            exit()
        else:
            print("       Wrong Password")
            n+=1
            break


            
