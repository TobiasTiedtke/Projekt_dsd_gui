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
	SaveButton.clicked.connect(SaveB.SaveButton)
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())





