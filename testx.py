import hashlib

def some(mess):
    m = hashlib.md5()
    m.update(mess.encode())
    print(m.digest())

some('tung')