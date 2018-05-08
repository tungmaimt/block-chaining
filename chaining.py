from block import Block, time

class Chaining:
    def __init__(self):
        self.__chaining = [Block('root', 0)]
        self.anchor = None

    def append_block(self, message):
        self.__chaining.append(Block(message, self.__chaining[len(self.__chaining) - 1].id))

    def get_block(self, index):
        if index >= len(self.__chaining) or index < 0:
            print('index block is out of range or invalid')
        else:
            return self.__chaining[index]

    def view(self):
        for i in self.__chaining:
            i.view()

    def view_meta(self):
        for i in self.__chaining:
            i.view_meta()
    
    def verify(self):
        for i in self.__chaining:
            if (self.__chaining.index(i) == 0):
                continue
            if not i.verify():
                return False
            if i.pre == self.__chaining[self.__chaining.index(i) - 1].id:
                pass
            else:
                return False
        return True