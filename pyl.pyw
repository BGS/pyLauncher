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


import sys
import subprocess
import os

from pyl_core.pyl_engine import * 
from pyl_core.pyl_model import *
from pyl_core.pyl_winreg import *
from pyl_core.pyl_config_parser import *

from pyl_rc.pyl_rc import *

from pyl_ui.main_window_ui import Ui_MainWindow

from PyQt4 import QtCore
from PyQt4 import QtGui

from ctypes import c_bool, c_int, WINFUNCTYPE, windll
from ctypes.wintypes import UINT

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


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
        if not register:
            QtGui.QMessageBox.critical(None, 'pyLauncher Hotkeys', "Can't Register Hotkey Control + Space, make sure all instances of pyLauncher are closed.")

    def winEventFilter(self, msg):
        if msg.message == self.WM_HOTKEY:
            if self.mainWindow.isVisible():
                self.mainWindow.hide()
            else:
                self.mainWindow.lineEdit.clear()
                self.mainWindow.lineEditSetFocus()
                self.mainWindow.show()
            return True, 0
        

        return False, 0

    def getMainWindow(self):
        return self.mainWindow


class Main(QtGui.QMainWindow):
    def __init__(self):
        super(QtGui.QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.createContextMenu()
        self._engine = EngineInit(os.path.join(os.path.dirname(sys.argv[0]), 'catalog.rldb'))
        self.windowOpts()
        self.setTrayIcon()
        self.setShortcuts()
        self.config_checkup()

    def config_checkup(self):
        parser = CfgParser()
        if os.path.exists('config.cfg'):
            cfg_parser = parser.get_cfg_parser()
            cfg_parser.read('config.cfg')
            dbopt = cfg_parser.get('dbSynchronised', 'isSynchronised')
            auto_start_opt = cfg_parser.get('Autostart', 'isEnabled')
            if dbopt == 'False' or auto_start_opt == 'False':
                cfg_parser.set('dbSynchronised', 'isSynchronised', 'True')
                cfg_parser.set('Autostart', 'isEnabled', 'True')
                self.beginRebuildCatalog()
                addToRegistry(os.path.realpath(sys.argv[0]))       
                self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation in progress please wait! \nAutostart has been Enabled!\nPress Ctrl+Space to show or hide me and Ctrl+Q\nto turn me off :( !", 50000)         
                
            elif auto_start_opt == 'Denied':
                pass
            elif auto_start_opt == 'True':
                pass
            elif dbopt == 'True':
                pass

            with open('config.cfg', 'wb') as configfile:
                cfg_parser.write(configfile)
                
        else:
            parser.generate_cfg_file()


    def setShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

    def windowOpts(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.8)

    def setTrayIcon(self):
        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.activated.connect(self.onTrayIconActivated)
        self.trayIcon.setIcon(QtGui.QIcon(':/pyl/icons/pyl.ico'))
        
        self.trayMenu = QtGui.QMenu()
        self.showAction = QtGui.QAction("Show", self)
        self.refreshAction = QtGui.QAction("Refresh Catalog", self)
        self.resyncAction = QtGui.QAction("Resync Catalog", self)
        self.exitAction = QtGui.QAction("Exit", self)
        
        self.trayMenu.addAction(self.showAction)
        self.trayMenu.addAction(self.refreshAction)
        self.trayMenu.addAction(self.resyncAction)
        self.trayMenu.addAction(self.exitAction)

        self.showAction.triggered.connect(self.show)
        self.exitAction.triggered.connect(self._close)
        
        self.trayIcon.setContextMenu(self.trayMenu)
        
        self.trayIcon.show()
    
    def onTrayIconActivated(self, reason):
        if reason == QtGui.QSystemTrayIcon.DoubleClick:
            self.show()
        
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
        self.listView.setModel(self._engine.getFavAppData())

    def MenuGetAppData(self):
        self.listView.setModel(self._engine.getMenuAppData())

    def MenuGetInternetAppData(self):
        self.listView.setModel(self._engine.getInternetAppData())

    def MenuGetGraphicsAppData(self):
        self.listView.setModel(self._engine.getGraphicsAppData())

    def MenuGetSystem_UtilitiesData(self):
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
        _add_graphAction = QtGui.QAction("Graphics", self)
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
        _rem_graphAction = QtGui.QAction("Graphics", self)
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
        
        _refresh_catalog_action = QtGui.QAction("Refresh Catalog", self)
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
            status = self._engine.appExec(index)
            if status == False:
                self.trayIcon.showMessage("pyLauncher | Daemon", "Application not found or invalid! Preparing to remove it from catalog.", 10000)
                return ''
            self.listView.setModel(self._engine.getFavAppData())
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
            name = ''
            name += str(self.lineEdit.text())
            if len(name) < 2:
                self.listView.setModel(self._engine.getFavAppData())
            else:
                self.listView.setModel(self._engine.getAppData(name))

class Ui_Options(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Ui_Options, self).__init__(parent)
        self.windowOpts()
        
        self.resyncCatalogButton = QtGui.QCommandLinkButton("Resync Catalog", self)
        self.resyncCatalogButton.setGeometry(QtCore.QRect(20, 10, 121, 41))
        self.resyncCatalogButton.setObjectName(_fromUtf8("resyncCatalogButton"))
        self.startWithWindowsButton = QtGui.QCommandLinkButton("Enable Autostart", self)
        self.startWithWindowsButton.setGeometry(QtCore.QRect(20, 50, 161, 41))
        self.startWithWindowsButton.setObjectName(_fromUtf8("startWithWindowsButton"))
        self.disableStartWithWindowsButton = QtGui.QCommandLinkButton("Disable Autostart", self)
        self.disableStartWithWindowsButton.setGeometry(QtCore.QRect(20, 100, 161, 41))
        self.disableStartWithWindowsButton.setObjectName(_fromUtf8("disableStartWithWindowsButton"))       
        self.ExitButton = QtGui.QCommandLinkButton("Exit", self)
        self.ExitButton.setGeometry(QtCore.QRect(330, 0, 71, 41))
        self.ExitButton.setObjectName(_fromUtf8("ExitButton"))

        self.pyLauncherLabel = QtGui.QLabel("pyLauncher", self)
        self.pyLauncherLabel.setGeometry(QtCore.QRect(10, 195, 121, 21))
        
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        
        self.pyLauncherLabel.setFont(font)
        self.pyLauncherLabel.setTextFormat(QtCore.Qt.AutoText)
        self.pyLauncherLabel.setObjectName(_fromUtf8("pyLauncherLabel"))
   
        self.connect(self.ExitButton, QtCore.SIGNAL('clicked()'), self.close)
        self.connect(self.resyncCatalogButton, QtCore.SIGNAL('clicked()'), self.beginRebuildCatalog)
        self.connect(self.startWithWindowsButton, QtCore.SIGNAL('clicked()'), self.enableStartWithWindows)
        self.connect(self.disableStartWithWindowsButton, QtCore.SIGNAL('clicked()'), self.disableStartWithWindows)

    def windowOpts(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.8)
        self.resize(394, 229)
        self.setWindowTitle("pyLauncher | Options")
        self.setStyleSheet(_fromUtf8("color:gray;\n"
"background-color: rgb(0, 0, 0)"))   
        
    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos()-self.offset)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moving = True; self.offset = event.pos()

    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.moving = False


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
       
         
    def enableStartWithWindows(self):
        addToRegistry(os.path.realpath(sys.argv[0]))
        
    def disableStartWithWindows(self):
        removeFromRegistry()
        parser = CfgParser()
        if os.path.exists('config.cfg'):
            cfg_parser = parser.get_cfg_parser()
            cfg_parser.read('config.cfg')
            cfg_parser.set('Autostart', 'isEnabled', 'Denied')
            with open('config.cfg', 'wb') as configfile:
                cfg_parser.write(configfile)

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
