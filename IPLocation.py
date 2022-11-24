# Garlic To Onion / IP Location


from ipapi import location as ipapi
from time import sleep

from banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def ip_location() :

    while True :
        
        banner()
    
    
        sleep (0.05)
        print (" •–(IP Location)––––––––– \n")


        sleep (0.05)
        print (yellow , "[~] Type a IP:")
    
        print (white)
        ip = input (" >>> ")
    
        if ip == "0" :
            break
   
   
        try :
        
            loc = ipapi (ip)
            location = str(loc) . replace("," , "\n") . replace("{" , "") . replace("}" , "") . replace("'" , "")
            print (green , "\n" , location)
        
        except :
        
            print (red , "\n [!] Error")


        input()
