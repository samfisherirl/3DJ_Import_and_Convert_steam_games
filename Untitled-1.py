import os
import shutil
import urllib.request
import requests
import io 

id = "1534900"

def DL(id):
	r = requests.get(("".join(['http://webcache.googleusercontent.com/search?q=cache:https://steamdb.info/app/', id, '/config/'])), stream=True, headers={'User-agent': 'Mozilla/5.0'}) 
	with open('example.txt', 'w', encoding='utf-8') as my_file:
		my_file.write((r.content.decode("utf-8")))
	with open('example.txt', 'r', encoding='utf-8') as file:
		# contents = (file.read()).decode("utf-8")
	for line in contents:
		if ".exe" in line:
			line = line.split("</code>")[0]
			line = line.split("<code>")[1]
			print(line)
			return line

