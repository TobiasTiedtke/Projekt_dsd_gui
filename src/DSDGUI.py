from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
import qtmodern.styles
import qtmodern.windows
import SaveButton as SaveB

import warnings


class DropList(QtWidgets.QListWidget):
    def __init__(self, parent, Ui):
        super(DropList, self).__init__(parent)
        self.Ui = Ui
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

    def dragEnterEvent(self, f):
        super(DropList, self).dragEnterEvent(f)
        print (f)
        self.DraggedItem = f.mimeData().text()

    def dropEvent(self, e):
        super(DropList, self).dropEvent(e)
        s = e.mimeData()
        t = s.text()
        print(self.DraggedItem)
        if str(e.mimeData().text()).startswith("$"):
            warnings.warn("Test")
#            for line in str(ActionList):
#                if line == str(e.text):


# Loading UI
class Ui(QtWidgets.QDialog):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DSDGUI.ui', self)
        self.DraggedItem = ""
        self.DSDGroup = self.findChild(QtWidgets.QGroupBox, 'groupBox_3')
        self.DSDList = DropList(self.DSDGroup, Ui)
        self.DSDList.setMinimumWidth(581)
        self.DSDList.setMinimumHeight(1024)
        self.ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
        self.DecisionGroup = self.findChild(QtWidgets.QGroupBox, 'groupBox')
        self.DecisionList = DropList(self.DecisionGroup, Ui)
        self.DecisionList.setMinimumWidth(581)
        self.DecisionList.setMinimumHeight(512)
        self.ReadButton = self.findChild(QtWidgets.QPushButton, 'ReadButton')
        self.ReadButton.clicked.connect(self.SingleBrowse)
        self.SaveButton = self.findChild(QtWidgets.QPushButton, 'SaveButton')
        self.SaveButton.clicked.connect(self.SaveButtonClick)
        self.DeleteAllButton = self.findChild(QtWidgets.QPushButton, 'DeleteAllButton')
        self.DeleteAllButton.clicked.connect(self.DeleteAll)
        self.SingleDeleteButton = self.findChild(QtWidgets.QPushButton, 'SingleDeleteButton')
        self.SingleDeleteButton.clicked.connect(self.SingleDelete)
        self.EditButton = self.findChild(QtWidgets.QPushButton, 'EditButton')
        self.EditButton.clicked.connect(self.EditButtonClick)
        self.SortButton = self.findChild(QtWidgets.QPushButton, 'SortButton')
        self.SortButton.clicked.connect(self.SortButtonClick)
        self.EditButton.setEnabled(False)
        self.SingleDeleteButton.setEnabled(False)
        self.SortButton.setEnabled(False)
        self.SaveButton.setEnabled(False)
        self.DeleteAllButton.setEnabled(False)
        self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint |
                            QtCore.Qt.WindowMaximizeButtonHint |
                            QtCore.Qt.CustomizeWindowHint |
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint |
                            QtCore.Qt.WindowStaysOnTopHint
                            )
        self.show()

    def SortButtonClick(self):
        DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
        ActionList = self.findChild(QtWidgets.QListWidget, 'ActionList')
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        for item in range(DSDList.count()):
            for item1 in range(DecisionList.count()):
                if DSDList.item(item).text() == DecisionList.item(item1).text():
                    DSDList.item(item).setText("    " + str(DSDList.item(item).text()))
            for item1 in range(ActionList.count()):
                if DSDList.item(item).text() == ActionList.item(item1).text():
                    DSDList.item(item).setText("        YES/NO --> @" + str(DSDList.item(item).text()))
                    
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

    def SingleBrowse(self):
        # browsing for a folder and changing it to a string
        filePath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                              QtWidgets.QFileDialog.ShowDirsOnly)
        filePath = str(filePath)
        # Adding variables for the various lists
        ActionFilePath = filePath + "/actions/"
        DecisionFilePath = filePath + "/decisions/"
        self.ActionList.setDragEnabled(True)
        self.DecisionList.setDragEnabled(True)
        self.SingleDeleteButton.setEnabled(True)
        self.DeleteAllButton.setEnabled(True)
        self.SaveButton.setEnabled(True)
        self.EditButton.setEnabled(True)
        self.SortButton.setEnabled(True)
        self.DSDList.clear()
        self.DecisionList.clear()
        self.ActionList.clear()
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
                        self.ActionList.addItem(item)
                        item.setText("        YES/NO --> @" + str(line))
                        self.ActionList.addItem(item)
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
                                self.DecisionList.addItem(item)
                                item.setText("    " + lineItem)
                                self.DecisionList.addItem(item)
                                if "]" in line:
                                    returners = 0
                    elif line.startswith("class"):
                        line = line.split(" ")[1]
                        line = line.split("(")[0]
                        item = QtWidgets.QListWidgetItem()
                        item.setText("$" + str(line))
                        self.DecisionList.addItem(item)
        dsd_files = [f for f in os.listdir(filePath) if f.endswith('.dsd')]
        if len(dsd_files) != 1:
            warnings.warn("There has to be exactly one dsd-file")
        DSDFile = open(filePath + "/" + dsd_files[0], "r")
        for line in DSDFile:
            item = QtWidgets.QListWidgetItem()
            self.DSDList.addItem(item)
            if line != "__init__.py":
                line = str(line.split("\n")[0])
                item.setText(line)
                self.DSDList.addItem(item)
                item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)

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
        # Saves the DSD-text to a new file
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        FileName = "StandardName"
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Filename:')
        if ok:
            FileName = str(text)
        Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                          QtWidgets.QFileDialog.ShowDirsOnly)
        # writes a file with a specific name and the structure needed for action-elements.
        completeName = os.path.join(Path, FileName + ".dsd")
        f = open(completeName, 'w')
        for i in range(DSDList.count()):
            string = DSDList.item(i).text()
            f.write(string + "\n")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    qtmodern.styles.dark(app)
    window = Ui()
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    sys.exit(app.exec_())
