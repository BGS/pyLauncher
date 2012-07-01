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




setup(
    options = {'py2exe': {'bundle_files': 1},
               "py2exe":{"dll_excludes":[ "mswsock.dll", "powrprof.dll" ]},
               "py2exe":{"packages":["gzip"], 
                         "includes":["sip", "csv"]}},    windows = [{'script': "dbsync.pyw"}],
    zipfile = None,
)
