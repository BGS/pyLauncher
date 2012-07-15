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

import subprocess


info = {"name" : "pyLShell",
        "author" : "Blaga Florentin Gabriel <https://github.com/BGS/pyLauncher>",
        "version": "1.0",
        "category": "pylSearchExtensions",
        "class" : "execCmdCommand"}

class execCmdCommand():

    def parseQuery(self, query):

        if query:
            query = query.split()
            args = query[1:]
        
            if query[0] == "cmd":
                subprocess.Popen("cmd /K %s" % " ".join(args)) 
            else:
                pass
        
