from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
import SaveButton as SaveB

#Loading UI
class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DSDGUI.ui', self)
        DecisionFolderButton = self.findChild(QtWidgets.QPushButton, 'DecisionFolderButton')
        DecisionFolderButton.clicked.connect(self.SingleBrowse)
        ActionFolderButton = self.findChild(QtWidgets.QPushButton, 'ActionFolderButton')
        ActionFolderButton.clicked.connect(self.SingleBrowse)
	SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
	SaveButton.clicked.connect(self.SaveButtonClick)
        self.show()

    #Function to enable drag of text
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    #Function to drop text
    def dropEvent(self, e):

        self.setText(e.mimeData().text())

    def SingleBrowse(self):
	#Open directory
        filePath = QtWidgets.QFileDialog.getOpenFileNames(self, 'File Browser', "-/Desktop/",'')
        print('filePath', filePath, '\n')
        fileHandle = open( filePath, 'r')

    def SaveButtonClick(self):
	#TODO: Change FileName and Path to actual input-windows
	FileName = "StandardName"
	text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Filename:')
	if ok:
            FileName = str(text)
	Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/", QtWidgets.QFileDialog.ShowDirsOnly)
	#writes a file with a specific name and the structure needed for action-elements. 
	completeName = os.path.join(Path, FileName + ".py") 
	f = open(completeName, 'w')
	f.write("This has to be done in the future")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())





