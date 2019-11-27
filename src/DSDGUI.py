from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
import SaveButton as SaveB
import warnings


# Loading UI
class Ui(QtWidgets.QDialog):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DSDGUI.ui', self)
        ReadButton = self.findChild(QtWidgets.QPushButton, 'ReadButton')
        ReadButton.clicked.connect(self.SingleBrowse)
        SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        SaveButton.clicked.connect(self.SaveButtonClick)
        DeleteAllButton = self.findChild(QtWidgets.QPushButton, 'DeleteAllButton')
        DeleteAllButton.clicked.connect(self.DeleteAll)
        SaveButton.setEnabled(False)
        DeleteAllButton.setEnabled(False)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
            QtCore.Qt.WindowMaximizeButtonHint |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint
        )
        self.show()

    def DeleteAll(self):
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        DSDList.clear()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Ui, self).resizeEvent(event)

    # Function to enable drag of text
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # Function to drop text
    def dropEvent(self, e):

        self.setText(e.mimeData().text())

    def SingleBrowse(self):
        # browsing for a folder and changing it to a string
        filePath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        filePath = str(filePath)
        # Adding variables for the various lists
        ActionFilePath = filePath + "/actions/"
        DecisionFilePath = filePath + "/decisions/"
        DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        DecisionList.setDragEnabled(True)
        DSDList.setAcceptDrops(True)
        ActionList.setDragEnabled(True)
        DeleteAllButton = self.findChild(QtWidgets.QPushButton, 'DeleteAllButton')
        DeleteAllButton.setEnabled(True)
        SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        SaveButton.setEnabled(True)




        # Extracting the classes in the files in the actions-Folder from the selected path and adding it to the ActionList
        onlyfiles = [f for f in os.listdir(ActionFilePath) if os.path.isfile(os.path.join(ActionFilePath, f))]
        for f in onlyfiles:
            if f != "__init__.py":
                f = open(ActionFilePath + "/" + f, 'r')
                for line in f:
                    line = str(line)
                    if line.startswith("class"):
                        line = line.split(" ")[1]
                        line = line.split("(")[0]
                        item = QtWidgets.QListWidgetItem()
                        ActionList.addItem(item)
                        item.setText(str(line))
                        ActionList.addItem(item)

        # Extracting the classes in the files in the decisions-Folder from the selected path and adding it to the DecisionList
        onlyfiles = [f for f in os.listdir(DecisionFilePath) if os.path.isfile(os.path.join(DecisionFilePath, f))]
        for f in onlyfiles:
            if f != "__init__.py":
                f = open(DecisionFilePath + "/" + f, 'r')
                for line in f:
                    line = str(line)
                    if line.startswith("class"):
                        line = line.split(" ")[1]
                        line = line.split("(")[0]
                        item = QtWidgets.QListWidgetItem()
                        DecisionList.addItem(item)
                        item.setText(str(line))
                        DecisionList.addItem(item)

        dsd_files = [f for f in os.listdir(filePath) if f.endswith('.dsd')]
        if len(dsd_files) != 1:
            warnings.warn("There has to be exactly one dsd-file")
        DSDFile = open(filePath + "/" + dsd_files[0], "r")
        for line in DSDFile:
            item = QtWidgets.QListWidgetItem()
            DSDList.addItem(item)
            if line != "__init__.py":
                line = str(line)
                item.setText(line)
                DSDList.addItem(item)

    def SaveButtonClick(self):
        # TODO: Change FileName and Path to actual input-windows
        FileName = "StandardName"
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Filename:')
        if ok:
            FileName = str(text)
        Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                          QtWidgets.QFileDialog.ShowDirsOnly)
        # writes a file with a specific name and the structure needed for action-elements.
        completeName = os.path.join(Path, FileName + ".py")
        f = open(completeName, 'w')
        f.write("This has to be done in the future")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    sys.exit(app.exec_())