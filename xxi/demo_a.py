import traceback
while True:
    num = input('input a number:')
    try:
        print('100/%s = %s'%(num,100.0/int(num)))

    except:
        print('我异常了',traceback.format_exc())