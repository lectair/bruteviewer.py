import requests
import sys
import time

try:
    media_code = sys.argv[1].split('/p/')[1].split('/')[0]
    delay = int(sys.argv[2])+0
    time.sleep(int(delay))
    print(f'MEDIA CODE: {media_code}\nDELAY: {delay}\n\nProcess:')
except IndexError:
    print('Usage:    python bruteviewer.py video_link delay_in_seconds\nExample:  python bruteviewer.py https://www.instagram.com/p/CAbMALKg0VM/ 3\n')
    sys.exit()
except ValueError:
    print('Please set a valid delay\nExample: python bruteviewer.py https://www.instagram.com/p/CAbMALKg0VM/ 3\n')
    sys.exit()
except NameError:
    print('Usage:    python bruteviewer.py video_link delay_in_seconds\nExample:  python bruteviewer.py https://www.instagram.com/p/CAbMALKg0VM/ 3\n')
    sys.exit()
except:
    print('Unknown exception ocurred.')

headers = {
    "Host":"sifresiz.instahile.co",
    "Accept":"application/json, text/javascript, /; q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "Accept-Language":"es-es",
    "Accept-Encoding":"gzip, deflate, br",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Origin":"https://sifresiz.instahile.co",
    "User-Agent":"LMAOOO",
    "Connection":"keep-alive",
    "Referer":"https://sifresiz.instahile.co/views",
    "Content-Length":"34",
    "Cookie":"INSERT_COOKIES_HERE"
}

params = {
    "media_code": media_code,
    "quantity": 30
}

while True:
    request = requests.post("https://sifresiz.instahile.co/c/views.php", data=params, headers=headers)
    response = request.text
    if "�" in response:
        print('Captcha!')
    elif "503 Service" in response:
        print('Error 503. Wait a minute while we reload...')
        time.sleep(15)
    else:
        print(response)
        time.sleep(int(delay))
