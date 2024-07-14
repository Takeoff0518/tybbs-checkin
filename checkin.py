import requests
import os

def check_in():
    url = 'https://bbs.66ccff.cc/wp-admin/ajax.php'
    headers = {
        'authority': 'bbs.66ccff.cc',
        'method': 'POST',
        'path': '/wp-admin/ajax.php',
        'scheme': 'https',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': os.getenv('BBS_COOKIE'),
        'Origin': 'https://bbs.66ccff.cc',
        'Referer': 'https://bbs.66ccff.cc/',
        'Sec-Ch-Ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'action': 'user_checkin'
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print('签到成功！')
        print("```json")
        print(response.json()) # 打印出来看看awa？
        print("```")
    else:
        print('签到失败！')
        print("```json")
        print(response.status_code, response.text)
        print("```")
        exit(1)

if __name__ == '__main__':
    check_in()
