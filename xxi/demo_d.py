yd = [137,159]
lt = [166,167]
dx = [177,188]
tel = input('请输入你的手机号')

if not tel.isdigit():
    print('请输入纯数字')
elif len(tel) == 11:
    temp = int(tel[0:3])
    if temp in yd:
        print('移动')
    elif temp in lt:
        print('联通手机')
    elif temp in dx:
        print('电信手机')
    else:
        print('识别不出运营商')

else:
    print('位数不对')
