# Garlic To Onion / Connection


import os , time , requests

from banner import banner

red = "\033[91m"


num = 10


while True:
   
    try :
        requests.get ('http://google.com')
        break
        
    except :
        if num == -1 :
            print()
            exit ()
            
            
        os.system ('clear')
        
        banner ()
        
        print (red , '[!] No Network Connection')
        print (' [!] Another {} seconds closes'.format (num))
        
        num = num-1
        time.sleep (0.95)