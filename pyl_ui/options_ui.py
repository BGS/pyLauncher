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

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Options(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(394, 229)
        Dialog.setStyleSheet(_fromUtf8("color:gray;\n"
"background-color: rgb(0, 0, 0)"))
        self.resyncCatalogButton = QtGui.QCommandLinkButton(Dialog)
        self.resyncCatalogButton.setGeometry(QtCore.QRect(20, 10, 121, 41))
        self.resyncCatalogButton.setObjectName(_fromUtf8("resyncCatalogButton"))
        self.startWithWindowsButton = QtGui.QCommandLinkButton(Dialog)
        self.startWithWindowsButton.setGeometry(QtCore.QRect(20, 50, 161, 41))
        self.startWithWindowsButton.setObjectName(_fromUtf8("startWithWindowsButton"))
        self.pyLauncherLabel = QtGui.QLabel(Dialog)
        self.pyLauncherLabel.setGeometry(QtCore.QRect(10, 195, 121, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pyLauncherLabel.setFont(font)
        self.pyLauncherLabel.setTextFormat(QtCore.Qt.AutoText)
        self.pyLauncherLabel.setObjectName(_fromUtf8("pyLauncherLabel"))
        self.ExitButton = QtGui.QCommandLinkButton(Dialog)
        self.ExitButton.setGeometry(QtCore.QRect(330, 0, 71, 41))
        self.ExitButton.setObjectName(_fromUtf8("ExitButton"))
        self.commandLinkButton = QtGui.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(20, 100, 168, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "pyLauncher | Options", None, QtGui.QApplication.UnicodeUTF8))
        self.resyncCatalogButton.setText(QtGui.QApplication.translate("Dialog", "Resync Catalog", None, QtGui.QApplication.UnicodeUTF8))
        self.startWithWindowsButton.setText(QtGui.QApplication.translate("Dialog", "    pyLauncher\n"
"Enable Autostart", None, QtGui.QApplication.UnicodeUTF8))
        self.pyLauncherLabel.setText(QtGui.QApplication.translate("Dialog", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.ExitButton.setText(QtGui.QApplication.translate("Dialog", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.commandLinkButton.setText(QtGui.QApplication.translate("Dialog", "    pyLauncher\n"
" Disable Autostart", None, QtGui.QApplication.UnicodeUTF8))

