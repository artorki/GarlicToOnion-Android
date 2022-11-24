from time import sleep
from os import system


cyan = '\033[96m'


def banner () :
    system ("clear")
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
