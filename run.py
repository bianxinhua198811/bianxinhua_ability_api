# @Time     :2019/10/12 11:25
# @Author   :dengyuting
# @File     :run.py
import requests

# s = requests.Session()

r = requests.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(r.text)
r = requests.get('https://httpbin.org/cookies')
print(r.text)



s = requests.Session()

r = s.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
print(r.text)
r = s.get('https://httpbin.org/cookies')
print(r.text)