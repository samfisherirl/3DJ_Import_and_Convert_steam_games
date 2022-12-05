import os
import shutil
import urllib.request
import requests
import py

final = []
urltotxt = {}
shortcuts = {}


dirname = os.path.dirname(__file__)

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
for filename in os.listdir(desktop):
	f = os.path.join(desktop, filename)
	# checking if it is a file
	if os.path.isfile(f):
		split_tup = os.path.splitext(f)
		if split_tup[1] == '.url':
			shortcuts[os.path.basename(f)] = f

for key, val in shortcuts.items():
	print(key, val)
	urltotxt[key] = (dirname + '\\bin\\' + key + '.txt')
	shutil.copy(val, (urltotxt[key]))

for key, val in urltotxt.items():
	with open(val, "r+") as f:
		lines = f.readlines()
		f.seek(0)
		for line in lines:
			if "steam://rungameid/" in line:
					id = line.split("steam://rungameid/")[1]
					print(id)
					try:
						py.Br.DL(str(id))
					except:
						print("er")
					r = requests.get(
						("".join(['https://steamdb.info/app/' + id + '/config/'])),
						stream=True,
						headers={'User-agent': 'Mozilla/5.0'})
					open('id.txt', 'wb').write(r.content)

					final.append(key + " ==> ==> " + line)
					break

with open("final.txt", "w") as f:
	for i in final:
		f.write(i + '\n')

os.system(f'\"{dirname}\\final.txt\"')
