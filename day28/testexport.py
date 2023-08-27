import requests

url = "https://fanyi-api.baidu.com/api/trans/vip/translate?q=apple&from=en&to=zh&appid=20230122001536890&salt=1435660288&sign=0ba9fd94566fdeb51d72452228f0c4a0"

payload = {}
headers = {
  'Cookie': 'BAIDUID=CFC98D8C6430754DF13096C4E131CC38:FG=1; BIDUPSID=CFC98D8C6430754DDA8362136A50FB83; PSTM=1693125757'
}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)
resjson = response.json()
print(resjson)