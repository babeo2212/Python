import requests

# r = requests.get('https://imgs.xkcd.com/comics/python.png')
# # with open('comic.png', 'wb') as f:
# #     f.write(r.content) # write a picture
# print(r.status_code) #200 is respond from the site means success, 300 is redirect, 400 cannot access , 500 server error
# print(r.ok) # True if less than 400 respond
# print(r.headers)

# payload = {'page': 3, 'count': 25}
# r = requests.get('https://httpbin.org/get', params=payload)
# print(r.url) #get the correct url with given arguments

payload = {'username': 2, 'password': 25}
r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text) #post data

r_dict = r.json()
print(r_dict['form'])

