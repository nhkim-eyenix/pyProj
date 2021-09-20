class Myclass:
    def __init__(self, name):
        self.name = name
        print('Created Creator')
    def sayHello(self, name):
        print('Hello, %s' %(name))

    def getName(self):
        print(self.name)

obj = Myclass('Tow')
obj.getName()