import time
import hashlib
import unicodedata

class Block:
    global __gen_id
    def __init__(self, message, pre):
        has = hashlib.md5()
        self.message = message
        self.created_time = int(time.time()) 
        self.pre = pre
        has.update(unicodedata.normalize('NFKD', str(message)).encode())
        has.update(unicodedata.normalize('NFKD', str(self.created_time)).encode())
        has.update(unicodedata.normalize('NFKD', str(pre)).encode())
        self.id = has.hexdigest()
    
    def view(self):
        print('message: ', self.message, ' created time: ', self.created_time)

    def view_meta(self):
        print('id: ', self.id, 'message: ', self.message, 'pre: ', self.pre)
    
    def verify(self):
        has = hashlib.md5()
        has.update(unicodedata.normalize('NFKD', str(self.message)).encode())
        has.update(unicodedata.normalize('NFKD', str(self.created_time)).encode())
        has.update(unicodedata.normalize('NFKD', str(self.pre)).encode())
        if has.hexdigest() == self.id:
            return True
        else:
            return False