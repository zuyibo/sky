class Tiger:
    nickName = '老虎'
    #如果这个属性每个实例可以不一样--实例属性
    def __init__(self,inWeight):
        self.weight = inWeight

    #叫--判断该方法是不是与实例有关系--看是否涉及到实例属性
    def roar(self):
        print('我是老虎--wow---体重减少5斤！')
        self.weight -= 5
    #喂食操作
    def feed(self,food):
        if food == '肉':
            self.weight += 10
            print('恭喜，喂食正确，体重增加10斤')
        else:
            self.weight -= 10
            print('抱歉，喂食错误，体重减少10斤')


class SouTiger(Tiger):
    def __init__(self,inWeight,inName):
        Tiger.__init__(self,inWeight)#super.__init__(self,inWeight)
        self.name = inName

s1 = SouTiger(200,'moco')
print(s1.nickName,s1.weight,s1.name)
s1.roar()
