from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys

#Loading UI
class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('TestUI.ui', self)
        TestButton = self.findChild(QtWidgets.QPushButton, 'pushButton')
        TestButton.clicked.connect(self.SingleBrowse)
        self.show()
   
    def SingleBrowse(self):
#browsing for a folder and changing it to a string
		filePath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/", QtWidgets.QFileDialog.ShowDirsOnly)
		filePath = str(filePath)
		ActionFilePath = filePath + "/actions/"
		DecisionFilePath = filePath + "/decisions/"
		DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
		ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
#Extracting the files from the selected path and adding it to the ListWidget
		onlyfiles = [f for f in os.listdir(ActionFilePath) if os.path.isfile(os.path.join(ActionFilePath, f))]
		for f in onlyfiles:
			item = QtWidgets.QListWidgetItem()
			ActionList.addItem(item)
	#		f = str(f).split(".")[:-1]
			if f != "__init__.py":
				f = str(f)
		        	item.setText(f)
			       	ActionList.addItem(item)
		onlyfiles = [f for f in os.listdir(DecisionFilePath) if os.path.isfile(os.path.join(DecisionFilePath, f))]
		for f in onlyfiles:
			item = QtWidgets.QListWidgetItem()
			DecisionList.addItem(item)
	#		f = str(f).split(".")[:-1]
			if f != "__init__.py":
				f = str(f)
		        	item.setText(f)
			       	DecisionList.addItem(item)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
