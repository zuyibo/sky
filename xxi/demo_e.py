# boys = ['Mike','Jack','Tom']
# girls = ['Lisa','Linda','Mary']
#
# for boy in boys:
#     for girl in girls:
#         print('%s shake %s' %(boy,girl))

# beforetax = [10000,15000,8000,5000]
# aftertax = []
# for one in alist:
#     aftertax.append(one*0.9)
# print(aftertax)

# aftertax = [one*0.9 for one in beforetax]
# print(aftertax)

# boys = ['Mike','Jack','Tom']
# a = [one for one in boys]
# print(a)
# alist = [9,0,6,2]
# alist.sort(reverse=True)
# # print(alist)
# # alist.reverse()
# print(alist)

# alist = [3,5,7,2]
#
# for i in range(len(alist)-1):  #0,1,2
#     for j in range(len(alist)-1-i):  #3,2,1
#         if alist[j]>alist[j+1]:
#             alist[j],alist[j+1] = alist[j+1],alist[j]
#
# print(alist)
# Jack Green,  21 ; Mike Mos ,  9;
inStr = input('请输入学生的信息:')

info = inStr.split(';')
del info[-1]
for one in info:
    temp = one.split(',')
    name = temp[0].strip()
    age = int(temp[1].strip())
    print(f'{name:<20}:{age:0>2};')



