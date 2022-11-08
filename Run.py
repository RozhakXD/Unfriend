#!/usr/bin/env python3
import requests, time, random, os, re, sys, json
from rich import print as prints
from rich.console import Console
from requests.exceptions import ConnectionError
from requests.exceptions import TooManyRedirects
from rich.panel import Panel

# Banner
def Banner():
    if sys.platform.lower() == 'win':
        os.system('cls')
    else:
        os.system('clear')
    Console(width=40, style="bold deep_sky_blue4").print(Panel("""[bold red]╦ ╦┌┐┌┌─┐┬─┐┬┌─┐┌┐┌┌┬┐
[bold red]║ ║│││├┤ ├┬┘│├┤ │││ ││
[bold white]╚═╝┘└┘└  ┴└─┴└─┘┘└┘─┴┘
[reverse blue]Coded by Rozhak""", title="[bold green]Version 3.0"), justify="center")
    return 0
# Delay
def Delay(menit, detik):
    jumlah = (menit * 60 + detik)
    while (jumlah):
        menit, detik = divmod(jumlah, 60)
        prints(f"[bold green]#[bold white] {menit:02d}:{detik:02d}                              ", end='\r')
        time.sleep(1)
        jumlah -= 1
    return 0
# Convert
def Convert(cookie):
    with requests.Session() as r:
        url = ('https://business.facebook.com/business_locations')
        r.headers.update({
            'Host': 'business.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://m.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        response = r.get(url).text
        token = re.search('(EAAG\w+)', str(response)).group(1)
    return token
# Simpan
def Simpan(path, cookie):
    with open(path, 'w') as x:
        x.write(json.dumps({
            'Cookie': cookie
        }))
    x.close()
    return 0
# Login Utama
def Login_Utama():
    Banner()
    try:
        Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic white]Silahkan Masukan Cookie Akun Facebook Yang Mau Di Unfriend!", title="🙂"))
        cookie = Console().input("[bold green]#[bold white] Cookie : ")
        if 'c_user' not in str(cookie):
            Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic red]Periksa Cookie Facebooknya, Apakah Sudah Benar?", title="😡"));sys.exit()
        else:
            with requests.Session() as r:
                url = ('https://mbasic.facebook.com/home.php/?')
                r.headers.update({
                    'Host': 'mbasic.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
                })
                response = r.get(url, cookies = {'cookie': cookie}).text
                first_name = str(re.search('Keluar (.*?)</a>', str(response)).group(1)).replace('(','').replace(')','')
                Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic white]Welcome :[italic green] {first_name}", title="👋"));Simpan('Data/Cookie.json', cookie);time.sleep(3.1);Menu()
    except Exception as e:
        Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
# Menu
def Menu():
    Banner()
    try:
        cookie = json.loads(open('Data/Cookie.json','r').read())["Cookie"]
        with requests.Session() as r:
            url = ('https://mbasic.facebook.com/home.php/?')
            r.headers.update({
                'Host': 'mbasic.facebook.com',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
            })
            response = r.get(url, cookies = {'cookie': cookie}).text
            first_name = str(re.search('Keluar (.*?)</a>', str(response)).group(1)).replace('(','').replace(')','')
            Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic white]Welcome :[italic green] {first_name}", title="👋"))
    except Exception as e:
        Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));time.sleep(3.5);Login_Utama()
    Console(width=40, style="bold deep_sky_blue4").print(Panel("""[bold green]1[bold white]. Mengumpulkan ID Dari Teman
[bold green]2[bold white]. Mulai Menghapus Teman
[bold green]3[bold white]. Keluar Dari Program""", title="😎"))
    zhak = Console().input("[bold green]#[bold white] Choose : ")
    if zhak == '01' or zhak == '1':
        try:
            Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic white]Silahkan Masukan Cookie Akun Tumbal Untuk Mengumpulkan ID Akun Yang Mau Di Unfriend!", title="🙂"))
            userid = re.search('c_user=(\d+);', str(cookie)).group(1)
            cookie = Console().input("[bold green]#[bold white] Cookie : ")
            token = Convert(cookie)
            Dump(cookie, token, userid)
        except Exception as e:
            Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
    elif zhak == '02' or zhak == '2':
        try:
            Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic white]Silahkan Masukan Delay Agar Tidak Terblokir, Minimal 10 Detik Dan Maksimal 60 Detik!", title="🙂"))
            delay = int(Console().input("[bold green]#[bold white] Delay : "))
            if delay <= 9 or delay >= 61:
                Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic red]Delay Yang Kamu Masukan Tidak Ada Di Dalam Informasi!", title="😡"));sys.exit()
            else:
                userid = re.search('c_user=(\d+);', str(cookie)).group(1)
                Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic white]Jika Ingin Berhenti Menghapus Teman, Tekan ([italic green]CTRL + Z[italic white])", title="😆"))
                Hapus(cookie, userid, delay)
        except Exception as e:
            Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic red]{str(e).title()}", title="😡"));sys.exit()
    elif zhak == '03' or zhak == '3':
        try:
            Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic white]Sedang Menghapus Cookie Akun Facebook, Silahkan Tunggu!", title="🙂"));os.remove("Data/Cookie.json");sys.exit()
        except:sys.exit()
    else:
        Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic red]Sikahkan Periksa, Apakah Pilihan Yang Kamu Masukan Sudah Benar?", title="😡"));time.sleep(5.1);Menu()
# Dump
def Dump(cookie, token, userid):
    if os.path.exists("Data/Friends.txt") == False:
        pass
    else:
        os.remove("Data/Friends.txt")
    with requests.Session() as r:
        url = ('https://graph.facebook.com/v15.0/{}'.format(userid))
        r.headers.update({
            'Host': 'graph.facebook.com',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'x-requested-with': 'mark.via.gp',
            'sec-fetch-site': None,
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://graph.facebook.com/',
            'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': cookie
        })
        params = {
            'fields': 'friends.fields(id,name).limit(5000)',
            'access_token': token
        }
        response = r.get(url, params = params)
        if 'Request is not from' in str(response.text):
            cookie = json.loads(open('Data/Cookie.json','r').read())["Cookie"]
            token = Convert(cookie)
            Dump(cookie, token, "me")
        else:
            x = json.loads(response.text)
            for z in json.loads(response.text)['friends']['data']:
                uid, name = z['id'], z['name']
                open('Data/Friends.txt','a+').write(f"{uid}|{name}\n")
                prints(f"[bold green]#[bold white] Dump {uid}/{str(len(open('Data/Friends.txt','r').readlines()))} ID     ", end='\r')
            prints("                                      ", end='\r')
            Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[bold white]Jumlah Uid :[bold green] {str(len(open('Data/Friends.txt','r').readlines()))}", title="😆"))
            Console().input("[bold white][[bold green]Kembali[bold white]]");Menu()
# Hapus
def Hapus(cookie, userid, delay):
    try:
        friends = open('Data/Friends.txt','r').read().splitlines()
    except (IOError):
        Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic red]Sepertinya Kamu Belum Mengumpulkan ID Teman!", title="😡"));sys.exit()
    with requests.Session() as r:
        try:
            for z in friends:
                uid, name = z.split('|')[0], z.split('|')[1]
                if str(uid) in str(open('Data/Terhapus.txt','r').read()):
                    continue
                else:
                    Delay(0, delay)
                    url = ('https://mbasic.facebook.com/')
                    r.headers.update({
                        'Host': 'mbasic.facebook.com',
                        'cache-control': 'max-age=0',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'sec-fetch-site': 'same-origin',
                        'sec-fetch-mod': 'navigate',
                        'sec-fetch-user': '?1',
                        'sec-fetch-dest': 'document',
                        'referer': 'https://mbasic.facebook.com',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cookie': cookie
                    })
                    response = r.get(url).text
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response)).group(1)
                    url = ('https://mobile.facebook.com/a/friends/remove/?subject_id={}&unfriend_ref=bd_profile_button'.format(uid))

                    r.headers.clear()

                    r.headers.update({
                        'Host': 'mobile.facebook.com',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36',
                        'content-type': 'application/x-www-form-urlencoded',
                        'accept': '*/*',
                        'origin': 'https://m.facebook.com',
                        'sec-fetch-site': 'same-site',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-dest': 'empty',
                        'referer': 'https://m.facebook.com/',
                        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cookie': cookie
                    })
                    data = {
                        'fb_dtsg': fb_dtsg,
                        'jazoest': jazoest,
                        '__csr': '',
                        '__user': userid
                    }
                    response9 = r.post(url, data = data).text
                    if "for (;;);{\"payload\":" in str(response9):
                        Console(width=40, style="bold deep_sky_blue4").print(Panel(f"""[bold white][*] Status :[bold green] Sukses
[bold white][*] Name   : {name.title()}
[bold white][*] Userid : {uid}""", title="✅"))
                        open('Data/Terhapus.txt','a+').write(str(uid))
                    else:
                        Console(width=40, style="bold deep_sky_blue4").print(Panel(f"""[bold white][*] Status :[bold red] Sukses
[bold white][*] Name   : {name.title()}
[bold white][*] Userid : {uid}""", title="❌"));continue
            Console(width=40, style="bold deep_sky_blue4").print(Panel(f"[italic white]Berhasil Menghapus[italic green] {str(len(friends))}[italic white] Teman!", title="🙂"));sys.exit()
        except (TooManyRedirects):
            Console(width=40, style="bold deep_sky_blue4").print(Panel("[italic red]Sepertinya Akun Kamu Menggunakan Mode Gratis Jadi Tidak Bisa Menghapus Teman!", title="😡"));sys.exit()
        except (ConnectionError):
            prints("[bold green]#[bold red] Koneksi Kamu Bermasalah!     ", end='\r');time.sleep(7.5);Hapus(cookie, userid, delay)

if __name__=='__main__':
    os.system('git pull');Menu()
