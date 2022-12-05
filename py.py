import os
import shutil
import urllib.request
import requests
import io 

class Br:
	def __init__(self, url, func):
		self.url = url
		self.func = func
		self.header = {'User-agent': 'Mozilla/5.0'}


	def DL(self, id):
		r = requests.get(("http://webcache.googleusercontent.com/search?q=cache:https://steamdb.info/app/" + id + "/config/"), stream=True, headers=self.header) 
		with open('example.txt', 'w', encoding='utf-8') as my_file:
			my_file.write((r.content.decode("utf-8")))
		with open('example.txt', 'r', encoding='utf-8') as file:
			# contents = (file.read()).decode("utf-8")
			for line in file:
				if ".exe" in line:
					line = line.split("</code>")[0]
					line = line.split("<code>")[1]
					print(line)
					return line
	



