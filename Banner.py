# Garlic To Onion / Banner


from time import sleep
import os , time , requests


cyan , red = "\033[96m" , "\033[91m"


def banner() :


    num = 10

    while True :
   
        try :

            requests.get ('http://google.com')
            break
        
        except :

            if num == -1 :
                print()
                exit ()
            
            os.system ('clear')
        
            print (red , '[!] No Network Connection')
            print (' [!] Another {} seconds closes'.format (num))
        
        num = num-1
        time.sleep (0.95)


    os.system ("clear")

    sleep (0.05)
    print (cyan , """
 ______________________________________________________________________

 .d88b            8 w         88888          .d88b.       w             
 8P www .d88 8d8b 8 w .d8b      8   .d8b.    8P  Y8 8d8b. w .d8b. 8d8b. 
 8b  d8 8  8 8P   8 8 8         8   8' .8    8b  d8 8P Y8 8 8' .8 8P Y8 
 `Y88P' `Y88 8    8 8 `Y8P      8   `Y8P'    `Y88P' 8   8 8 `Y8P' 8   8 

  [ Mini Data Collection Tool ]  [OS: Android]  [ Developer: Artorki ]
 ______________________________________________________________________
""")
