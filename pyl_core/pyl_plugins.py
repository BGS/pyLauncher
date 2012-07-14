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

from pyl_plugin_categories.pyl_categories import pylSearchExtensions
from yapsy.PluginManager import PluginManager

import os
import sys

class PluginInit():
    def __init__(self):
        self.manager = PluginManager(categories_filter={ "pylSearchExtensions": pylSearchExtensions})
        
        self.manager.setPluginPlaces([os.path.join(os.path.dirname(sys.argv[0]), 'plugins')])
        self.manager.setPluginInfoExtension('ext')
        self.manager.locatePlugins()
        self.manager.loadPlugins()

    def getPluginsFromCategory(self, category):
        self.extensions = {}
        for plugin in self.manager.getPluginsOfCategory(category):
            self.extensions[plugin.plugin_object.name] = plugin.plugin_object

        return self.extensions

