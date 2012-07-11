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


import sys
import os

from pyl_core.pyl_engine import *
from pyl_core.pyl_winreg import *
from pyl_core.pyl_model import *
from pyl_core.pyl_config_parser import Parser

from pyl_rc.pyl_rc import *

from pyl_ui.main_window_ui import Ui_MainWindow
from pyl_ui.options_ui import Ui_Options

from PyQt4 import QtCore
from PyQt4 import QtGui

from ctypes import c_bool, c_int, WINFUNCTYPE, windll
from ctypes.wintypes import UINT

class GlobalHotKey(QtGui.QApplication):
    def __init__(self, argv):
        super(GlobalHotKey, self).__init__(argv)

        '''
         Win32 API
         BOOL RegisterHotKey(      
         HWND hWnd,
         int id,
         UINT fsModifiers,
         UINT vk
         );
        '''   
        
        self.HOT_KEY_ID = 1
        self.WM_HOTKEY = 0x0312
        
        function_prototype = WINFUNCTYPE(c_bool, c_int, c_int, UINT, UINT)
        
        paramflags = (1, 'hWnd', 0), (1, 'id', 0), (1, 'fsModifiers', 0), (1, 'vk', 0)

        self.RegisterHotKey = function_prototype(('RegisterHotKey', windll.user32), paramflags)

    def register(self):
        self.mainWindow = Main()
        
        # 0x002 -> MOD_CONTROL | 0x20 -> SPACEBAR
        
        register = self.RegisterHotKey(c_int(self.mainWindow.winId()), self.HOT_KEY_ID, 0x0002, 0x20)
        
    def winEventFilter(self, msg):
        if msg.message == self.WM_HOTKEY:
            if self.mainWindow.isVisible():
                self.mainWindow.hide()
            else:
                self.mainWindow.lineEdit.clear()
                self.mainWindow.show()
                self.mainWindow.lineEditSetFocus()
            return True, 0
        

        return False, 0

    def getMainWindow(self):
        return self.mainWindow


class Main(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isInUse = False
        self.fileManagerMode = False
        self.model = QtGui.QFileSystemModel()
        self.setTrayIcon()
        self.createContextMenu()
        self._engine = EngineInit(os.path.join(os.path.dirname(sys.argv[0]), 'catalog'))
        self.cfg_parse()
        self.setShortcuts()
     

    def cfg_parse(self):

        parser = Parser()
        if os.path.exists(os.path.join(os.path.dirname(sys.argv[0]), 'settings.ini')):
            config = parser.get_config_values()
           
            if config['always_on_top'] == 'True':
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            else:
                self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       
            self.setWindowOpacity(0.8)
           
            if config['first_run'] == 'True':
                self.beginRebuildCatalog()
                addToRegistry(os.path.realpath(sys.argv[0]))
                parser.set_value(section='Settings', option='first_run', value='False')
            if config['first_run'] == 'False':
                if config['autosync'] == 'True':
                    self.beginRebuildCatalog()
            if config['autorun'] == 'True':
                addToRegistry(os.path.realpath(sys.argv[0]))
                             
        else:
            parser.generate_ini_file()
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
            self.setWindowOpacity(0.8)

        
    def setShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)


    def setTrayIcon(self):
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.activated.connect(self.onTrayIconActivated)
        self.trayIcon.setIcon(QtGui.QIcon(':/pyl/icons/pyl.ico'))
        
        self.trayMenu = QtGui.QMenu()
        self.showAction = QtGui.QAction("Show", self)
        self.showOptionsAction = QtGui.QAction("Options", self)
        self.resyncAction = QtGui.QAction("Resync Catalog", self)
        self.exitAction = QtGui.QAction("Exit", self)
        
        self.trayMenu.addAction(self.showAction)
        self.trayMenu.addAction(self.showOptionsAction)
        self.trayMenu.addAction(self.resyncAction)
        self.trayMenu.addAction(self.exitAction)

        self.showOptionsAction.triggered.connect(self.showOptions)
        self.showAction.triggered.connect(self.show)
        self.exitAction.triggered.connect(self._close)
        
        self.trayIcon.setContextMenu(self.trayMenu)
        
        self.trayIcon.show()

    def showOptions(self):
        self._OptUi = Ui_Options()
        self._OptUi.show()
    
    def onTrayIconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            if self.isVisible():
                self.hide()
            else:
                self.lineEdit.clear()
                self.show()
                self.lineEditSetFocus()
        
    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos()-self.offset)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moving = False
            
    def MenuGetFavAppData(self):
        self.fileManagerMode = False
        self.listView.setModel(self._engine.getFavAppData())

    def MenuGetAppData(self):
        self.fileManagerMode = False
        self.listView.setModel(self._engine.getMenuAppData())

    def MenuGetInternetAppData(self):
        self.fileManagerMode = False
        self.listView.setModel(self._engine.getInternetAppData())

    def MenuGetMediaAppData(self):
        self.fileManagerMode = False
        self.listView.setModel(self._engine.getMediaAppData())

    def MenuGetSystem_UtilitiesData(self):
        self.fileManagerMode = False
        self.listView.setModel(self._engine.getSystem_UtilitiesAppData())

    def MenuShowOptions(self):
        self._OptUi = Ui_Options()
        self._OptUi.show()

        
    def createContextMenu(self):
        _contMenu = QtGui.QMenu(self)
        self._contMenu = _contMenu
        _sub_Add = QtGui.QMenu("Add to", self)
        _sub_Rem = QtGui.QMenu("Remove from", self)
                
        _add_favAction = QtGui.QAction("Favorites", self)
        _add_appAction = QtGui.QAction("Applications", self)
        _add_graphAction = QtGui.QAction("Media", self)
        _add_sys_util_Action = QtGui.QAction("System Utilities", self)
        _add_internetAction = QtGui.QAction("Internet", self)
        
        _sub_Add.addAction(_add_favAction)
        _sub_Add.addAction(_add_appAction)
        _sub_Add.addAction(_add_graphAction)
        _sub_Add.addAction(_add_sys_util_Action)
        _sub_Add.addAction(_add_internetAction)
        
        _add_favAction.triggered.connect(self.execFavAddAction)
        _add_appAction.triggered.connect(self.execAppAddAction)
        _add_graphAction.triggered.connect(self.execGraphAddAction)
        _add_sys_util_Action.triggered.connect(self.execSysUtilAddAction)
        _add_internetAction.triggered.connect(self.execInternetAddAction)

 
        _rem_favAction = QtGui.QAction("Favorites", self)
        _rem_appAction = QtGui.QAction("Applications", self)
        _rem_graphAction = QtGui.QAction("Media", self)
        _rem_sys_util_Action = QtGui.QAction("System Utilities", self)
        _rem_internetAction = QtGui.QAction("Internet", self)
        
        _sub_Rem.addAction(_rem_favAction)
        _sub_Rem.addAction(_rem_appAction)
        _sub_Rem.addAction(_rem_graphAction)
        _sub_Rem.addAction(_rem_sys_util_Action)
        _sub_Rem.addAction(_rem_internetAction)

        _rem_favAction.triggered.connect(self.execFavRemAction)
        _rem_appAction.triggered.connect(self.execAppRemAction)
        _rem_graphAction.triggered.connect(self.execGraphRemAction)
        _rem_sys_util_Action.triggered.connect(self.execSysUtilRemAction)
        _rem_internetAction.triggered.connect(self.execInternetRemAction)

        self._contMenu.addMenu(_sub_Add)
        self._contMenu.addMenu(_sub_Rem)

        self._contMenu.addSeparator()
        
        _rebuild_catalog_action = QtGui.QAction("Rebuild Catalog", self)
        
        
        _exit_action = QtGui.QAction("Exit", self)
        _hide_window = QtGui.QAction("Hide", self)

        self._contMenu.addAction(_rebuild_catalog_action)
        self._contMenu.addAction(_hide_window)
        self._contMenu.addAction(_exit_action)

        _rebuild_catalog_action.triggered.connect(self.beginRebuildCatalog)
        _hide_window.triggered.connect(self.hide)
        _exit_action.triggered.connect(self._close)

    def closeEvent(self, event):
        self.trayIcon.hide()
        self.close()
        
    def _close(self):
        self.trayIcon.hide()
        self.close()

    def beginRebuildCatalog(self):
        self.dbsync = QtCore.QProcess(self)
        self.connect(self.dbsync, QtCore.SIGNAL("started()"), self.Started)
        self.connect(self.dbsync, QtCore.SIGNAL("finished(int)"), self.onFinished)
        self.dbsync.setWorkingDirectory(os.path.dirname(sys.argv[0]))
        self.isInUse = True
        self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation started please wait!", 10000) 
        self.dbsync.start(os.path.join(os.path.dirname(sys.argv[0]), 'dbsync.exe'))

    def Started(self):
        self.emit(QtCore.SIGNAL("Started"))
        
    def onFinished(self, exitCode):
        if exitCode == 0:
            self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation completed!", 10000)
            self._engine.syncMemDb()
            self.isInUse = False
        else:
            self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation failed!", 10000)   
            self.isInUse = False
        
    def listView(self, listView):
        self.listView = listView
        self.listView.setStyle(QtGui.QStyleFactory.create("plastique"))
        self.listView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.listView,QtCore.SIGNAL('customContextMenuRequested(QPoint)'),
                             self.on_context_menu)
        self.listView.doubleClicked.connect(self.appExec)
        self.listView.setModel(self._engine.getFavAppData())

    def appExec(self, index):
        if self.isInUse == True:
            self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation in progress please wait!", 10000)
            return ''
        else:
            if  self.fileManagerMode == True:
                path = str(self.model.filePath(index))
                path = path.replace("/", "\\")
                subprocess.Popen(r'explorer ' + path )
                self.lineEdit.clear()
                self.hide()
                self.trayIcon.showMessage("pyLauncher | Daemon", "Opening path: "+path+" please wait!", 10000)
                return ''
            
            else:
                status = self._engine.appExec(index)
                if status == False:
                    self.trayIcon.showMessage("pyLauncher | Daemon", "Application not found or invalid! Preparing to remove it from catalog.", 10000)
                    return ''
                self.lineEdit.clear()
                self.hide()
                self.trayIcon.showMessage("pyLauncher | Daemon", "Application will start in a moment! Please wait.", 10000)
        

    def execFavAddAction(self):
        self._engine.addApplication(self._current_index, 'fav')

    def execGraphAddAction(self):
        self._engine.addApplication(self._current_index, 'graph')

    def execSysUtilAddAction(self):
        self._engine.addApplication(self._current_index, 'sys_util')
        
    def execAppAddAction(self):
        self._engine.addApplication(self._current_index, 'app')

    def execInternetAddAction(self):
        self._engine.addApplication(self._current_index, 'internet')
            
    def execFavRemAction(self):
        self._engine.remApplication(self._current_index, 'fav')

    def execGraphRemAction(self):
        self._engine.remApplication(self._current_index, 'graph')

    def execSysUtilRemAction(self):
        self._engine.remApplication(self._current_index, 'sys_util')

    def execAppRemAction(self):
        self._engine.remApplication(self._current_index, 'app')

    def execInternetRemAction(self):
        self._engine.remApplication(self._current_index, 'internet')

    def on_context_menu(self, point):
        self._current_index = self.listView.indexAt(point).row()
        self._contMenu.exec_(self.listView.mapToGlobal(point))
   
       
    def lineEdit(self, lineEdit):
        self.lineEdit = lineEdit   
        self.lineEdit.textChanged[str].connect(self.textChanged)
        self.lineEdit = lineEdit
        self.lineEdit.setFocus()

    def lineEditSetFocus(self):
        self.lineEdit.setFocus()

    def textChanged(self):
        if self.isInUse == True:
            self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation in progress please wait!", 10000)      
            return ''
        else:
            query = ''
            query += self.lineEdit.text()
            if len(query) < 2:
                self.fileManagerMode = False
                self.listView.setModel(self._engine.getFavAppData())
            else:
                if os.path.exists(query):
                    self.fileManagerMode = True
                    self.listView.setModel(self.model)
                    self.listView.setRootIndex(self.model.setRootPath(query))
                
                else:
                    self.fileManagerMode = False
                    self.listView.setModel(self._engine.getAppData(query))


         
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
    disablePy2ExeLogging()
    app = GlobalHotKey(sys.argv)
    app.register()
    ui = Ui_MainWindow()
    MainWindow = app.getMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.lineEdit(ui.lineEdit)
    MainWindow.listView(ui.listView)
    MainWindow.setWindowIcon(QtGui.QIcon(':/pyl/icons/pyl.ico'))
    MainWindow.show()
    sys.exit(app.exec_())
