import csv
import time
import requests
import hashlib


url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
f = 'zh'
to = 'en'
appid = 20230122001536890
salt = 1435660288


def readcsv(filepath):
    mylist = []
    with open(filepath, 'r', encoding='gbk') as f:
        csvobj = csv.reader(f)
        for i in csvobj:
            mylist.append(i)
    return mylist


def writecsv(filepath, mylist):
    with open(filepath, 'w', encoding='gbk', newline="") as f:
        csvobj = csv.writer(f)
        for i in mylist:
            csvobj.writerow(i)


def tbaidu():
    csvlist = readcsv("data.csv")
    result = [["Chinese", "English"]]
    for row in csvlist:
        if row[0] == 'Chinese':
            continue
        q = row[0]
        sign = hashlib.md5((str(appid) + q + str(salt) + 'NYc5tKmC1cVGuquHx1BL').encode('utf8')).hexdigest()
        print(sign)
        full_resquest = f'{url}?q={q}&from={f}&to={to}&appid={appid}&salt={salt}&sign={sign}'
        res = requests.get(full_resquest)
        resjson = res.json()
        print(resjson)
        templist = [resjson['trans_result'][0]['src'], resjson['trans_result'][0]['dst']]
        result.append(templist)
        time.sleep(2)
    print(result)
    writecsv("datares.csv", result)


tbaidu()
