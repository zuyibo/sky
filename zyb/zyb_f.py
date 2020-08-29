class VipCustomer:
    welfare = '商品8折优惠券+生日礼券'
    def __init__(self,inName,inAge):
        self.name = inName
        self.age = inAge

    def shopping(self):
        print('-----<VIP用户江浙沪包邮>---')

class SvipCustomer(VipCustomer):
    def __init__(self,inName,inAge,inLevel):
        VipCustomer.__init__(self,inName,inAge)
        self.level = inLevel

    def shopping(self):
        print('-----<SVIP用户江浙沪包邮>---')