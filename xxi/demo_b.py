# import traceback
# def f3():
#     print('in f3 - begin')
#     b = 4 / 0
#     print('in f3 - end')
#
#
# def f2():
#     print('in f2 -begin')
#     f3()
#     print('in f2 -end')
#
#
# def f1():
#     print('in f1 -begin')
#     f2()
#     print('in f1 -end')
#
#
# f1()

# try:
#     fo = open('xxx')
# except:
#     print('asdas')
# class NameTooLongError(Exception):
#     err = 'name.long'
#     print('NameTooLongError')
#     def methFun(self):
#         pass
#
#
# class NameTooShortError(Exception):
#     print('NameTooShortError')
#
# def inputName():
#     name = input(('请输入用户名：'))
#     if len(name) > 10:
#         raise NameTooShortError
#     elif len(name) <5:
#         raise NameTooShortError
#
# try:
#     inputName()
# except NameTooShortError:
#     print('您输入的用户名太短')
# except NameTooLongError as e:
#     print('您输入的用户名太长',e.err)
#     e.methFun()

# tel = input('请输入手机号!')
# assert len(tel) == 1 or len(tel) == 2,'手机数位有误'
# print('我在处理')

# for one in range(0,3):
#     if one == 2:
#         raise ValueError


