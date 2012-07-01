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

import ConfigParser

class CfgParser():
    def __init__(self):
        self._config = ConfigParser.RawConfigParser()

    def generate_cfg_file(self):
        self._config.add_section('dbSynchronised')
        self._config.set('dbSynchronised', 'isSynchronised', 'False')
        self._config.add_section('Autostart')
        self._config.set('Autostart', 'isEnabled', 'False')

        with open('config.cfg', 'wb') as configfile:
            self._config.write(configfile)

    
    def get_cfg_parser(self):
        return self._config
