import os
import itertools
import base64

pwd_path = os.path.dirname(os.path.realpath(__file__))
normal_path = os.path.join(pwd_path, 'normal')

easy_beg = []
easy_end = []
easy_mid = []

for perm in  list(itertools.permutations(['tasks', 'are', 'too', 'easy'])):
	if perm[0] == 'easy':
		easy_beg.append(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3])
	elif  perm[3] == 'easy':
		easy_end.append(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3])
	else:
		easy_mid.append(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3])


for perm in list(itertools.permutations(['interns','devops','are','cool'])):
	with open(os.path.join(normal_path, perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3]), 'w') as the_file:
		if perm[0] == 'interns':
			the_file.write(str(base64.b64encode(easy_beg[0].encode()).decode()))
			print(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3] , str(base64.b64encode(easy_beg[0].encode()).decode()) , easy_beg[0])
			easy_beg.pop(0)
		elif perm[3] == 'interns':
			the_file.write(str(base64.b32encode(easy_end[0].encode()).decode()))
			print(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3] , str(base64.b32encode(easy_end[0].encode()).decode()) , easy_end[0])
			easy_end.pop(0)
		else:			
			the_file.write(str(base64.b16encode(easy_mid[0].encode()).decode()))
			print(perm[0] + '_' + perm[1] + '_' + perm[2] + '_' + perm[3] , str(base64.b16encode(easy_mid[0].encode()).decode()) , easy_mid[0] )
			easy_mid.pop(0)
		
		
		