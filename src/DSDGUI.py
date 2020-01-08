from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
import qtmodern.styles
import qtmodern.windows
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
            SingleDeleteButton = self.findChild(QtWidgets.QPushButton, 'SingleDeleteButton')
            SingleDeleteButton.clicked.connect(self.SingleDelete)
            SingleDeleteButton.setEnabled(False)
            DecisionEdit = self.findChild(QtWidgets.QPushButton, 'DecisionEdit')
            DecisionEdit.clicked.connect(self.DecisionPlus)
            ActionEdit = self.findChild(QtWidgets.QPushButton, 'ActionEdit')
            ActionEdit.clicked.connect(self.ActionEditClick)
            EditButton = self.findChild(QtWidgets.QPushButton, 'EditButton')
            EditButton.clicked.connect(self.EditButtonClick)
            EditButton.setEnabled(False)
            SortButton = self.findChild(QtWidgets.QPushButton, 'SortButton')
            SortButton.setEnabled(False)
            SaveButton.setEnabled(False)
            DeleteAllButton.setEnabled(False)

   #         self.setStyleSheet("background-image: url(C:/Users/Tobias/Pictures/Tree.png)")
            self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                QtCore.Qt.WindowMaximizeButtonHint |
                QtCore.Qt.CustomizeWindowHint |
                QtCore.Qt.WindowTitleHint |
                QtCore.Qt.WindowCloseButtonHint |
                QtCore.Qt.WindowStaysOnTopHint
            )
            self.show()
    def DecisionPlus(self):
        DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
        item2 = QtWidgets.QListWidgetItem()
        DecisionList.addItem(item2)
        DecisionList.openPersistentEditor(item2)

    def DeleteAll(self):
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        DSDList.clear()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Ui, self).resizeEvent(event)

    def DecisionEditClick(self):
            DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
            for i in range(DecisionList.count()):
               DecisionList.closePersistentEditor(DecisionList.item(i))
            sel_items = DecisionList.selectedItems()
            for item in sel_items:
               DecisionList.openPersistentEditor(item)

    def ActionEditClick(self):
            ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
            for i in range(ActionList.count()):
               ActionList.closePersistentEditor(ActionList.item(i))
            sel_items = ActionList.selectedItems()
            for item in sel_items:
               ActionList.openPersistentEditor(item)

    def EditButtonClick(self):
            DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
            for i in range(DSDList.count()):
               DSDList.closePersistentEditor(DSDList.item(i))
            sel_items = DSDList.selectedItems()
            for item in sel_items:
               DSDList.openPersistentEditor(item)
#	text, okPressed = QtWidgets.QInputDialog.getText(self, "Add to the list item","Your Change:", QtWidgets.QLineEdit.Normal, ""), QtWidgets.QInputDialog.setText(str(sel_items))
#        if okPressed and text != '':
#	    for item in sel_items:
#	        item.setText(item.text() + text)
      
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
        ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        DecisionList.setDragEnabled(True)
        DSDList.setAcceptDrops(True)
        ActionList.setDragEnabled(True)
        DeleteAllButton = self.findChild(QtWidgets.QPushButton, 'DeleteAllButton')
        SingleDelete = self.findChild(QtWidgets.QPushButton, 'SingleDeleteButton')
        SingleDelete.setEnabled(True)
        DeleteAllButton.setEnabled(True)
        SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        SaveButton.setEnabled(True)
        SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        SaveButton.clicked.connect(self.SaveButtonClick)
        EditButton = self.findChild(QtWidgets.QPushButton, 'EditButton')
        EditButton.setEnabled(True)
        SortButton = self.findChild(QtWidgets.QPushButton, 'SortButton')
        SortButton.setEnabled(True)




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
            returners = 0
            if f != "__init__.py":
                    f = open(DecisionFilePath + "/" + f, 'r')
                    for line in f:
                        if "def _register():" in line:
                                  returners = 1
                        elif returners == 1 and "def _register():" not in line:
                                if "[" in line:
                                    line = line.split("[")[1]
                                    lineItems = []
                                    lineItems.extend(line.split(","))
                                    for items in lineItems:
                                        if items.strip():
                                            lineItem = str(items.split(" ")[-1])
                                            lineItem = str(items.split("'")[1])
                                            item = QtWidgets.QListWidgetItem()
                                            DecisionList.addItem(item)
                                            item.setText(lineItem)
                                            DecisionList.addItem(item)
                                if "]" in line:
                                    returners = 0
                                elif line.startswith("class"):
                                     line = line.split(" ")[1]
                                     line = line.split("(")[0]
                                     item = QtWidgets.QListWidgetItem()
                                     item.setText(str(line))
                                     DecisionList.addItem(item)

        dsd_files = [f for f in os.listdir(filePath) if f.endswith('.dsd')]
        if len(dsd_files) != 1:
            warnings.warn("There has to be exactly one dsd-file")
        DSDFile = open (filePath + "/" + dsd_files[0], "r")
        for line in DSDFile:
                item = QtWidgets.QListWidgetItem()
                DSDList.addItem(item)
                if line != "__init__.py":
                    line = str(line)
                    item.setText(line)
                    DSDList.addItem(item)
    def SingleDelete(self):
            ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
            DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
            DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
            listItems = self.DSDList.selectedItems()
            listItems2 = self.ActionList.selectedItems()
            listItems3 = self.DecisionList.selectedItems()
            if listItems:
               for item in listItems:
                self.DSDList.takeItem(self.DSDList.row(item))
            if listItems2:
               for item in listItems2:
                self.ActionList.takeItem(self.ActionList.row(item))
            if listItems3:
             for item in listItems3:
                self.DecisionList.takeItem(self.DecisionList.row(item))
            DSDList.clearSelection()
            ActionList.clearSelection()
            DecisionList.clearSelection()


    def clearSelection(self):
        ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
        DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        DSDList.clearSelection()
        ActionList.clearSelection()
        DecisionList.clearSelection()

    def SaveButtonClick(self):
        # TODO: Change FileName and Path to actual input-windows
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        FileName = "StandardName"
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Filename:')
        if ok:
            FileName = str(text)
        Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                          QtWidgets.QFileDialog.ShowDirsOnly)
        # writes a file with a specific name and the structure needed for action-elements.
        completeName = os.path.join(Path, FileName + ".py")
        f = open(completeName, 'w')
        for i in range(DSDList.count()):
            string = DSDList.item(i).text()
            f.write(string)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    window = Ui()
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    sys.exit(app.exec_())
