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
        self.isInUse = False
        self.setTrayIcon()
        self.createContextMenu()
        self._engine = EngineInit(os.path.join(os.path.dirname(sys.argv[0]), 'catalog.rldb'))
        self.config_checkup()
        self.windowOpts()
        self.setShortcuts()
     

    def config_checkup(self):
        parser = CfgParser()
        self.cfg_parser = parser.get_cfg_parser()
        if os.path.exists('config.cfg'):
            self.cfg_parser.read('config.cfg')
            db_first_sync_opt = self.cfg_parser.get('dbSynchronised', 'isSynchronised')
            auto_start_opt = self.cfg_parser.get('Autostart', 'isEnabled')
            auto_sync_opt = self.cfg_parser.get('dbSynchronised', 'autoSynchronisation')
            if db_first_sync_opt == 'False' or auto_start_opt == 'False':
                self.cfg_parser.set('dbSynchronised', 'isSynchronised', 'True')
                self.cfg_parser.set('Autostart', 'isEnabled', 'True')
                self.beginRebuildCatalog()
                addToRegistry(os.path.realpath(sys.argv[0]))       
                self.trayIcon.showMessage("pyLauncher | Daemon", "Catalog synchronisation in progress please wait! \nAutostart has been Enabled!\nPress Ctrl+Space to show or hide me and Ctrl+Q\nto turn me off :( !", 50000)         
            elif auto_sync_opt == 'True' and db_first_sync_opt != 'False':
                self.beginRebuildCatalog()
            elif auto_sync_opt == 'False':
                pass
            elif auto_start_opt == 'Disabled':
                pass
            elif auto_start_opt == 'True':
                pass
            elif dbopt == 'True':
                pass

            with open('config.cfg', 'wb') as configfile:
                self.cfg_parser.write(configfile)
                
        else:
            parser.generate_cfg_file()


    def setShortcuts(self):
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self, self.close)

    def windowOpts(self):
        always_on_top = self.cfg_parser.get('windowOptions', 'wndAlwaysOnTop')
        if always_on_top == 'True':
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
       
        self.setWindowOpacity(0.8)

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
            auto_start_opt = self.cfg_parser.get('Autostart', 'isEnabled')
            auto_sync_opt = self.cfg_parser.get('dbSynchronised', 'autoSynchronisation')
            always_on_top = self.cfg_parser.get('windowOptions', 'wndAlwaysOnTop')
            print always_on_top
        if auto_start_opt == 'True':
            self.startWithWindowsCheckbox.toggle()
        elif auto_sync_opt == 'True':
            self.autoUpdateCheckBox.toggle()
        elif always_on_top == 'True':
            self.checkBoxStayOnTop.toggle()   
            
        else:
            pass

        self.checkBoxStayOnTop.stateChanged.connect(self.stayOnTopCheckBox)
        self.startWithWindowsCheckbox.stateChanged.connect(self.autoStartCheckBox)
        self.autoUpdateCheckBox.stateChanged.connect(self._autoUpdateCheckBox)  
        
        QtCore.QMetaObject.connectSlotsByName(self)

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
                cfg_parser.set('windowOptions', 'wndAlwaysOnTop', 'True')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
        else:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.set('windowOptions', 'wndAlwaysOnTop', 'False')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
            
    def _autoUpdateCheckBox(self, state):
        if state == QtCore.Qt.Checked:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.set('dbSynchronised', 'autoSynchronisation', 'True')
                with open('config.cfg', 'wb') as configfile:
                    cfg_parser.write(configfile)
        else:
            parser = CfgParser()
            if os.path.exists('config.cfg'):
                cfg_parser = parser.get_cfg_parser()
                cfg_parser.set('dbSynchronised', 'autoSynchronisation', 'False')
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
