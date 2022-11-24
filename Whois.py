# Garlic To Onion / Whois


import socket
from socket import *
from time import sleep

from Banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def whois() :
    
    while True :  
    
        banner()
    
        sleep (0.05)
        print (" •–(Whois)––––––––– \n")


        sleep (0.05)
        print (yellow , "[~] Type a URL:")
    
        sleep (0.05)
        print (white)
        url = input(" >>> ") . lower()
        
        if url == "0" :
            break


        elif url[-3:] == "org" or "com" or "net" :
            server = "whois.internic.net"
        
        else :
            server =  "whois.iana.org"


        try :
            
            s = socket (socket.AF_INET , socket.SOCK_STREAM)
            s.connect ((server , 43))
            s.send ((url + "\r\n") . encode())
            output = s.recv(10000)
            
            print (green)
            print (output)
            
        except :
            
            print (red , "\n [!] Error")
            
       
        input()
