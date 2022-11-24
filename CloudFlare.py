# Garlic To Onion / Cloud Flare


import socket
from os import system
from time import sleep
from ipapi import location as ipapi

from banner import banner


white , cyan , green , yellow , red = "\033[0;37m" , "\033[96m" , "\033[92m" , "\033[93m" , "\033[91m"


def cloud_flare () :

    while True :

    
        banner ()
 
        sleep (0.05)
        print (white , " •–(Cloud Flare)––––––––– \n")


        sleep (0.05)
        print (yellow , "[~] Type a Domain:")

        sleep (0.05)
        print (white)
        domain = input (" >>> ")
        
        if domain == "0" :
            break

       
        file = open ("sub.txt" , "r")
        sublist = file.read ()
        file.close ()
        
     
        try :
    
            ip = socket.gethostbyname (domain)
     
            sleep (0.05)
            print (green , "\n [+] " , domain , ">>>" , ip)
 
            dif1 = ip.split (".")
            dif1 = dif1[0] + dif1[1] + dif1[2]

        except :
      
            print (red , "\n Error")
            exit()
        
      
        sublist = sublist . split("\n")
 
        num = 0
    
  
        for i in sublist :
   
            num += 1
   
            try :
 
                url = i + "." + domain
                ip = socket.gethostbyname (url)
            
                dif2 = ip.split (".")
                dif2 = dif2[0] + dif2[1] + dif2[2]
              

                if  dif2 != dif1 :
                
                    bug = "[+]  " + num + "  |  " + url + "  >>>  " + ip
                
                    sleep (0.05)
                    print (yellow , bug)
                
                else :
                    print (green , "[+] " , num , " | " , url , " >>> " , ip)
      
            except :
                print (red , "[-] " , num , " | " , url)        

  
        print (yellow , "\n Finish")
    
        input()
