from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os

def SaveButton(self):
	#TODO: Change FileName and Path to actual input-windows
	FileName = "Testfile"
	Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/", QtWidgets.QFileDialog.ShowDirsOnly)
	#writes a file with a specific name and the structure needed for action-elements. 
	completeName = os.path.join(Path, FileName + ".py") 
	f = open(completeName, 'w')
	f.write("This has to be done in the future")

