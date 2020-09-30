'''
 - Obiectiv -
Crearea unui json cu informatiile decoded pe baza fisierelor din directorul normal

 - Instructiuni -
Numele fisierelor ce incep cu 'interns' contin encodari base64 0
Numele fisierelor ce se termina cu 'interns' contin encodari base32 3
Numele fisierelor ce contin 'interns' ca al doilea sau al treilea cuvant contin encodari base16 1 2

Pentru fiecare fisier din directorul normal, json-ul final (flag) va contine:
	* nume = decodarea continutului
	* continut = numele fisierului original
	
ex: pentru fisierul 'interns_are_cool_devops' si continutul 'ZWFzeV9hcmVfdG9vX3Rhc2tz' se va crea entry {'easy_are_too_tasks': 'interns_are_cool_devops', ...}

Mentiuni: validarea se face cu jsonvalidator.py, ordine rezultata din 'sort_keys = True'

'''

# ----------------- NO CHANGE REQUIRED

import os
import base64
import json

pwd_path = os.path.dirname(os.path.realpath(__file__))
normal_path = os.path.join(pwd_path, 'normal')

normal_file_paths = [os.path.join(normal_path, f) for f in os.listdir(normal_path) if os.path.isfile(os.path.join(normal_path, f))]

# -----------------
dicts={}
for i in normal_file_paths:
	normalFile=open(i).read()
	textName=i.split('\\')[-1].split('_').index('interns')
	if (textName==0):
		key=base64.b64decode(normalFile).decode()
	elif (textName==3):
		key=base64.b32decode(normalFile).decode()
	else:
		key=base64.b16decode(normalFile).decode()
	dicts[key]=i.split('\\')[-1]

# print(base64.b64decode("ZWFzeV90b29fYXJlX3Rhc2tz").decode()) # .decode() de la final e pentru afisare fara tipul obiectului

dicts=json.dumps([dicts], sort_keys = True,indent=4)

with open(os.path.join(pwd_path+"/encoded", 'out.json') , 'w') as json_file:
    json_file.write(str(dicts))



