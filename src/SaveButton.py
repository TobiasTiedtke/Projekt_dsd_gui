import os

def SaveButton(self):
	#TODO: Change FileName and Path to actual input-windows
	FileName = "Testfile"
	Path = "/informatik2/students/home/6kornell/Schreibtisch/Projekt_dsd_gui/src"
	#writes a file with a specific name and the structure needed for action-elements. 
	completeName = os.path.join(Path, FileName + ".py") 
	f = open(completeName, 'w')
	f.write("This has to be done in the future")

