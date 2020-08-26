# vipData = {
#     "aac003":"tom",
#     "tel":"13313313321"}

# import json
# temp = json.loads(vipData)
# print(temp)
#
# for a,b in vipData.items():
#     print(a,b)


# temp['aac003'] = 'jack'
# print(type(temp),temp)
# print(json.dumps(temp),type(json.dumps(temp)))


def test(a,**kwargs):
    print(a,kwargs)

test(1,**{'name':'tom'})