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


from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')


import pywintypes
import pythoncom
import win32api
try:
    import py2exe.mf as modulefinder
    import win32com
    for p in win32com.__path__[1:]:
        modulefinder.AddPackagePath("win32com", p)
    for extra in ["win32com.shell"]: 
        __import__(extra)
        m = sys.modules[extra]
        for p in m.__path__[1:]:
            modulefinder.AddPackagePath(extra, p)
except ImportError:
    pass

excludes = ["pywin", "pywin.debugger"]
setup(
    name='pyLauncher',
    version='0.1',
    author='Blaga Florentin Gabriel',
    options = {'py2exe': {'bundle_files': 1},
               'py2exe': {'optimize':2},
               'py2exe': {'excludes': excludes},
               "py2exe":{"dll_excludes":[ "mswsock.dll", "powrprof.dll", "MSWSOCK.DLL", "POWRPROF.DLL" ]},
               "py2exe":{"packages":["gzip"], 
                         "includes":["sip", "csv", "webbrowser"]}},
    
                         
    data_files = [
            ('imageformats', [
              r'C:\Python27x86\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll',
              r'pyl.ico']),
             
             ('plugins', ['plugins/pyLShell.py',
                          'plugins/pyLWeb.py']),
             
             ('', ['settings.ini'])
             ],

    windows = [{
        'script': "pyl.pyw",
        "icon_resources":[(0, "pyl.ico")],
        "dest_base":"pyl"
        }],
 

    zipfile = None,
)
