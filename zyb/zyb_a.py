yd = [137]

tel = input('请输入手机号：')

if not tel.isdigit():
    print('非数字')

elif len(tel) ==11:
    temp = int(tel[0:3])
    if temp in yd:
        print('移动')
    else:
        print('识别不出')

else:
    print('位数不对')