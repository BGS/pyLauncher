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

from _winreg import *

def addToRegistry(path):
    key = OpenKey(HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)
    SetValueEx(key,'pyLauncher',0,REG_SZ, path) 
    CloseKey(key)

def removeFromRegistry():
    key = OpenKey(HKEY_CURRENT_USER,'Software\Microsoft\Windows\CurrentVersion\Run', 0, KEY_ALL_ACCESS)
    DeleteValue(key, 'pyLauncher')
    CloseKey(key)

    
