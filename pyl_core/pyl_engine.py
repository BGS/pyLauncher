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
        try:
            self._con = apsw.Connection(self._dbname)
            self._con.close()
        except Exception:
            pass
        
        if os.stat(self._dbname).st_size == 0:
            self._con = sqlite3.connect(self._dbname)
            self._cursor = self._con.cursor()
            self.dbIntegrityCheck()        
        else:
            self._con = apsw.Connection(self._dbname)
            self._cursor = self._con.cursor()

        with self._memcon.backup("main", self._con, "main") as backup:
            while not backup.done:
                backup.step(100)

    def syncMemDb(self):
        with self._memcon.backup("main", self._con, "main") as backup:
            backup.step()

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

    def getGraphicsAppData(self):
        self._path_list = []
        self._name_list = []
        for row in self._memcon.cursor().execute("SELECT name,path FROM graphics"):
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
                self._cursor.execute('INSERT OR REPLACE INTO graphics VALUES (?,?)', (self._name_list[index], self._path_list[index]))
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
                self._cursor.execute('DELETE FROM graphics WHERE path="%s"' % self._path_list[index].strip())
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
            Popen(self._path_list[index.row()], cwd=os.path.dirname(self._path_list[index.row()]))
        except WindowsError:
            self._cursor.execute('DELETE FROM app_data WHERE path="%s"' % self._path_list[index.row()].strip())

            #resync db
            with self._memcon.backup("main", self._con, "main") as backup:
                backup.step()
                return False
