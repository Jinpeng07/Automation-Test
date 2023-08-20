import hashlib


def MD5(str):
    return hashlib.md5(str.encode(encoding='utf8')).hexdigest()


print(MD5('123456'))