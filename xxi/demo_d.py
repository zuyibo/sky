
# str1 = "1231213347845713824718237489123748343246217489132"
# str11 = int(str1)
# str2 = "623478573127438912743892017489132748172341324132"
# str22 = int(str2)
# a = str11 + str22
# print('数据类型-->', type(a), str(a))

# import copy
# alist = [10,20,[55,66]]
# blist = copy.copy(alist)
# blist.append(30)
# # blist[-1].append(30)
# print('blist->: ',blist,'id->:',id(blist))
# print('alist->: ',alist,'id->:',id(alist))
'''不可变对象'''
# a = 30
# b = a
# print('a内存地址：',id(a),'b内存地址：',id(b))
# print('a打印：',a,'b内打印：',b)
# a = 'hello'
# print('a内存地址：',id(a),'b内存地址：',id(b))
# print('a打印：',a,'b内打印：',b)

# '''可变对象'''
# c = [1,2,3,4]
# d = c
# c = [88,99]
# print('c等于：',c,'d等于',d)

# import copy
# a = [(1, 2, (3, 4))]
# copy_a = copy.deepcopy(a)
# print(id(a), id(copy_a))
import requests

host = 'http://127.0.0.1:80'
api_url = f'{host}/api/mgr/sq_mgr/'
header = {'Content-Type':  'application/x-www-form-urlencoded'}
payload = {"action": "add_course",
           "data": """{
                "name":"生理课",
              "desc":"生理课课程",
              "display_idx":"4"
               }"""
           }
res = requests.post(api_url, payload,header)
print(res)
