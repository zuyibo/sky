import  traceback

while True:
    num = input('请输入')
    try:
        print(100 / int(num))
    # except ZeroDivisionError:
    #     print('不能为0')
    # except ValueError:
    #     print('一定是数字')

    except:
        print('结果\n '+traceback.format_exc())

