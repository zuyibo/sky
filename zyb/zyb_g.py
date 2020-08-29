# Tiger   nickName inWeight roar feed  SouTiger

class Tiger:
    nickName = '老虎'

    def __init__(self,inWeight):
        self.weight = inWeight

    def roar(self):
        self.weight -=5
        print('我是老虎，体重减少5斤')

    def feed(self,food):
        if food == '肉':
            self.weight += 10
            print('我是老虎体重，重了10斤')
        else:
            self.weight -= 10
            print('我是老虎体重，少了10斤')




class SouTiger(Tiger):
    def __init__(self,inWeight,inAge):
        Tiger.__init__(self,inWeight)
        self.age = inAge

s1  = SouTiger(300,20)
s1.roar()
print(s1.weight,s1.age)