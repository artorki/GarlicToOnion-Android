# @artorki


from time import sleep

from banner import banner
import connection
import libs


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


while True :
   
    banner()
   
    sleep (0.05)
    print (white , "•–(Home)–––––––––")


    sleep (0.05)
    print (yellow)
    print (" [01] URL To IP")
    sleep (0.05)
    print (" [02] Cloud Flare")
    sleep (0.05)
    print (" [03] IP Location")
    sleep (0.05)
    print (" [04] Port Scanner")
    sleep (0.05)
    print (" [05] Whois")
    sleep (0.05)
    print (" [00] Exit")

    sleep (0.05)
    print (white)
    h_input = input (" >>> ")

    if h_input == "" :
        print (red , "\n [!] Error")
        sleep (5)


    elif h_input == "1"  or h_input == "01" :
        from URLToIP import url_ip
        url_ip()
    
    elif h_input == "2" or h_input == "02" :
        from CloudFlare import cloud_flare
        cloud_flare()
        
    elif h_input == "3" or h_input == "03" :
        from IPLocation import ip_location  
        ip_location()

    elif h_input == "4" or h_input == "04" :
        from PortScanner import port_scanner
        port_scanner()

    elif h_input == "5" or h_input == "05" :
        from Whois import whois
        whois()
    
    elif h_input == "0" :
        exit()

    else:
        print (red , "\n [!] Error \n")
        exit()
    
    
input()
