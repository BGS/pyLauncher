
# -*- coding: utf-8 -*-

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




import os


info = {"name" : "pyLWeb",
        "author" : "Blaga Florentin Gabriel <https://github.com/BGS/pyLauncher>",
        "category": "pylSearchExtensions", 
        "version": "1.0",
        "class" : "execWebSearch"}

class execWebSearch():

    def parseQuery(self, query):
        query = query.split()
        args = query[1:]

        if query:
            if query[0] == "google":
                os.startfile("http://www.google.com/search?source=pyLauncher&q=%s" % " ".join(args))
            elif query[0] == "wikipedia":
                os.startfile("http://en.wikipedia.org/wiki/Special:Search?search=%s&fulltext=Search" % " ".join(args))
            elif query[0] == "youtube":
                os.startfile("http://www.youtube.com/results?search_query=%s" % " ".join(args))
            else:
                pass
                    
               


        
