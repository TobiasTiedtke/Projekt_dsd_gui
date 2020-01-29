from PyQt5 import QtWidgets, uic, QtCore, QtGui
import os, sys
#import qtmodern.styles
#import qtmodern.windows
import warnings

dragItem = None


class DragList(QtWidgets.QListWidget):
    def __init__(self, parent, Ui):
        super(DragList, self).__init__(parent)
        self.Ui = Ui
        self.setDragEnabled(True)

    def startDrag(self, supportedActions):
        global dragItem
        dragItem = self.currentItem()
#        if str(dragItem.text()).startswith("$"):
#            print("success")
        super(DragList, self).startDrag(supportedActions)

class DropList(QtWidgets.QListWidget):
    def __init__(self, parent, Ui):
        super(DropList, self).__init__(parent)
        self.Ui = Ui
        self.setAcceptDrops(True)
        self.setDragEnabled(True)

#ToDo: Mit DropEvent die Verarbeitung auf der rechten Seite anstoßen
    def dropEvent(self, e):
        item = QtWidgets.QListWidgetItem()
        item.setText(str(dragItem.text()))
        self.addItem(item)
        item.setFlags(item.flags() | QtCore.Qt.ItemIsEditable)
#        super(DropList, self).dropEvent(e)
#        QtCore.pyqtSignal()
#        if str(dragItem.text()).startswith("$"):
#            newText = str(dragItem.text()).split("$")[1]
#            item = QtWidgets.QListWidgetItem()
#            item.setText(newText)
#            self.addItem(item)
#        if str(dragItem.text()).startswith("        YES/NO --> @"):
#            newText = str(dragItem.text()).split("@")[1]
#            item = QtWidgets.QListWidgetItem()
#            item.setText(newText)
#            self.addItem(item)
#            self.row(item)

# Loading UI
class Ui(QtWidgets.QDialog):
    EditableActionList = []
    EditableDecisionList = []
    resized = QtCore.pyqtSignal()
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('DSDGUI.ui', self)
        self.DraggedItem = ""
        self.DSDGroup = self.findChild(QtWidgets.QGroupBox, 'groupBox_3')
        self.DSDList = DropList(self.DSDGroup, Ui)
        self.DSDList.setMinimumWidth(581)
        self.DSDList.setMinimumHeight(1024)
        self.ActionGroup = self.findChild(QtWidgets.QGroupBox, 'groupBox_2')
        self.ActionList = DragList(self.ActionGroup, Ui)
        self.ActionList.setMinimumWidth(581)
        self.ActionList.setMinimumHeight(480)
        self.DecisionGroup = self.findChild(QtWidgets.QGroupBox, 'groupBox')
        self.DecisionList = DragList(self.DecisionGroup, Ui)
        self.DecisionList.setMinimumWidth(581)
        self.DecisionList.setMinimumHeight(480)
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

        self.ActionEdit = self.findChild(QtWidgets.QPushButton, 'ActionEdit')
        self.ActionEdit.clicked.connect(self.ActionEditClick)

        self.DecisionEdit = self.findChild(QtWidgets.QPushButton, 'DecisionEdit')
        self.DecisionEdit.clicked.connect(self.DecisionEditClick)

        self.SortButton = self.findChild(QtWidgets.QPushButton, 'SortButton')
        self.DecisionList.setDragEnabled(True)
        self.DecisionList.setAcceptDrops(False)
        self.DSDList.setDragEnabled(False)
        self.DSDList.setAcceptDrops(True)
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

    def DecisionPlus(self):
        DecisionList = self.findChild(QtWidgets.QListWidget, 'DecisionList')
        item2 = QtWidgets.QListWidgetItem()
        DecisionList.addItem(item2)
        DecisionList.openPersistentEditor(item2)
        
    def DeleteAll(self):

        self.DSDList.clear()

    def resizeEvent(self, event):
        self.resized.emit()
        return super(Ui, self).resizeEvent(event)

    def DecisionEditClick(self):

            for i in range(self.DecisionList.count()):
               self.DecisionList.closePersistentEditor(self.DecisionList.item(i))
            sel_items = self.DecisionList.selectedItems()
            for item in sel_items:
               self.DecisionList.openPersistentEditor(item)

                
    def ActionEditClick(self):
      
            for i in range(self.ActionList.count()):
               self.ActionList.closePersistentEditor(self.ActionList.item(i))
            sel_items = self.ActionList.selectedItems()
            for item in sel_items:
               self.ActionList.openPersistentEditor(item)

                
    def EditButtonClick(self):
      
            for i in range(self.DSDList.count()):
               self.DSDList.closePersistentEditor(self.DSDList.item(i))
            sel_items = self.DSDList.selectedItems()
            for item in sel_items:
                self.DSDList.openPersistentEditor(item)

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
                        # itemYes = QtWidgets.QListWidgetItem()
                        # itemYes.setText("        YES --> @")
                        # self.DecisionList.addItem(itemYes)
                        # itemNo = QtWidgets.QListWidgetItem()
                        # itemNo.setText("        NO --> @")
                        # self.DecisionList.addItem(itemNo)
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

        for item in range (self.DecisionList.count()) :
            #print(self.DecisionList.item(item).text())
            self.EditableDecisionList.append(self.DecisionList.item(item).text())

        print(len(self.EditableDecisionList))
        for item in range(self.ActionList.count()):
            #print(self.ActionList.item(item).text())
            self.EditableActionList.append(self.ActionList.item(item).text())

        #print(len(self.EditableActionList))



    def SingleDelete(self):

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
            self.DSDList.clearSelection()
            self.ActionList.clearSelection()
            self.DecisionList.clearSelection()
            
    def clearSelection(self):

        self.DSDList.clearSelection()
        self.ActionList.clearSelection()
        self.DecisionList.clearSelection()

    def SaveButtonClick(self):
        # Saves the DSD-text to a new file
        FileName = "StandardName"
        text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter Filename:')
        if ok:
            FileName = str(text)
        Path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                          QtWidgets.QFileDialog.ShowDirsOnly)
        # writes a file with a specific name and the structure needed for action-elements.
        completeName = os.path.join(Path, FileName + ".dsd")
        n = self.EditableActionList.count()
        f = open(completeName, 'a')
        for i in range(self.DSDList.count()):
            string = self.DSDList.item(i).text()
            f.write(string + "\n" + n)
        f.close()


        for i in range(self.ActionList.count()):
            if not self.ActionList.item(i).text() in self.EditableActionList:
                path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select a folder:', "-/Desktop/",
                                                                  QtWidgets.QFileDialog.ShowDirsOnly)
                fileName = str(self.ActionList.item(i).text())
                y = str(self.ActionList.item(i).text())
                completeName = os.path.join(path, fileName + ".py")
                a = open(completeName, 'a')
                a.write("from dynamic_stack_decider.abstract_action_element import AbstractActionElement\n")
                a.write("\n")
                a.write("class " + str(y) + "(AbstractActionElement):\n")
                a.write("    def __init__(self, blackboard, dsd, parameters=None):\n")
                a.write("        super(" + y + ", self).__init__(blackboard, dsd, parameters)\n")
                a.write("\n")
                a.write("#TODO: write your own code here.\n")
                a.write("\n")
                a.write("    def perform(self, reevaluate=False):\n")
                a.write("\n")
                a.write("#TODO: write your own code here.\n")
                a.write("\n")
                a.close()
        f = open(completeName, 'w')
        for i in range(self.DSDList.count()):
            string = self.DSDList.item(i).text()
            f.write(string + "\n")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
#    qtmodern.styles.dark(app)
    window = Ui()
#    mw = qtmodern.windows.ModernWindow(window)
#    mw.show()
    sys.exit(app.exec_())
