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
from pyl_core.pyl_winreg import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import os
import sys

class Ui_Options(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_Options, self).__init__(parent)
        
        self.setWindowTitle("pyLauncher | Options")

        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
  
        self.resize(320, 195)
        
        self.groupBox = QtGui.QGroupBox("pyLauncher", self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 305, 165))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        self.autoUpdateCheckBox = QtGui.QCheckBox("Auto synchronise Catalog ", self.groupBox)
        self.autoUpdateCheckBox.setGeometry(QtCore.QRect(10, 30, 161, 18))

        self.startWithWindowsCheckBox = QtGui.QCheckBox("Start with Windows", self.groupBox)
        self.startWithWindowsCheckBox.setGeometry(QtCore.QRect(10, 70, 121, 18))
    
        self.checkBoxStayOnTop = QtGui.QCheckBox("Always on top", self.groupBox)
        self.checkBoxStayOnTop.setGeometry(QtCore.QRect(10, 110, 131, 18))


        parser = Parser()
        config = parser.get_config_values()
        

        if config['autosync'] == 'True':
            self.autoUpdateCheckBox.toggle()
        
        if config['autorun'] == 'True':
            self.startWithWindowsCheckBox.toggle()
           
        if config['always_on_top'] == 'True':
            self.checkBoxStayOnTop.toggle()
            
   
        self.checkBoxStayOnTop.stateChanged.connect(self.stayOnTopCheckBox)
        self.startWithWindowsCheckBox.stateChanged.connect(self.autoStartCheckBox)
        self.autoUpdateCheckBox.stateChanged.connect(self._autoUpdateCheckBox)  

        QtCore.QMetaObject.connectSlotsByName(self)

    def _autoUpdateCheckBox(self, state):
        parser = Parser()
        if state == QtCore.Qt.Checked:
            parser.set_value(section='Settings', option='autosync', value='True')
        else:
            parser.set_value(section='Settings', option='autosync', value='False')
       
            
    def autoStartCheckBox(self, state):
        parser = Parser()
        if state == QtCore.Qt.Checked:
            parser.set_value(section='Settings', option='autorun', value='True')
            addToRegistry(os.path.realpath(sys.argv[0]))
        else:
            parser.set_value(section='Settings', option='autorun', value='False')
            removeFromRegistry()
            
    def stayOnTopCheckBox(self, state):
        parser = Parser()
        if state == QtCore.Qt.Checked:
            parser.set_value(section='Settings', option='always_on_top', value='True')
        else:
            parser.set_value(section='Settings', option='always_on_top', value='False')
           
            
