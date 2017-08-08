import requests
url1 = 'http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&'
url2 = 'http://ipgw.neu.edu.cn/include/auth_action.php?k=72013'
data1 = {"username":"yourid", "password":"yourpw","action":"login", "ac_id": 1, "save_me": 0}
requests.post(url1, data = data1)

data2 = {"action":"get_online_info", "key": "72013"}
t = requests.post(url2, data = data2)


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