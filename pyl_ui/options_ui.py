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

from pyl_core.pyl_config_parser import Parser
from pyl_core.pyl_winreg import addToRegistry, removeFromRegistry
from pyl_core.pyl_plugins import PluginInit

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import os
import sys

class Ui_Options(QtGui.QWidget):
    def __init__(self, main_window_instance=None, parent=None):
        super(Ui_Options, self).__init__(parent)

        self.plugins = PluginInit()
        
        self.setWindowTitle("pyLauncher | Options")
        self.main_window_instance=main_window_instance
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
  
        self.resize(419, 243)

        self.pylMainTab = QtGui.QTabWidget(self)
        self.pylMainTab.setGeometry(QtCore.QRect(0, 10, 421, 241))

        self.optionsMainTab = QtGui.QWidget()

        self.autoUpdatecheckBox = QtGui.QCheckBox(self.optionsMainTab)
        self.autoUpdatecheckBox.setGeometry(QtCore.QRect(10, 30, 161, 18))

        self.startWithWindowsCheckbox = QtGui.QCheckBox(self.optionsMainTab)
        self.startWithWindowsCheckbox.setGeometry(QtCore.QRect(10, 70, 121, 18))

        self.numberOfResultsDisplayed = QtGui.QSpinBox(self.optionsMainTab)
        self.numberOfResultsDisplayed.setGeometry(QtCore.QRect(350, 30, 46, 22))

        self.checkBoxStayOnTop = QtGui.QCheckBox(self.optionsMainTab)
        self.checkBoxStayOnTop.setGeometry(QtCore.QRect(10, 110, 131, 18))

        self.numResultDispalyed = QtGui.QLabel(self.optionsMainTab)
        self.numResultDispalyed.setGeometry(QtCore.QRect(190, 30, 141, 21))

        self.tipsCheckBox = QtGui.QCheckBox("Show tips on start up", self.optionsMainTab)
        self.tipsCheckBox.setGeometry(10, 140, 131, 18)

        self.autoUpdatepyLauncher = QtGui.QCheckBox(self.optionsMainTab)
        self.autoUpdatepyLauncher.setGeometry(QtCore.QRect(190, 70, 161, 18))

        self.transpLabel = QtGui.QLabel("Transparency:", self.optionsMainTab)
        self.transpLabel.setGeometry(QtCore.QRect(180, 111, 71, 20))

        self.transparencySpinBox = QtGui.QDoubleSpinBox(self.optionsMainTab)
        self.transparencySpinBox.setGeometry(QtCore.QRect(260, 110, 62, 22))
        self.transparencySpinBox.setMinimum(0.1)
        self.transparencySpinBox.setMaximum(1.0)
        self.transparencySpinBox.setDecimals(1)
        self.transparencySpinBox.setSingleStep(0.1)
        self.transparencySpinBox.setRange(0.1, 1.0)

        self.label_3 = QtGui.QLabel(self.optionsMainTab)
        self.label_3.setGeometry(QtCore.QRect(70, 150, 241, 61))

        font = QtGui.QFont()

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)

        self.label_3.setFont(font)

        self.pylMainTab.addTab(self.optionsMainTab, _fromUtf8("About pyLauncher"))

        self.pylPluginsTab = QtGui.QWidget()

        self.availPlugsBox = QtGui.QGroupBox(self.pylPluginsTab)
        self.availPlugsBox.setGeometry(QtCore.QRect(10, 20, 391, 181))

        self.tableView = QtGui.QTableView(self.availPlugsBox)
        self.tableView.setGeometry(QtCore.QRect(10, 20, 371, 151))

        self.pylMainTab.addTab(self.pylPluginsTab, _fromUtf8("About pyLauncher2"))
        
        self.pylAbout = QtGui.QWidget()

        self.label = QtGui.QLabel(self.pylAbout)
        self.label.setGeometry(QtCore.QRect(80, 0, 241, 61))

        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe Print"))
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        
        self.label.setFont(font)

        self.label_2 = QtGui.QLabel(self.pylAbout)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 391, 181))
        
        font = QtGui.QFont()

        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(7)
        self.label_2.setOpenExternalLinks(True)

        self.pylMainTab.addTab(self.pylAbout, _fromUtf8("About pyLauncher"))

        self.pylMainTab.setCurrentIndex(0)


        self.parser = Parser()
        config = self.parser.get_config_values()
        
        
        if config['auto_update'] == 'True':
            self.autoUpdatepyLauncher.toggle()
        
        if config['autosync'] == 'True':
            self.autoUpdatecheckBox.toggle()
        
        if config['autorun'] == 'True':
            self.startWithWindowsCheckbox.toggle()
           
        if config['always_on_top'] == 'True':
            self.checkBoxStayOnTop.toggle()

        if config['show_tips'] == 'True':
            self.tipsCheckBox.toggle()
            
        self.numberOfResultsDisplayed.setValue(int(config['max_results']))
        self.numberOfResultsDisplayed.setMinimum(1)
        self.transparencySpinBox.setValue(float(config['transparency']))
               
        self.retranslateUi()
        
        QtCore.QMetaObject.connectSlotsByName(self)
        self.connectSignals()

    def connectSignals(self):
        self.checkBoxStayOnTop.stateChanged.connect(self.stayOnTopCheckBox)
        self.startWithWindowsCheckbox.stateChanged.connect(self.autoStartCheckBox)
        self.autoUpdatecheckBox.stateChanged.connect(self._autoSyncCheckBox)
        self.numberOfResultsDisplayed.valueChanged.connect(self.updateNumberOfResults)
        self.autoUpdatepyLauncher.stateChanged.connect(self.autoUpdateStateChanged)
        self.transparencySpinBox.valueChanged.connect(self.updateTransparency)
        self.tipsCheckBox.stateChanged.connect(self.tipsCheckBoxState)
        
    def tipsCheckBoxState(self, state):
        if state == QtCore.Qt.Checked:
            self.parser.set_value(section='Settings', option='show_tips', value='True')
        else:
            self.parser.set_value(section='Settings', option='show_tips', value='False')
               
    def updateTransparency(self, value):
        self.parser.set_value(section='Settings', option='transparency', value=value)
        self.main_window_instance.setWindowOpacity(value)
        
    def autoUpdateStateChanged(self, state):
        if state == QtCore.Qt.Checked:
            self.parser.set_value(section='Settings', option='auto_update', value='True')
        else:
            self.parser.set_value(section='Settings', option='auto_update', value='False')
       
        
    def updateNumberOfResults(self):
        self.parser.set_value(section='Settings', option='max_results', value=self.numberOfResultsDisplayed.value())
        
    def _autoSyncCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            self.parser.set_value(section='Settings', option='autosync', value='True')
        else:
            self.parser.set_value(section='Settings', option='autosync', value='False')
       
            
    def autoStartCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            self.parser.set_value(section='Settings', option='autorun', value='True')
            addToRegistry(os.path.realpath(sys.argv[0]))
        else:
            self.parser.set_value(section='Settings', option='autorun', value='False')
            removeFromRegistry()
            
    def stayOnTopCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            self.parser.set_value(section='Settings', option='always_on_top', value='True')
        else:
            self.parser.set_value(section='Settings', option='always_on_top', value='False')


    def retranslateUi(self):
        self.autoUpdatecheckBox.setText(QtGui.QApplication.translate("Options", "Auto synchronise Catalog", None, QtGui.QApplication.UnicodeUTF8))
        self.startWithWindowsCheckbox.setText(QtGui.QApplication.translate("Options", "Start with Windows", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxStayOnTop.setText(QtGui.QApplication.translate("Options", "Stay always on top", None, QtGui.QApplication.UnicodeUTF8))
        self.numResultDispalyed.setText(QtGui.QApplication.translate("Options", "Number of results displayed:", None, QtGui.QApplication.UnicodeUTF8))
        self.autoUpdatepyLauncher.setText(QtGui.QApplication.translate("Options", "Auto Update on new version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Options", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.pylMainTab.setTabText(self.pylMainTab.indexOf(self.optionsMainTab), QtGui.QApplication.translate("Options", "pyLauncher Main", None, QtGui.QApplication.UnicodeUTF8))
        self.availPlugsBox.setTitle(QtGui.QApplication.translate("Options", "Available Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.pylMainTab.setTabText(self.pylMainTab.indexOf(self.pylPluginsTab), QtGui.QApplication.translate("Options", "pyLauncher Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Options", "pyLauncher", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Options", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">pyLauncher</span><span style=\" font-size:10pt;\"> is a free utility for </span><span style=\" font-size:10pt; font-weight:600;\">Microsoft Window</span><span style=\" font-size:10pt;\">s designed to help you forget about your Start Menu, the Icons on your Desktop, </span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">and even your File Manager.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">If you want to help improve pyLauncher or fill a bug report please visit: </span><a href=\"https://github.com/BGS/pyLauncher\"><span style=\" font-size:10pt; text-decoration: underline; color:#0000ff;\">pyLauncher Home Page</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pylMainTab.setTabText(self.pylMainTab.indexOf(self.pylAbout), QtGui.QApplication.translate("Options", "About pyLauncher", None, QtGui.QApplication.UnicodeUTF8))  
        
