class Tiger:
    nickName = '老虎'

    def __init__(self,inWeight):
        self.weight = inWeight

    def roar(self):
        self.weight -= 5
        print(f'{Tiger.nickName}体重减少了5斤')

    def feed(self,food):
        if food == '肉':
            self.weight += 10
            print(f'{Tiger.nickName}胖了10斤')

t1 = Tiger(300)
t1.roar()
t1.feed('肉')