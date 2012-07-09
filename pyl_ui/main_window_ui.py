'''

pyLauncher: Windows Application Launcher
Copyright (C) Blaga Florentin Gabriel

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

'''

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon May 07 17:41:02 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost! 

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setStyleSheet(_fromUtf8("""
        *
        {
            background-color:  rgb(0, 0, 0);\n
        }
        QMenuBar::item
        {
            background-color:   rgb(0, 0, 0);\n
        }
        color: lightGrey;\n
        """
        ))
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

        self.menuAppAction = QtGui.QAction("Applications", self.menuBar)
        self.menuInternetAction = QtGui.QAction("Internet", self.menuBar)
        self.menuMediaAction = QtGui.QAction("Media", self.menuBar)
        self.menuFavoritesAction = QtGui.QAction("Favorites", self.menuBar)
        self.menuSystem_UtilitiesAction = QtGui.QAction("System Utilities", self.menuBar)
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
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.qLabel.setText(QtGui.QApplication.translate("MainWindow", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.statusBar.showMessage(QtGui.QApplication.translate("MainWindow", "v0.1"))
