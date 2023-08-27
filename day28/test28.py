import requests
import hashlib
import json


url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
q = 'apple'
f = 'en'
to = 'zh'
appid = 20230122001536890
salt = 1435660288
sign = hashlib.md5((str(appid) + q + str(salt) + 'NYc5tKmC1cVGuquHx1BL').encode('utf8')).hexdigest()
print(sign)
full_resquest = f'{url}?q={q}&from={f}&to={to}&appid={appid}&salt={salt}&sign={sign}'
res = requests.get(full_resquest)
dic = json.loads(res.text)
print(dic)
for i in dic:
    if i == 'trans_result':
        print(dic['trans_result'][0]['dst'])