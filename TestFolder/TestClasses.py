import os, sys
def SingleBrowse():
#browsing for a folder and changing it to a string
	filePath = "/informatik2/students/home/6kornell/Schreibtisch/bitbots_behavior-master/bitbots_head_behavior/src/bitbots_head_behavior/actions/look_at.py"        
	f = open(filePath, 'r')
    	for line in f: 
	    line = str(line)
	    if line.startswith("class"):
		line = line.split(" ")[1]
		line = line.split("(")[0]
		print(line)

SingleBrowse()
