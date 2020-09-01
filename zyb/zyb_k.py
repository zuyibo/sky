import requests
Host = 'http://127.0.0.1:80'
api_url = f'{Host}/api/mgr/sq_mgr/'
header = {'Content-Type':'application/x-www-form-urlencoded'}
import re
payload = {
        'action':'add_course',
        'data':'''{"name":"初中化学",
               "desc":"初中化学课程",
               "display_idx":"4"}'''
}


reps = requests.post(api_url,json=payload)
reps.encoding = 'unicode_escape'
print(reps.text)