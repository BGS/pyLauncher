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

import ConfigParser, os, sys

class Parser():

    def generate_ini_file(self, _file=os.path.join(os.path.dirname(sys.argv[0]), 'settings.ini')):
        self._parser = ConfigParser.RawConfigParser()
        
        self._parser.add_section('Settings')
        self._parser.set('Settings', 'first_run', 'True')
        self._parser.set('Settings', 'autosync', 'True')
        self._parser.set('Settings', 'autorun', 'True')
        self._parser.set('Settings', 'always_on_top', 'True')

        with open(_file, 'wb') as cfgfile:
            self._parser.write(cfgfile)

    def get_config_values(self, parser=ConfigParser.RawConfigParser(), _file=os.path.join(os.path.dirname(sys.argv[0]), 'settings.ini')):
        parser.read(_file)
        return dict(parser.items('Settings'))
                         
    def set_value(self, section, option, value, parser=ConfigParser.RawConfigParser(), _file=os.path.join(os.path.dirname(sys.argv[0]), 'settings.ini')):
        parser.read(_file)
        parser.set(section, option, value)
        with open(_file, 'wb') as cfgfile:
            parser.write(cfgfile)


