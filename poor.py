import os
try:
  import requests
  import re
  import sys
except:
   os.system("pip install requests")
   os.system("pip install sys")
   os.system("pip install re")  

def robot():
    print('''
    
    \033[0;31m\       _           _       
           | |         | |      
  _ __ ___ | |__   ___ | |_ ___ 
 | '__/ _ \| '_ \ / _ \| __/ __|
 | | | (_) | |_) | (_) | |_\__ \
 |_|  \___/|_.__/ \___/ \__|___/
                                
                                
''')
    web = str(input("Enter Url [https://example.com]> "))

    domo = web+"/robots.txt"

    try:
       page = requests.get(domo,"html.parser").text

       hidd = re.findall("Disallow\: \S{1,}",page)

       for i in hidd:
          link = "[+] " + web+i[10:]
          print(link)
    except:
      print("EXIT !!!!")  
def xss():
   print('''

   \033[0;32m\                           
  _  __ ___ ___ 
  \ \/ / __/ __|
   >  <\__ \__ \
  /_/\_\___/___/
                
                
''')
   tar = input("Enter Target Url + [/id?=] , [https://example.com/id?=] > ")

   pay = "<script>alert('went xss');</script>"

   req = requests.get(tar+pay,"html.parser").text

   if pay in req:
    print("Discoversd Xxs ")
   else:
    print('No Found !')

def sud_domo():
  print('''

  
  \033[0;32m\

                _      _                       _       
               | |    | |                     (_)      
  ___ _   _  __| |  __| | ___  _ __ ___   ___  _ _ __  
 / __| | | |/ _` | / _` |/ _ \| '_ ` _ \ / _ \| | '_ \ 
 \__ \ |_| | (_| || (_| | (_) | | | | | | (_) | | | | |
 |___/\__,_|\__,_| \__,_|\___/|_| |_| |_|\___/|_|_| |_|
               ______                                  
              |______|                                 

  ''')  
  host = input("Enter Url [No Sud ] , [example.com]> ")

  f = open("list.txt","r")
  r = f.read()
  w = r.splitlines()

  for sud in w:
    domin = "https://"+sud+"."+host
     
    try:
        req = requests.get(domin,"html.parser")
        if req.status_code == 200:
            print("[+] There is Domin :" +domin)
    except requests.ConnectionError:
        pass
    except KeyboardInterrupt:
        print("\nExit!!")
        sys.exit()
  
def get_dir():
   print('''
   
     \033[0;32m\                     _          _ _      
                         | |        | (_)     
  ___  ___  __ _ _ __ ___| |__    __| |_ _ __ 
 / __|/ _ \/ _` | '__/ __| '_ \  / _` | | '__|
 \__ \  __/ (_| | | | (__| | | || (_| | | |   
 |___/\___|\__,_|_|  \___|_| |_| \__,_|_|_|   
                             ______           
                            |______|          

   ''')  
   erl = str(input("Enter Url Now [https://exampe.com] >  "))

   wordlist = open("wordlist1.txt","r")

   r = wordlist.read()

   wer = r.splitlines()

   try:
    for word in wer:
        url = erl+"/"+word
        abd = requests.get(url,"html.parser")
        if abd.status_code == 200:
            print("[+]_Found  "+ url)
   except:
    print("NO Found")
    sys.exit()        
    ##################
print('''
  \033[0;32m\

 ██▓███   ▒█████   ▒█████   ██▀███  
▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██   ██░▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░   ░▒ ░ ▒░
░░       ░ ░ ░ ▒  ░ ░ ░ ▒    ░░   ░ 
             ░ ░      ░ ░     ░     
                BY = MAHMOUD_EG | INSTA = MH__AFIF

''')
while True:
        print("\033[0;34m[01] \033[0;35mSearch xss in url \n")
        print("\033[0;34m[02] \033[0;35mAdd files robots in url \n")
        print("\033[0;34m[03] \033[0;35mCreate sud Domion in url\n")
        print("\033[0;34m[04] \033[0;35mSearch Wordlist Exhausted in the url\n")
        print("\033[0;34m[05] \033[0;35mAbout Tool\n")

        vpn = int(input("Choose Number > "))

        if vpn == 1:
         xss()
        elif vpn == 2:
         robot()
        elif vpn == 3:
         sud_domo()
        elif vpn == 4:
         get_dir()
        elif vpn == 5:
         print("MADA TOOL BY MAHMOUD_EG") 
        else:
         print("Sorry Try Again ")               

         