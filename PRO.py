import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from MAX64 import buy
 
        buy()
 
 
 
elif bit == "32bit":
 
        from MAX32 import buy
 
        buy()