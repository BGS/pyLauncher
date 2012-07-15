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


class PluginManager:

    search_extensions = {}
    extensions_info = {}
    
    def __init__(self, plugin_path):
        
        plugin_path = os.path.abspath(plugin_path)

        if not os.path.isdir(plugin_path):
            return

        sys.path.append(plugin_path)

        plugin_candidates = [p for p in os.listdir(plugin_path) if not p.endswith(".pyc")]

        for plugin in plugin_candidates:
            self.__initialize_plugin(plugin)

    def __initialize_plugin(self, plugin):

        if plugin.endswith(".py"):
            name = plugin[:-3]   
        else:
            name = plugin
                 
        try:
            __import__(name, globals(), locals(), [], -1)
        except ImportError:
            pass
        
        plugin = sys.modules[name]

        if hasattr(plugin, plugin.info["class"]):
            self.search_extensions[plugin.info["name"]] = plugin
            self.extensions_info[plugin.info["name"]] = plugin.info["name"], plugin.info["author"], plugin.info["version"]
            
    def getPluginsHandle(self, *args, **kwargs):
        plugin_list = []
        for extension in self.search_extensions.keys():
            plugin = self.search_extensions[extension]
            plugin_list.append(getattr(plugin, plugin.info["class"])(*args, **kwargs))
        return plugin_list

    def getPluginInformation(self):
        return self.extensions_info
        
