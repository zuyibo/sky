class Person:
    nickName = '人类'

    def __init__(self, inName, inAge, inWeight):
        self.name = inName
        self.age = inAge
        self.weight = inWeight

    def eat(self):
        self.weight += 10
        print('我在吃饭！---我立马重了10斤', self.weight)

    @classmethod
    def tell(cls):
        print('我是类方法')

    @staticmethod
    def run():
        print('---我是类方法--')



Person('tom', 30, 160).eat()
Person.run()
