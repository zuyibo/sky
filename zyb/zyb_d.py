# Person  inName inAge inWeight nickName

class Person:
    nickName = '人类'

    # def __init__(self,inName,inAge,inWeight):
    #     self.name = inName
    #     self.age = inAge
    #     self.weight = inWeight

    def run(self,inName,inAge,inWeight):
        self.name = inName
        self.age = inAge
        self.weight = inWeight

        print(f'我叫{self.name}今年{self.age}体重{self.weight}')

    def eat(self):
        self.weight += 10
        print('我在吃饭！---我立马重了10斤')


P = Person()
# P.eat('tom',30,180)
# P.run()
P.run('tom',30,180)
P.eat()