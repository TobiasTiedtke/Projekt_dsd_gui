from os import listdir
from os.path import isfile, join

mypath = "/informatik3/bitbots_behavior-master/bitbots_body_behavior/src/bitbots_body_behavior/actions"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for f in onlyfiles:
	f = str(f)[:-3]
	print f
#print onlyfiles

