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

import itertools
import sys
import os
import sqlite3
import platform
import pythoncom

from win32com.shell import shell
from ctypes import *
from ctypes.wintypes import *

from pyl_core.pyl_engine import EngineInit

class DbEngine():
        
    def connect(self, dbname):
        self.dbname = dbname
        try:
            self._con = sqlite3.connect(self.dbname)
            if self._con:
                self._cursor = self._con.cursor()

        except sqlite3.Error, e:
            if self._con:
                self._con.rollback()
                print "Error %s:" % e.args[0]
                
         
    def dbIntegrityCheck(self):
        app_data = 'CREATE VIRTUAL TABLE IF NOT EXISTS app_data USING fts4(name, path)'
        favorites = 'CREATE VIRTUAL TABLE IF NOT EXISTS favorites USING fts4(name, path)'
        sysutils = 'CREATE VIRTUAL TABLE IF NOT EXISTS sysutils USING fts4(name, path)'
        applications = 'CREATE VIRTUAL TABLE IF NOT EXISTS applications USING fts4(name, path)'
        graphics = 'CREATE VIRTUAL TABLE IF NOT EXISTS graphics USING fts4(name, path)'
        internet = 'CREATE VIRTUAL TABLE IF NOT EXISTS internet USING fts4(name, path)'


        self._cursor.execute(app_data)
        self._cursor.execute(favorites)
        self._cursor.execute(sysutils)
        self._cursor.execute(applications)
        self._cursor.execute(graphics)
        self._cursor.execute(internet)

        self._con.commit()

   

    def insert_data(self, queryset, args):
        self.queryset = queryset
        self.args = args
        try:
            self._cursor.execute(self.queryset, self.args)
            self._con.commit()
        except sqlite3.Error, e:
            print "Error %s" % e.args[0]


class DbSync():

    def getMsiRealPath(self, shortcut_path):
        '''
        UINT MsiGetShortcutTarget(
        LPCTSTR szShortcutTarget,
        LPTSTR szProductCode,
        LPTSTR szFeatureId,
        LPTSTR szComponentCode
        );
        '''

        MsiGetShortcutTarget = windll.msi.MsiGetShortcutTargetA
        MsiGetShortcutTarget.argtypes = [c_char_p, c_char_p, c_char_p, c_char_p]

        szShortcutTarget = c_char_p(shortcut_path)
        szProductCode = create_string_buffer(100)
        szFeatureId = create_string_buffer(100)
        szComponentCode = create_string_buffer(100)
        
        LPDWORD = PDWORD = POINTER(DWORD)
        
        MsiGetShortcutTarget(szShortcutTarget, szProductCode, szFeatureId,
                             szComponentCode)

        '''
        INSTALLSTATE MsiGetComponentPath(
        LPCTSTR szProduct,
        LPCTSTR szComponent,
        LPTSTR lpPathBuf,
        DWORD* pcchBuf);
        '''
        
        MsiGetComponentPath = windll.msi.MsiGetComponentPathA
        MsiGetComponentPath.argtypes = [c_char_p, c_char_p, c_char_p, LPDWORD]

        szProdCode = c_char_p(szProductCode.value)
        szCompCode = c_char_p(szComponentCode.value)
        pccBuf = pointer(c_ulong(100))
        szPath = create_string_buffer(100)
        MsiGetComponentPath(szProdCode, szCompCode, szPath, pccBuf)

        return  szPath.value
        

    def getAppPathData(self):
        dbe = DbEngine()
        dbe.connect(os.path.join(os.path.dirname(sys.argv[0]),'catalog.rldb'))
        dbe.dbIntegrityCheck()
        self._db = dbe

        windows_version = platform.uname()

        if windows_version[0] == 'Windows' and windows_version[2] == '7':
            paths = ["%s\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu" % (os.environ['SYSTEMDRIVE'], os.environ.get("USERNAME")),
                     "%s\ProgramData\Microsoft\Windows\Start Menu" % os.environ['SYSTEMDRIVE']]
            # sper sa fie asa =) fuckin windows xp
        elif windows_version[0] == "Windows" and windows_version[2] == "xp":
            paths = ["%s\Documents and Settings\Users\Start Menu\Programs" % os.environ['SYSTEMDRIVE'],
                     "%s\Documents and Settings\%s\Start Menu\Programs" % (os.environ['SYSTEMDRIVE'], os.environ.get("USERNAME")),
                     "%s\Documents and Settings\All Users\Start Menu\Programs" % os.environ['SYSTEMDRIVE']]
        self.inserted = set()       
        shortcut_path = []
        shortcut_name = []

        for path in paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith(".lnk"):
                        shortcut_path.append(os.path.join(root, file))
                        shortcut_name.append(file)
        for path, name in itertools.izip(shortcut_path, shortcut_name):
            self.pushData2Db(path, name)

    
    def pushData2Db(self, path, name):
        sh = pythoncom.CoCreateInstance(shell.CLSID_ShellLink, None,
                                           pythoncom.CLSCTX_INPROC_SERVER,
                                           shell.IID_IShellLink)
        persistent_interface = sh.QueryInterface(pythoncom.IID_IPersistFile)

        persistent_interface.Load(path)
        shortcut_path = path
        if sh.GetPath(shell.SLGP_RAWPATH)[0] and name not in self.inserted:
            path = sh.GetPath(shell.SLGP_RAWPATH)[0]
            if path.find("{") != -1 and path.startswith("{", 21):
                real_path = self.getMsiRealPath(shortcut_path)
                self._db.insert_data('INSERT OR REPLACE INTO app_data VALUES (?,?)', (name.split('.')[0], real_path))              
                
            else:
                if path.endswith(".exe"):
                    if path.startswith("%systemroot%") or path.startswith("%windir%"):
                        tmp_path = path.split('%')
                        path = os.environ['windir'] + tmp_path[2]
                        self._db.insert_data('INSERT OR REPLACE INTO app_data VALUES (?,?)', (name.split('.')[0], path))

                    elif  path.startswith("%ProgramFiles%"):
                        tmp_path = path.split('%')
                        path = os.environ["ProgramFiles"] + tmp_path[2]
                        self._db.insert_data('INSERT OR REPLACE INTO app_data VALUES (?,?)', (name.split('.')[0], path))

                    else:
                        self._db.insert_data('INSERT OR REPLACE INTO app_data VALUES (?,?)', (name.split('.')[0], path))                      
                        self.inserted.add(name)
        else:
            pass
        

def disablePy2ExeLogging():
    try:
        sys.stdout = open("nul", "w")
    except:
        pass
    try:
        sys.stderr = open("nul", "w")
    except:
        pass

if __name__ == '__main__':
    #disablePy2ExeLogging()
    DbSync().getAppPathData()
    
