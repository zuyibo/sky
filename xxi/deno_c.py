filedir = r"C:\Users\18836\Desktop\sq1.txt"
fo = open(filedir,'rb')
print(fo.read())
print('操作前--->',fo.tell())
print(fo.read(2))
print('操作后--->',fo.tell())

fo.seek(1,1)
print('seek后--->',fo.tell())