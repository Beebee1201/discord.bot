import re
import time
import random
import numpy as np
import requests as rq

url = 'https://docs.google.com/forms/u/3/d/e/1FAIpQLSc5cqrV7FXz1ZrUAGNfXhTToxhxZj4Iqxt4A181h24Xt4Tnmg/formResponse'

payload = [
{
'entry.504834344': '103',
'dlut': '1630586025123',
'hud': 'true',
'fvv': '1',
'draftResponse': '[]',
'pageHistory': '0',
'token': 'CA62pnsBAAA.12955T5jNmardxZYg7V64w.9qfARv35na99YWLz675N2w',
'fbzx': '-6414505224175029536',
'continue': '1',
},
{
'entry.1825098563': '陳立峰',
'dlut': '1630586138146',
'hud': 'true',
'fvv': '1',
'draftResponse': '[]',
'pageHistory': '0,1',
'token': 'ycG7pnsBAAA.12955T5jNmardxZYg7V64w.lIh8v2m4mlkQxVFCX4YLhw',
'fbzx': '-6414505224175029536',
'continue': '1',
},
{
'entry.1077843025': '選項 1',
'dlut': '1630585292045',
'hud': 'true',
'fvv': '1',
'draftResponse': '[]',
'pageHistory': '0,1,2',
'token': 'LmCrpnsBAAA.bANpXaRhUyLIM1g9qIs-OA.vZjOX683QX6IPw8pKZN72w',
'fbzx': '-6414505224175029536',

}
]

login_url = 'https://accounts.google.com/ServiceLoginAuth'
login_data = {'Email': 'boss120194@gmail.com', 'Passwd': 'boss20051201'}
session = rq.session()
session.post(login_url, data=login_data)

print('登入成功')
for i in range(3): 
    res = rq.post(url, data=payload[i])
    res.raise_for_status()
    time.sleep(1)
    print('第%d頁完成'% i)