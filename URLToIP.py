# Garlic To Onion / URL To IP


import socket
from os import system
from time import sleep

from Banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def url_ip() :

    while True :
    
    banner()
    
    sleep (0.05)
    print (white , " •–(Reverse IP)––––––––– \n")


    sleep (0.05)
    print (yellow , "[~] Type a URL:")
       
    sleep (0.05)
    print (white)
    url = input (" >>> ").lower ()
        
    if url == "0" :
        break

        
    try :
        
        ip = socket.gethostbyname (url)
        sleep (0.05)
        print (green , "\n [+] " , ip)
        

    except :

        print (red , "\n Error")


    input ()
