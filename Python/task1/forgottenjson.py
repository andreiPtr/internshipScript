'''
 - Obiectiv -
Crearea unui json valid folosind lista si dictionarul dat

 - Instructiuni -
Atribuie rasele in ordinea aparitiei, ex  "terrier": {'name': 'Lola', 'age': [12]}
Varsta fiecarui caine va creste cu valoarea din variabila old_age, ex "terrier": {'name': 'Lola', 'age': [22]}
Output JSON va fi scris in fisierul out.json

Mentiuni: jsonvalidator.py este adaugat doar pentru validare (nu trebuie modificat)

'''

# ----------------- NO CHANGE REQUIRED

import os

pwd_path = os.path.dirname(os.path.realpath(__file__))

old_age = 10

dogs = {1: {'name': 'Bobita', 'age': [31]},
           2: {'name': 'Lola', 'age': [12]},
           3: {'name': 'Luna', 'age': [1]},
           4: {'name': 'Rex', 'age': [5]},
		   5: {'name': 'Dora', 'age': [4]},
		   6: {'name': 'Coco', 'age': [8]}}

dog_breeds = [ 'maidanez' , 'terrier' , 'bichon' , 'ciobanesc', 'lup' , 'metis']

# -----------------

print(dogs[2]['age'])



for dog_index in range(1,len(dogs)+1):
    dogs[dog_index]['age']=dogs[dog_index]['age'][0]+old_age
    dogs[dog_breeds[dog_index-1]]=dogs[dog_index]
    del dogs[dog_index]

dogs=str(dogs)
dogs=dogs.replace('\'','\"')
with open(os.path.join(pwd_path, 'out.json') , 'w') as json_file:
    json_file.write(str(dogs))

