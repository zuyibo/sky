filedir1 = r"C:\Users\18836\Desktop\aa.txt"
filedir2 = r"C:\Users\18836\Desktop\aabb.txt"
with open(filedir1,encoding='utf8') as rFile, open(filedir2,'w') as wFile:
    lines = rFile.read().splitlines()
    for line in lines:
        temp = line.split(';')
        name = temp[0].split(':')[1].strip()
        salary = temp[1].split(':')[1].strip()
        salary = int(salary)

        info = f'name:{name:>6};salary:{salary:>6};tax:{int(salary*0.1):>6};income:{int(salary*0.9):>6}'
        print(info)
        wFile.write(info+'\n')