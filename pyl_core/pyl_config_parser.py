
# -*- coding: utf-8 -*-

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



import os, sys

from PyQt4 import QtCore

class Parser():

    def __init__(self):
        self.settings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, 'pyLauncher', application='settings.ini')
        self.settings.setFallbacksEnabled(False)

    def generate_ini_file(self):
        self.settings.setValue('first_run', 'True')
        self.settings.setValue('autosync', 'True')
        self.settings.setValue('autorun', 'True')
        self.settings.setValue('show_tips', 'True')
        self.settings.setValue('transparency', 0.8)
        self.settings.setValue('max_results', 5)
        self.settings.setValue('auto_update', 'True')
        self.settings.setValue('always_on_top', 'True')

        self.settings.setValue('menu_item_1', 'Applications')
        self.settings.setValue('menu_item_2', 'Internet')
        self.settings.setValue('menu_item_3', 'Media')
        self.settings.setValue('menu_item_4', 'Favorites')
        self.settings.setValue('menu_item_5', 'System Utilities')

    def read_value(self, section, fallback, _type):
        if _type == 'str':
            return self.settings.value(section, fallback).toString()
        elif _type == 'int':
            return self.settings.value(section, fallback).toInt()[0]
        elif _type == 'float':
            return self.settings.value(section, fallback).toDouble()[0]
                         
    def set_value(self, section, value):
        self.settings.setValue(section, value)
