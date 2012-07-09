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

from pyl_core.pyl_config_parser import *
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

        self.startWithWindowsCheckbox = QtGui.QCheckBox("Start with Windows", self.groupBox)
        self.startWithWindowsCheckbox.setGeometry(QtCore.QRect(10, 70, 121, 18))
    
        self.checkBoxStayOnTop = QtGui.QCheckBox("Always on top", self.groupBox)
        self.checkBoxStayOnTop.setGeometry(QtCore.QRect(10, 110, 131, 18))
        
        parser = CfgParser()
        self.cfg_parser = parser.get_cfg_parser()
        if os.path.exists('config.cfg'):
            self.cfg_parser.read('config.cfg')
            auto_sync_opt = self.cfg_parser.get('dbSynchronised', 'autoSynchronisation')
            auto_start_opt = self.cfg_parser.get('Autostart', 'isEnabled')
            always_on_top = self.cfg_parser.get('windowOptions', 'wndAlwaysOnTop')

        if auto_start_opt == 'True':
            self.startWithWindowsCheckbox.toggle()
        if auto_sync_opt == 'True':
            self.autoUpdateCheckBox.toggle()
        if always_on_top == 'True':
            self.checkBoxStayOnTop.toggle()   
   

        self.checkBoxStayOnTop.stateChanged.connect(self.stayOnTopCheckBox)
        self.startWithWindowsCheckbox.stateChanged.connect(self.autoStartCheckBox)
        self.autoUpdateCheckBox.stateChanged.connect(self._autoUpdateCheckBox)  
        
        QtCore.QMetaObject.connectSlotsByName(self)

    def _autoUpdateCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('dbSynchronised', 'autoSynchronisation', 'True')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
        else:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('dbSynchronised', 'autoSynchronisation', 'False')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)


    def autoStartCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            addToRegistry(os.path.realpath(sys.argv[0]))
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('Autostart', 'isEnabled', 'True')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
        else:
            removeFromRegistry()
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('Autostart', 'isEnabled', 'Disabled')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
            
    def stayOnTopCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('windowOptions', 'wndAlwaysOnTop', 'True')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
        else:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.read('config.cfg')
                cfg_parser.set('windowOptions', 'wndAlwaysOnTop', 'False')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
            
