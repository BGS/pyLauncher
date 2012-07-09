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


#! /usr/bin/env python

# -*- coding: utf-8 -*-

import apsw
import sqlite3
import sys
import subprocess
import os

from pyl_model import setModelData


import ctypes
import ctypes.wintypes

class EngineInit():

    def __init__(self, dbname):
        self._memcon = apsw.Connection(":memory:")
        self._dbname = dbname
        self._path_list = []
        self._name_list = []

        self._con = apsw.Connection(self._dbname)
        self._cursor = self._con.cursor()

        with self._memcon.backup("main", self._con, "main") as backup:
            while not backup.done:
                backup.step(100)

    def syncMemDb(self):
        with self._memcon.backup("main", self._con, "main") as backup:
            backup.step()
   
    def getAppData(self, app_name):
        self._path_list = []
        self._name_list = []

        for row in self._memcon.cursor().execute("SELECT name,path FROM app_data where name MATCH '*%s*'" % app_name):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)

    def getFavAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM favorites"):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)

    def getMenuAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM applications"):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)

    def getInternetAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM internet"):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)

    def getMediaAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM media"):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)
    
    def getSystem_UtilitiesAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM sysutils"):
            self._path_list.append(row[1])
            self._name_list.append(row[0])

        return setModelData(self._path_list, self._name_list)
    
    def addApplication(self, index, table):
        try:
            if table == 'fav':
                self._cursor.execute('INSERT OR REPLACE INTO favorites VALUES (?,?)', (self._name_list[index], self._path_list[index]))
            elif table == 'app':
                self._cursor.execute('INSERT OR REPLACE INTO applications VALUES (?,?)', (self._name_list[index], self._path_list[index]))
            elif table == 'graph':
                self._cursor.execute('INSERT OR REPLACE INTO media VALUES (?,?)', (self._name_list[index], self._path_list[index]))
            elif table == 'sys_util':
                self._cursor.execute('INSERT OR REPLACE INTO sysutils VALUES (?,?)', (self._name_list[index], self._path_list[index]))
            elif table == 'internet':
                self._cursor.execute('INSERT OR REPLACE INTO internet VALUES (?,?)', (self._name_list[index], self._path_list[index]))
        except IndexError:
            pass

        #resync db
        with self._memcon.backup("main", self._con, "main") as backup:
            backup.step()
          
    def remApplication(self, index, table):
        try:
            if table == 'fav':
                self._cursor.execute('DELETE FROM favorites WHERE path="%s"' % self._path_list[index].strip())
            elif table == 'app':
                self._cursor.execute('DELETE FROM applications WHERE path="%s"' % self._path_list[index].strip())
            elif table == 'graph':
                self._cursor.execute('DELETE FROM media WHERE path="%s"' % self._path_list[index].strip())
            elif table == 'sys_util':
                self._cursor.execute('DELETE FROM sysutils WHERE path="%s"' % self._path_list[index].strip())
            elif table == 'internet':
                self._cursor.execute('DELETE FROM internet WHERE path="%s"' % self._path_list[index].strip())
        except IndexError:
            pass
        
        #resync db
        with self._memcon.backup("main", self._con, "main") as backup:
            backup.step()

    def appExec(self, index):
        try:
            subprocess.Popen(self._path_list[index.row()], cwd=os.path.dirname(self._path_list[index.row()]))
        except WindowsError:
            self._cursor.execute('DELETE FROM app_data WHERE path="%s"' % self._path_list[index.row()].strip())

            #resync db
            with self._memcon.backup("main", self._con, "main") as backup:
                backup.step()
                return False
