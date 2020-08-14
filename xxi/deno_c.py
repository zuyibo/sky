import json
vipData = '''{
    "aac003":"tom",
    "crm003":"1",
    "tel":"135213123"
    }'''


print('转换前---->',type(vipData))
temp = json.loads(vipData)
temp['aac003'] = 'jack'
print('转换后---->',type(temp),temp)

print(json.dumps(temp),type(json.dumps(temp)))