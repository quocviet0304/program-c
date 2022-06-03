import requests
import colorama
import random
from time import sleep
list_done = []
colorama.init()
with open('user.txt',mode = 'a+') as w :
	w.read()
with open('user.txt',mode = 'r') as r :
    get = r.read()
tach = get.split('\n')
if get == "":
	chon_nick = 'n'
else:
	for i in range(len(tach)-1):
		print(f"{i+1}" +"\033[1;36;31m * \033[39m" + "\033[1;36;33m"+tach[i].split('|')[0]+"\033[39m")
		print("		" + tach[i].split('|')[1])
	chon_nick = str(input('''
chọn nick có sẵn [ENTER]
nếu không [n]
nếu toàn bộ [all]
Đổi sao [d]
Vui lòng chọn : '''))
if chon_nick.lower() == 'n':
	add_nick = str(input('''Nhập tên , Authorization bởi dấu |
Nếu nhiều nick thì viết cách nhau bởi dấu phẩy:
'''))
	nick = add_nick.split(',')
	with open('user.txt',mode = 'a+') as w :
		for i in nick:
			w.write(i + '\n')
	for i in nick:
		try:
			headers_me = {
			    'Authorization': i.split('|')[1],
			    'Accept': 'application/json, text/plain, */*',
			    'Referer': 'https://app.golike.net/',

				}
			roll_call_code = requests.get("https://dev.golike.net/api/users/me",headers=headers_me)
			data = {
			    'token': roll_call_code.json()['data']['roll_call_code']}

			done = requests.post("https://dev.golike.net/api/event/roll-call",headers=headers_me,data=data)
			try:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message']+" > > > số dư : "+str(done.json()['data']['coin']))
			except:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message'])
		except:
			print(f"Xảy ra lỗi ở nick số {i}")

elif chon_nick.lower() == 'all':
	for i in range(len(tach) - 1):
		try:
			headers_me = {
				'Authorization': tach[i].split('|')[1],
				'Accept': 'application/json, text/plain, */*',
				'Referer': 'https://app.golike.net/',
				}
			roll_call_code = requests.get("https://dev.golike.net/api/users/me",headers=headers_me)

			data = {
				'token': roll_call_code.json()['data']['roll_call_code']}
			done = requests.post("https://dev.golike.net/api/event/roll-call",headers=headers_me,data=data)
			try:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message']+" > > > số dư : "+str(done.json()['data']['coin']))
			except:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message'])
		except:
			print(f"Xảy ra lỗi ở nick số {i+1}")

elif chon_nick.lower() == 'd':
	z = 0
	while True:
		z = z + 1
		if len(list_done) == len(tach) - 1:
			break
		for i in range(len(tach) - 1):
			if i in list_done:
				pass
			else:
				try:
					headers_me = {
						'Authorization': tach[i].split('|')[1],
						'Accept': 'application/json, text/plain, */*',
						'Referer': 'https://app.golike.net/',
						}
					# roll_call_code = requests.post('https://dev.golike.net/api/event/shop/redeem-rewards',headers=headers_me,params={'item_id': '2'})
					roll_call_code = requests.post('https://dev.golike.net/api/event/shop/redeem-rewards?item_id=2',headers=headers_me)
					try:
						print(f'[{z}] nick số [{i+1}]  ' + str(roll_call_code.json()['_fb']['new']))
					except:
						print(f'[{z}] nick số [{i+1}]  ' + roll_call_code.json()['message'])
					if  "Không đủ sao" in roll_call_code.json()['message']:
						list_done.append(i)
					
				except:

					print(f"Xảy ra lỗi ở nick số {i+1}")
					try:
						print(roll_call_code.json())
					except:
						pass
		print("---------------------------------------------------")
		sleep(random.uniform(5,7))
else:
	nhap = str(input('''Hãy số thứ tự nick bạn cần chạy nếu nhiều thì cách nhau [,] : '''))
	print(nhap.split(','))
	for i in nhap.split(','):
		try:
			headers_me = {
				'Authorization': tach[int(i)-1].split('|')[1],
				'Accept': 'application/json, text/plain, */*',
				'Referer': 'https://app.golike.net/',
				}
			roll_call_code = requests.get("https://dev.golike.net/api/users/me", headers=headers_me)

			data = {
				'token': roll_call_code.json()['data']['roll_call_code']}
			done = requests.post("https://dev.golike.net/api/event/roll-call", headers=headers_me, data=data)
			try:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message']+" > > > số dư : "+str(done.json()['data']['coin']))
			except:
				print(roll_call_code.json()['data']['username']+" > > > "+done.json()['message'])
		except:
			print(f"Xảy ra lỗi ở nick số {i}")
print("done")
input()

