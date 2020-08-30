import requests
host = 'http://127.0.0.1:80'
api_url = f'{host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {
    'action':'add_course',
    'data':'''{
            "name":"恋爱学",
            "desc":"恋爱学学课程",
            "display_idx":"4"
            }'''
        }

reps = requests.post(api_url,data=payload,headers=header)
reps.encoding = 'unicode_escape'
print(reps.text)