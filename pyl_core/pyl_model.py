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

#! /usr/bin/env python

# -*- coding: utf-8 -*-

import win32ui
import win32gui

from PyQt4 import QtCore
from PyQt4 import QtGui

from win32com.shell import *
from pythoncom import *    

class ItemDelegatorModel(QtCore.QAbstractListModel):
    def __init__(self, path_list = [], app_name_list = [], parent = None):
        super(QtCore.QAbstractListModel, self).__init__()
        self._path_list = path_list
        self._app_name_list = app_name_list
        self._hIcon = []
        for path in self._path_list:
            large, small = win32gui.ExtractIconEx(path, 0)
            try:
                win32gui.DestroyIcon(small[0])
            except IndexError:
                pass
            self._hIcon.append(QtGui.QPixmap.fromWinHBITMAP(self.bitmapFromHIcon(large[0]), 2))

    def bitmapFromHIcon(self, hIcon):
        hdc = win32ui.CreateDCFromHandle(win32gui.GetDC(0))
        hbmp = win32ui.CreateBitmap()
        hbmp.CreateCompatibleBitmap(hdc, 32, 32)
        hdc = hdc.CreateCompatibleDC()
        hdc.SelectObject(hbmp)
        hdc.DrawIcon((0, 0), hIcon)
        hdc.DeleteDC()
        return hbmp.GetHandle()

    def rowCount(self, parent):
        return len(self._path_list)


    def data(self, index, role):

        if role == QtCore.Qt.DisplayRole:
            return str(self._app_name_list[index.row()])

        if role == QtCore.Qt.ToolTipRole:
            return "Run: %s " % str(self._app_name_list[index.row()])
        
        if role == QtCore.Qt.DecorationRole:
            return self._hIcon[index.row()]
      
        
def setModelData(path_list = [], name_list = []):
    return ItemDelegatorModel(path_list, name_list)

