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
        TestList = self.findChild(QtWidgets.QListWidget, 'listWidget')
#Extracting the files from the selected path and adding it to the ListWidget
	onlyfiles = [f for f in os.listdir(filePath) if os.path.isfile(os.path.join(filePath, f))]
	for f in onlyfiles:
		item = QtWidgets.QListWidgetItem()
		TestList.addItem(item)
#		f = str(f).split(".")[:-1]
		f = str(f)
        	item.setText(f)
	       	TestList.addItem(item)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())
