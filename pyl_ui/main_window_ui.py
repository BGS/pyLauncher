'''
pyLauncher: Windows Application Launcher
Copyright (C) Blaga Florentin Gabriel

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

from pyl_core.pyl_config_parser import Parser

PAUSE_LENGTH = 200

class EditableQMenu(QtGui.QMenuBar):
    '''
    A menu which allows users to edit the text fields.
    Double click on them to see this in action.
    '''
    def __init__(self, parent=None):
        QtGui.QMenuBar.__init__(self, parent)
        
        self.setMouseTracking(True)
        
    def mousePressEvent(self, event):
        '''
        slow down the click so that double clicks can be caught.
        '''

        def pass_on():
            QtGui.QMenuBar.mousePressEvent(self, event)
        action = self.actionAt(event.pos())
        if not action:
            return
        
        QtCore.QTimer.singleShot(PAUSE_LENGTH, pass_on)
        action.trigger()
        
        
        
    def mouseDoubleClickEvent(self, event):
        parser = Parser()
        action = self.actionAt(event.pos())
        if not action:
            return
        
        if action.text() == "Options":
            return
        text, result = QtGui.QInputDialog.getText(self, "edit menu",
            "enter new name for this menu item", text=action.text())
        if result:
            menu_item_uid = action.objectName()

            if  menu_item_uid == 'item1':
                parser.set_value(section='Menu', option='menu_item_1', value=text)
            elif menu_item_uid == 'item2':
                parser.set_value(section='Menu', option='menu_item_2', value=text)
            elif menu_item_uid == 'item3':
                parser.set_value(section='Menu', option='menu_item_3', value=text)
            elif menu_item_uid == 'item4':
                parser.set_value(section='Menu', option='menu_item_4', value=text)
            elif menu_item_uid == 'item5':
                parser.set_value(section='Menu', option='menu_item_5', value=text)
            action.setText(text)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self._MainWindow = MainWindow
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(471, 274)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet(_fromUtf8("border-radius: 5px;\n"
"color: lightGrey;\n"
"background-color: rgb(0, 0, 0)"))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.qLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.qLabel.setFont(font)
        self.qLabel.setStyleSheet(_fromUtf8("font: bold 11pt \"Segoe UI\";\n"
"color: lightGrey"))
        self.qLabel.setTextFormat(QtCore.Qt.AutoText)
        self.qLabel.setScaledContents(False)
        self.qLabel.setObjectName(_fromUtf8("qLabel"))
        self.verticalLayout.addWidget(self.qLabel)
        self.listView = QtGui.QListView(self.centralWidget)
        self.listView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.listView.setAutoFillBackground(True)
        self.listView.setStyleSheet(_fromUtf8("font:  8pt \"Segoe UI\";\n"
"background-color: rgb(0, 0, 0);\n"
"alternate-background-color: rgba(0,0,0,0%);\n"
"color: lightGrey;\n"
"border-style: solid;\n"
"border-width: 0px;\n"
"border: 1px solid gray;\n"
"\n"
""))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout.addWidget(self.listView)
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setStyleSheet(_fromUtf8("font:  8pt \"Segoe UI\";\n"
"border-width: 1px;\n"
"background-color:rgb(0, 0, 0);\n"
"border: 1px solid gray;\n"
"color: lightGrey;\n"
""))

        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = EditableQMenu(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuApplications = QtGui.QMenu(self.menuBar)
        self.menuApplications.setObjectName(_fromUtf8("menuApplications"))  
        self.menuInternet = QtGui.QMenu(self.menuBar)
        self.menuInternet.setObjectName(_fromUtf8("menuInternet"))
        self.menuMedia = QtGui.QMenu(self.menuBar)
        self.menuMedia.setObjectName(_fromUtf8("menuMedia"))
        self.menuFavorites = QtGui.QMenu(self.menuBar)
        self.menuFavorites.setObjectName(_fromUtf8("menuFavorites"))
        self.menuOptions = QtGui.QMenu(self.menuBar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuSystem_Utilities = QtGui.QMenu(self.menuBar)
        self.menuSystem_Utilities.setObjectName(_fromUtf8("menuSystem_Utilities"))
        self.menuBar.setStyleSheet(_fromUtf8("""*\n                                
{
background-color:  rgb(0, 0, 0);\n
}
QMenuBar::item
{
background-color:   rgb(0, 0, 0);\n
}
color: lightGrey;\n
    
"""))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.statusBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.retranslateUi(MainWindow)
        self.createMenuActions()
        self.connectMenuActions()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def createMenuActions(self):
        parser = Parser()
        menu_names = parser.get_menu_names()
        self.menuAppAction = QtGui.QAction(menu_names['menu_item_1'], self.menuBar)
        self.menuAppAction.setObjectName('item1')
        self.menuInternetAction = QtGui.QAction(menu_names['menu_item_2'], self.menuBar)
        self.menuInternetAction.setObjectName('item2')
        self.menuMediaAction = QtGui.QAction(menu_names['menu_item_3'], self.menuBar)
        self.menuMediaAction.setObjectName('item3')
        self.menuFavoritesAction = QtGui.QAction(menu_names['menu_item_4'], self.menuBar)
        self.menuFavoritesAction.setObjectName('item4')
        self.menuSystem_UtilitiesAction = QtGui.QAction(menu_names['menu_item_5'], self.menuBar)
        self.menuSystem_UtilitiesAction.setObjectName('item5')
        self.menuOptionsAction = QtGui.QAction("Options", self.menuBar)

        self.menuBar.addAction(self.menuAppAction)
        self.menuBar.addAction(self.menuInternetAction)
        self.menuBar.addAction(self.menuMediaAction)
        self.menuBar.addAction(self.menuFavoritesAction)
        self.menuBar.addAction(self.menuSystem_UtilitiesAction)
        self.menuBar.addAction(self.menuOptionsAction)

    def connectMenuActions(self):
        
        self.menuAppAction.triggered.connect(self._MainWindow.MenuGetAppData)
        self.menuInternetAction.triggered.connect(self._MainWindow.MenuGetInternetAppData)
        self.menuMediaAction.triggered.connect(self._MainWindow.MenuGetMediaAppData)
        self.menuFavoritesAction.triggered.connect(self._MainWindow.MenuGetFavAppData)
        self.menuSystem_UtilitiesAction.triggered.connect(self._MainWindow.MenuGetSystem_UtilitiesData)
        self.menuOptionsAction.triggered.connect(self._MainWindow.MenuShowOptions)



    def getMainWindow(self):
        return self._MainWindow
    
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.qLabel.setText(QtGui.QApplication.translate("MainWindow", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBar.showMessage(QtGui.QApplication.translate("MainWindow", "v0.1A"))

