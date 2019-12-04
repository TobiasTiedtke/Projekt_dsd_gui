from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
import warnings


# Loading UI
class Ui(QtWidgets.QDialog):
    resized = QtCore.pyqtSignal()
    def __init__(self):


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
                    DSDList.item(item).setText("        YES/NO --> " + str(DSDList.item(item).text()))
        
#eventFilter is used to check if a special event occurs and should then do something with that event
#    def eventFilter(self, object, event):
#        if (object is self.DSDList):
#        if (event.type() == QtCore.QEvent.Drop):
#	        print("WORK! GODDAMIT!")
 #       if (event.type() == QtCore.QEvent.MouseButtonDblClick):
  #        	#for i in range(DSDList.count()):
   #          #   DSDList.closePersistentEditor(DSDList.item(i))
    #        sel_items = DSDList.selectedItems()
     #       for item in sel_items:
      #          DSDList.openPersistentEditor(item)
       # return False # lets the event continue to the edit
#        return False

#TODO: Maybe??
    def eventFilter(self, object, event):
        DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
        if event.type() == QtCore.QEvent.MouseButtonPress and object is self.DSDList:
            warnings.warn("Gedidded!")
            return True

        return False

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
            EditButton = self.findChild(QtWidgets.QPushButton, 'EditButton')
            EditButton.clicked.connect(self.EditButtonClick)
            EditButton.setEnabled(False)
            SortButton = self.findChild(QtWidgets.QPushButton, 'SortButton')
            SortButton.clicked.connect(self.SortButtonClick)
            SortButton.setEnabled(False)
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
                line = str(line.split("\n")[0])
                item.setText(line)
                DSDList.addItem(item)
                if line != "__init__.py":
                    line = str(line)
                    item.setText(line)
                    DSDList.addItem(item)
    def SingleDelete(self):
            DSDList = self.findChild(QtWidgets.QListWidget, 'DSDList')
            listItems = self.DSDList.selectedItems()
            if not listItems: return
            for item in listItems:
                self.DSDList.takeItem(self.DSDList.row(item))


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
    window = Ui()
    sys.exit(app.exec_())
