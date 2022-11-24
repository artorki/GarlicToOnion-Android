# Garlic To Onion / Port Scanner


import socket
from time import sleep

from Bbanner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def port_scanner() :
    
    banner ()
          
    sleep (0.05)
    print (" •–(Port Scanner )–––––––––")


    sleep (0.05)
    print (yellow)
    print (" [~] Type a IP:")
    
    sleep (0.05)
    print (white)
    ip = input (" >>> ")
    
    if ip == 0 :
        break
    
    
    port = [22 , 21 , 23 , 25 , 53 , 80 , 443 , 3389 , 8080 , 9150]
    
    print()

    def pscan (p) :
        
        try :
            
            s = socket.socket (socket.AF_INET ,  socket.SOCK_STREAM)
            s.connect ((ip , i))
            
            return True

                 
        except :
            
            return False
           
        if pscan (i) :
            print(green , "[+] Port {} is open".format (i))