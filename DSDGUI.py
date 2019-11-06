from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys

#Loading UI
class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DSDGUI.ui', self)
        DecisionFolderButton = self.findChild(QtWidgets.QPushButton, 'DecisionFolderButton')
        DecisionFolderButton.clicked.connect(self.SingleBrowse)
        ActionFolderButton = self.findChild(QtWidgets.QPushButton, 'ActionFolderButton')
        ActionFolderButton.clicked.connect(self.SingleBrowse)
        self.show()
    def SingleBrowse(self):
#Open directory
        filePath = QtWidgets.QFileDialog.getOpenFileNames(self, 'File Browser', "-/Desktop/",'*.txt.')
        print('filePath', filePath, '\n')
        fileHandle = open( filePath, 'r')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())





