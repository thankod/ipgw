import requests
url1 = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
url2 = 'http://ipgw.neu.edu.cn/include/auth_action.php?k=5874'
url3 = 'http://ipgw.neu.edu.cn/include/auth_action.php'
login_data = {"username":"username", "password":"password","action":"login", "ac_id": 1, "save_me": 0}
logout_data = {"username":"username", "password":"password","action":"logout", "ajax": 1}
info_data = {"action":"get_online_info", "key": "5874"}
headers = {"User_Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36"}

requests.post(url3, data = logout_data, headers = headers)

requests.post(url1, data = login_data, headers = headers)

t = requests.post(url2, data = info_data, headers = headers)


list = t.text.split(',')
G = int(list[0]) // (1024 * 1024 * 1024)
M = (int(list[0]) % (1024 * 1024 * 1024)) // (1024 * 1024)
Hour = int(list[1]) // (60 * 60)
Minute = (int(list[1]) % (60 * 60)) // 60
Second = (int(list[1]) % (60 * 60)) % 60
res = list[2]

print("成功登陆！")
print("已用流量: %sG %sM" %(G, M))
print("已用时长: %s时%s分%s秒" %(Hour, Minute, Second))
print("剩余余额: " + res)

input()