import time
import hashlib
import unicodedata

class Block:
    def __init__(self, message, pre):
        has = hashlib.md5()
        self.message = message
        self.created_time = int(time.time()) 
        self.pre = pre
        has.update(message.encode())
        has.update(str(self.created_time).encode())
        has.update(str(pre).encode())
        self.id = has.hexdigest()
    
    def view(self):
        print('message: ', self.message, ' created time: ', self.created_time)

    def view_meta(self):
        print('id: ', self.id, 'message: ', self.message, 'pre: ', self.pre)
    
    def verify(self):
        has = hashlib.md5()
        has.update(self.message.encode())
        has.update(str(self.created_time).encode())
        has.update(str(self.pre).encode())
        if has.hexdigest() == self.id:
            return True
        else:
            return False