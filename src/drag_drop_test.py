from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QListWidgetItem, QListWidget, QAbstractItemView, QApplication, QMainWindow, QGroupBox, QVBoxLayout
import sys


drag_item = None
drag_row = None
class DragAndDropList(QListWidget):
    itemMoved = pyqtSignal(int, int, QListWidgetItem)  # Old index, new index, item
    def __init__(self, parent=None, **args):
        super(DragAndDropList, self).__init__(parent, **args)

        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.drag_item = None
        self.drag_row = None


    def dropEvent(self, event):
        super(DragAndDropList, self).dropEvent(event)
        #self.itemMoved.emit(self.drag_row, self.row(self.drag_item),
        #                    self.drag_item)
        print(drag_row, self.row(drag_item),
                            drag_item.text())
        self.drag_item = None


    def startDrag(self, supportedActions):
        global drag_item, drag_row
        drag_item = self.currentItem()
        drag_row = self.row(self.drag_item)
        super(DragAndDropList, self).startDrag(supportedActions)


if __name__ == '__main__':
    app = QApplication(sys.argv)
#    qtmodern.styles.dark(app)
    window = QMainWindow()
    b = QVBoxLayout()
    #window.setLayout(b)
    lefty = DragAndDropList(parent=window)
    righty = DragAndDropList(parent=window)
    righty.move(200,0)
    for i in range(5):
        l =QListWidgetItem()
        l.setText(str(i))
        lefty.addItem(l)
    lefty.resize(100,200)
    lefty.setAcceptDrops(True)
    lefty.setDragEnabled(True)
    righty.resize(100,200)
    righty.setAcceptDrops(True)
    righty.setDragEnabled(True)
    window.resize(800,600)
    window.show()

#    mw = qtmodern.windows.ModernWindow(window)
#    mw.show()
    sys.exit(app.exec_())