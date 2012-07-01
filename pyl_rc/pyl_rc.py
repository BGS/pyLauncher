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

# -*- coding: utf-8 -*-

from PyQt4 import QtCore

qt_resource_data = "\
\x00\x00\x15\x36\
\x00\
\x00\x01\x00\x02\x00\x10\x10\x00\x00\x00\x00\x20\x00\x68\x04\x00\
\x00\x26\x00\x00\x00\x20\x20\x00\x00\x00\x00\x20\x00\xa8\x10\x00\
\x00\x8e\x04\x00\x00\x28\x00\x00\x00\x10\x00\x00\x00\x20\x00\x00\
\x00\x01\x00\x20\x00\x00\x00\x00\x00\x40\x04\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x69\x69\x69\
\xff\x6f\x6f\x6e\xff\x74\x74\x74\xff\x79\x79\x79\xff\x7e\x7e\x7d\
\xff\x82\x82\x82\xff\x86\x86\x86\xff\x89\x89\x89\xff\x8b\x8b\x8b\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x63\x63\x63\
\xff\x69\x68\x69\xff\x6e\x6e\x6e\xff\x74\x74\x74\xff\x79\x79\x79\
\xff\x7e\x7e\x7d\xff\x82\x82\x82\xff\x86\x86\x86\xff\x89\x89\x89\
\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x5c\x5c\x5c\
\xff\x62\x62\x62\xff\x68\x68\x68\xff\x6e\x6e\x6e\xff\x74\x73\x73\
\xff\x78\x78\x78\xff\x7d\x7d\x7d\xff\x82\x82\x82\xff\x86\x86\x86\
\xff\x89\x89\x89\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x56\x56\x56\
\xff\x5c\x5c\x5c\xff\x62\x62\x62\xff\x68\x68\x68\xff\x6e\x6e\x6e\
\xff\x73\x73\x73\xff\x79\x79\x78\xff\x7d\x7d\x7d\xff\x82\x82\x82\
\xff\x85\x86\x85\xff\x89\x89\x89\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\
\xff\x8b\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x4f\x4f\x4f\
\xff\x56\x56\x56\xff\x7b\x7a\x7a\xff\x8f\x8f\x8e\xff\x68\x68\x68\
\xff\x6e\x6e\x6e\xff\x82\x82\x82\xff\xa7\xa7\xa7\xff\x84\x83\x83\
\xff\x82\x81\x82\xff\x85\x85\x85\xff\x89\x89\x89\xff\x8b\x8b\x8b\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x49\x49\x49\
\xff\x4f\x4f\x4f\xff\xa9\xa9\xa9\xff\xd6\xd6\xd6\xff\x62\x62\x62\
\xff\x67\x67\x68\xff\x91\x91\x91\xff\xe6\xe6\xe6\xff\xd3\xd3\xd3\
\xff\x7d\x7d\x7d\xff\x81\x81\x81\xff\x85\x85\x85\xff\x89\x88\x89\
\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x43\x42\x43\
\xff\x49\x49\x49\xff\xa6\xa6\xa6\xff\xe7\xe7\xe7\xff\xcf\xcf\xce\
\xff\xa9\xaa\xaa\xff\x67\x67\x67\xff\x96\x96\x96\xff\xff\xff\xff\
\xff\x89\x89\x89\xff\x95\x95\x95\xff\xdf\xdf\xdf\xff\xe1\xe0\xe0\
\xff\xd7\xd7\xd7\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x3d\x3d\x3d\
\xff\x42\x42\x42\xff\xa3\xa3\xa3\xff\xec\xec\xec\xff\x8c\x8c\x8c\
\xff\xff\xff\xff\xff\x86\x86\x86\xff\xca\xca\xca\xff\xf8\xf8\xf8\
\xff\xb9\xb9\xb9\xff\x99\x99\x99\xff\xff\xff\xff\xff\xa0\xa0\xa0\
\xff\x9f\x9f\x9f\xff\x88\x88\x88\xff\x8b\x8b\x8b\xff\x36\x36\x36\
\xff\x3c\x3c\x3c\xff\x9f\xa0\x9f\xff\xe6\xe6\xe6\xff\x5c\x5c\x5c\
\xff\xf9\xf9\xf9\xff\x9b\x9b\x9b\xff\xfa\xfa\xfa\xff\xab\xab\xab\
\xff\xed\xed\xed\xff\x95\x95\x95\xff\xff\xff\xff\xff\x7c\x7c\x7c\
\xff\x81\x80\x80\xff\x85\x85\x85\xff\x88\x88\x88\xff\x31\x31\x31\
\xff\x36\x36\x37\xff\x90\x90\x91\xff\xd5\xd5\xd5\xff\xdc\xdc\xdc\
\xff\xcd\xcd\xcd\xff\x9f\x9f\x9f\xff\xdb\xdb\xdb\xff\x62\x63\x63\
\xff\xe7\xe7\xe7\xff\xaf\xaf\xaf\xff\xff\xff\xff\xff\x77\x77\x77\
\xff\x7c\x7c\x7c\xff\x80\x81\x80\xff\x84\x85\x84\xff\x2b\x2b\x2c\
\xff\x31\x31\x31\xff\x36\x36\x36\xff\x3c\x3c\x3c\xff\x42\x42\x42\
\xff\x48\x48\x48\xff\x4e\x4e\x4e\xff\x54\x54\x54\xff\x5a\x5a\x5a\
\xff\x60\x60\x60\xff\x8c\x8c\x8c\xff\xff\xff\xff\xff\x72\x72\x71\
\xff\x77\x77\x77\xff\x7c\x7b\x7b\xff\x80\x80\x80\xff\x26\x27\x27\
\xff\x2c\x2b\x2c\xff\x30\x31\x30\xff\x36\x36\x36\xff\x3c\x3b\x3b\
\xff\x41\x42\x41\xff\x48\x48\x48\xff\x4e\x4e\x4e\xff\x54\x54\x54\
\xff\x5a\x5a\x5a\xff\x69\x6a\x6a\xff\x8c\x8c\x8c\xff\x6c\x6b\x6c\
\xff\x71\x71\x71\xff\x77\x76\x77\xff\x7b\x7b\x7b\xff\x22\x22\x22\
\xff\x27\x26\x26\xff\x2b\x2b\x2b\xff\x30\x30\x30\xff\x36\x36\x35\
\xff\x3b\x3b\x3b\xff\x41\x41\x41\xff\x47\x47\x47\xff\x4d\x4d\x4d\
\xff\x53\x54\x54\xff\x5a\x5a\x5a\xff\x5f\x60\x60\xff\x66\x66\x65\
\xff\x6b\x6c\x6c\xff\x71\x71\x71\xff\x76\x77\x76\xff\x1e\x1e\x1e\
\xff\x22\x22\x22\xff\x26\x26\x26\xff\x2b\x2b\x2b\xff\x30\x30\x30\
\xff\x35\x36\x35\xff\x3b\x3b\x3b\xff\x41\x41\x41\xff\x47\x47\x47\
\xff\x4d\x4d\x4d\xff\x53\x53\x53\xff\x59\x59\x59\xff\x60\x5f\x5f\
\xff\x65\x65\x65\xff\x6b\x6b\x6b\xff\x71\x70\x71\xff\x1b\x1b\x1b\
\xff\x1e\x1e\x1e\xff\x22\x22\x22\xff\x26\x27\x26\xff\x2b\x2a\x2a\
\xff\x30\x30\x30\xff\x35\x35\x35\xff\x3b\x3a\x3b\xff\x40\x40\x40\
\xff\x46\x47\x47\xff\x4d\x4d\x4d\xff\x53\x53\x53\xff\x59\x59\x59\
\xff\x5f\x5f\x5f\xff\x65\x65\x66\xff\x6b\x6b\x6b\xff\x1a\x1a\x1a\
\xff\x1b\x1b\x1b\xff\x1e\x1e\x1e\xff\x22\x22\x22\xff\x26\x26\x26\
\xff\x2a\x2b\x2a\xff\x30\x30\x2f\xff\x35\x35\x34\xff\x3a\x3a\x3a\
\xff\x40\x40\x40\xff\x46\x46\x46\xff\x4c\x4c\x4c\xff\x53\x53\x52\
\xff\x59\x59\x59\xff\x5f\x5f\x5f\xff\x65\x65\x65\xff\x00\x00\xff\
\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\
\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\
\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\
\xff\x00\x00\xff\xff\x00\x00\xff\xff\x00\x00\xff\xff\x28\x00\x00\
\x00\x20\x00\x00\x00\x40\x00\x00\x00\x01\x00\x20\x00\x00\x00\x00\
\x00\x80\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x69\x69\x69\xff\x6c\x6d\x6c\xff\x6f\x6f\x6e\
\xff\x72\x72\x72\xff\x74\x74\x75\xff\x77\x77\x77\xff\x7a\x79\x7a\
\xff\x7c\x7c\x7c\xff\x7e\x7e\x7e\xff\x81\x81\x80\xff\x83\x83\x82\
\xff\x84\x85\x84\xff\x86\x86\x86\xff\x88\x88\x88\xff\x8a\x89\x89\
\xff\x8b\x8b\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x66\x66\x66\xff\x69\x69\x6a\xff\x6c\x6c\x6c\
\xff\x6f\x6f\x6f\xff\x71\x72\x72\xff\x75\x75\x74\xff\x77\x77\x76\
\xff\x7a\x79\x79\xff\x7c\x7c\x7b\xff\x7e\x7e\x7e\xff\x81\x81\x81\
\xff\x82\x82\x83\xff\x85\x84\x84\xff\x87\x86\x86\xff\x88\x88\x88\
\xff\x89\x8a\x8a\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x63\x63\x64\xff\x66\x66\x66\xff\x69\x69\x69\
\xff\x6c\x6b\x6c\xff\x6f\x6e\x6f\xff\x72\x72\x71\xff\x75\x74\x74\
\xff\x76\x77\x77\xff\x79\x79\x7a\xff\x7c\x7c\x7b\xff\x7e\x7e\x7e\
\xff\x80\x81\x80\xff\x82\x82\x82\xff\x84\x84\x85\xff\x87\x86\x86\
\xff\x88\x88\x88\xff\x8a\x8a\x8a\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x60\x60\x5f\xff\x63\x63\x63\xff\x66\x66\x66\
\xff\x69\x69\x69\xff\x6b\x6c\x6c\xff\x6e\x6f\x6e\xff\x72\x72\x72\
\xff\x74\x74\x74\xff\x77\x76\x77\xff\x79\x79\x79\xff\x7c\x7b\x7b\
\xff\x7e\x7e\x7e\xff\x80\x80\x80\xff\x82\x83\x83\xff\x84\x84\x84\
\xff\x87\x87\x86\xff\x88\x88\x88\xff\x89\x8a\x89\xff\x8b\x8b\x8b\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x5c\x5c\x5d\xff\x5f\x60\x5f\xff\x63\x63\x62\
\xff\x66\x66\x65\xff\x68\x68\x69\xff\x6c\x6c\x6c\xff\x6f\x6f\x6e\
\xff\x71\x71\x71\xff\x74\x74\x73\xff\x77\x76\x76\xff\x79\x79\x79\
\xff\x7b\x7b\x7b\xff\x7e\x7e\x7e\xff\x80\x80\x80\xff\x83\x82\x83\
\xff\x84\x85\x84\xff\x87\x86\x86\xff\x88\x88\x88\xff\x89\x89\x89\
\xff\x8b\x8a\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x59\x59\x59\xff\x5c\x5d\x5d\xff\x5f\x5f\x60\
\xff\x63\x63\x62\xff\x66\x65\x65\xff\x68\x69\x68\xff\x6b\x6b\x6c\
\xff\x6e\x6f\x6e\xff\x71\x71\x71\xff\x74\x74\x74\xff\x76\x76\x76\
\xff\x79\x79\x79\xff\x7b\x7b\x7b\xff\x7d\x7e\x7d\xff\x80\x80\x7f\
\xff\x83\x82\x82\xff\x84\x84\x84\xff\x86\x86\x86\xff\x88\x88\x88\
\xff\x89\x8a\x89\xff\x8a\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x56\x56\x57\xff\x5a\x5a\x59\xff\x5d\x5d\x5c\
\xff\x60\x60\x60\xff\x62\x63\x62\xff\x66\x65\x65\xff\x69\x68\x69\
\xff\x6c\x6b\x6b\xff\x6e\x6e\x6e\xff\x71\x71\x71\xff\x73\x74\x74\
\xff\x76\x76\x76\xff\x79\x79\x79\xff\x7c\x7c\x7b\xff\x7e\x7d\x7e\
\xff\x80\x80\x80\xff\x82\x82\x82\xff\x84\x84\x84\xff\x86\x86\x86\
\xff\x88\x88\x87\xff\x8a\x8a\x8a\xff\x8a\x8b\x8b\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x53\x53\x53\xff\x57\x56\x56\xff\x59\x59\x59\
\xff\x5d\x5d\x5c\xff\x5f\x5f\x5f\xff\x62\x62\x62\xff\x65\x65\x65\
\xff\x68\x68\x68\xff\x6c\x6b\x6b\xff\x6e\x6e\x6e\xff\x70\x71\x71\
\xff\x74\x73\x74\xff\x76\x76\x76\xff\x79\x79\x78\xff\x7b\x7b\x7b\
\xff\x7d\x7d\x7d\xff\x80\x80\x80\xff\x82\x82\x82\xff\x83\x84\x84\
\xff\x86\x86\x86\xff\x87\x87\x87\xff\x89\x89\x8a\xff\x8a\x8b\x8b\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8b\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x50\x50\x50\xff\x53\x53\x53\xff\x56\x56\x56\
\xff\x5a\x59\x59\xff\x5c\x5c\x5c\xff\x60\x5f\x5f\xff\x62\x63\x62\
\xff\x66\x66\x65\xff\x68\x68\x69\xff\x6b\x6b\x6b\xff\x6e\x6e\x6e\
\xff\x71\x71\x71\xff\x74\x73\x74\xff\x76\x76\x76\xff\x78\x79\x79\
\xff\x7b\x7b\x7b\xff\x7e\x7d\x7d\xff\x80\x80\x80\xff\x82\x81\x82\
\xff\x84\x84\x84\xff\x85\x86\x86\xff\x88\x87\x87\xff\x89\x89\x89\
\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x4d\x4d\x4c\xff\x4f\x4f\x50\xff\x53\x53\x53\
\xff\x55\x56\x56\xff\x59\x59\x59\xff\xd7\xd7\xd7\xff\xd7\xd7\xd7\
\xff\x9e\x9d\x9d\xff\x65\x65\x66\xff\x68\x68\x68\xff\x6b\x6b\x6b\
\xff\x6e\x6e\x6e\xff\x70\x70\x70\xff\xb1\xb0\xb0\xff\xdd\xdd\xdd\
\xff\xcd\xcd\xcd\xff\x94\x94\x94\xff\x7e\x7d\x7d\xff\x80\x80\x80\
\xff\x82\x82\x82\xff\x84\x84\x84\xff\x85\x85\x85\xff\x87\x87\x87\
\xff\x89\x89\x89\xff\x8b\x8b\x8b\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x49\x4a\x49\xff\x4c\x4c\x4c\xff\x50\x4f\x4f\
\xff\x52\x53\x52\xff\x56\x55\x56\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xaf\xaf\xaf\xff\x62\x62\x62\xff\x65\x65\x65\xff\x68\x68\x68\
\xff\x6a\x6b\x6b\xff\x6e\x6e\x6e\xff\xdc\xdc\xdc\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xf7\xf7\xf7\xff\x8c\x8c\x8c\xff\x7e\x7d\x7e\
\xff\x7f\x80\x7f\xff\x82\x82\x82\xff\x83\x84\x83\xff\x86\x86\x85\
\xff\x88\x87\x87\xff\x89\x89\x89\xff\x8b\x8a\x8b\xff\x8c\x8b\x8c\
\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x46\x46\x47\xff\x49\x49\x49\xff\x4d\x4c\x4d\
\xff\x50\x4f\x4f\xff\x52\x52\x53\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xad\xae\xae\xff\x5f\x5f\x5f\xff\x62\x62\x62\xff\x65\x65\x65\
\xff\x68\x67\x68\xff\x6a\x6b\x6b\xff\x92\x92\x92\xff\xa6\xa6\xa6\
\xff\xf7\xf7\xf7\xff\xff\xff\xff\xff\xcd\xcd\xcd\xff\x7b\x7b\x7a\
\xff\x7d\x7d\x7e\xff\x7f\x80\x80\xff\x81\x81\x82\xff\x83\x83\x84\
\xff\x86\x85\x86\xff\x87\x87\x87\xff\x89\x89\x89\xff\x8a\x8a\x8a\
\xff\x8b\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x43\x43\x43\xff\x46\x46\x46\xff\x49\x49\x49\
\xff\x4d\x4d\x4c\xff\x4f\x4f\x50\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xac\xac\xac\xff\x85\x85\x84\xff\xb9\xb9\xb9\xff\x75\x76\x76\
\xff\x65\x65\x65\xff\x67\x67\x68\xff\x6b\x6b\x6a\xff\x6e\x6d\x6d\
\xff\xaf\xaf\xaf\xff\xff\xff\xff\xff\xff\xff\xff\xff\x81\x80\x80\
\xff\x7a\x7a\x7b\xff\x7d\x7d\x7d\xff\x9f\x9f\x9f\xff\xc0\xc0\xc0\
\xff\xc1\xc1\xc1\xff\xc2\xc2\xc2\xff\xc4\xc3\xc3\xff\xc4\xc4\xc4\
\xff\xb7\xb7\xb7\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x40\x3f\x40\xff\x43\x43\x43\xff\x46\x46\x46\
\xff\x49\x49\x49\xff\x4c\x4c\x4c\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xf5\xf5\xf5\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xce\xce\xce\xff\x64\x64\x65\xff\x67\x67\x67\xff\x6a\x6b\x6a\
\xff\xd2\xd2\xd2\xff\xff\xff\xff\xff\xff\xff\xff\xff\xb2\xb2\xb2\
\xff\x78\x78\x78\xff\x7b\x7a\x7a\xff\xbe\xbe\xbe\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xe2\xe2\xe2\xff\x8b\x8a\x8a\xff\x8c\x8c\x8c\xff\x8c\x8c\x8c\
\xff\x8c\x8c\x8c\xff\x3d\x3d\x3d\xff\x40\x40\x40\xff\x43\x43\x43\
\xff\x46\x46\x46\xff\x49\x49\x49\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xf5\xf5\xf5\xff\xaa\xaa\xaa\xff\xd6\xd6\xd6\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x9c\x9c\x9c\xff\x64\x64\x65\xff\x7a\x7a\x7b\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xe5\xe5\xe5\
\xff\x76\x76\x75\xff\x78\x78\x78\xff\xbd\xbd\xbd\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xc0\xc1\xc0\xff\xc1\xc1\xc1\xff\xc2\xc2\xc2\
\xff\xb4\xb4\xb4\xff\x89\x88\x88\xff\x8a\x8b\x8a\xff\x8c\x8b\x8c\
\xff\x8c\x8c\x8c\xff\x3a\x3a\x3a\xff\x3d\x3d\x3d\xff\x40\x3f\x40\
\xff\x42\x43\x42\xff\x45\x45\x46\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xbd\xbd\xbd\xff\x52\x52\x51\xff\x60\x60\x60\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xb9\xb9\xb9\xff\x62\x62\x61\xff\xb2\xb2\xb2\
\xff\xff\xff\xff\xff\xe4\xe4\xe4\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\x8d\x8d\x8d\xff\x75\x75\x76\xff\xbc\xbb\xbb\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x7f\x7f\x7f\xff\x82\x82\x81\xff\x83\x83\x83\
\xff\x85\x85\x85\xff\x87\x87\x87\xff\x89\x88\x88\xff\x8a\x8a\x8a\
\xff\x8b\x8b\x8c\xff\x37\x37\x36\xff\x39\x39\x3a\xff\x3d\x3c\x3d\
\xff\x40\x3f\x3f\xff\x42\x43\x42\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xb1\xb1\xb1\xff\x4e\x4e\x4f\xff\x51\x52\x52\xff\xea\xea\xea\
\xff\xff\xff\xff\xff\xd6\xd6\xd6\xff\x5e\x5e\x5e\xff\xec\xec\xec\
\xff\xff\xff\xff\xff\xbd\xbd\xbd\xff\xd1\xd1\xd1\xff\xff\xff\xff\
\xff\xc1\xc0\xc0\xff\x73\x72\x73\xff\xba\xba\xba\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x7c\x7d\x7c\xff\x7f\x7f\x7f\xff\x81\x81\x81\
\xff\x83\x83\x83\xff\x85\x85\x86\xff\x87\x87\x87\xff\x89\x89\x89\
\xff\x8a\x8a\x8a\xff\x34\x34\x34\xff\x37\x37\x37\xff\x39\x39\x39\
\xff\x3d\x3c\x3c\xff\x3f\x3f\x3f\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xe9\xe9\xe9\xff\x62\x62\x62\xff\x70\x70\x6f\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xab\xac\xac\xff\x8e\x8e\x8e\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x81\x81\x81\xff\xa0\xa0\xa0\xff\xff\xff\xff\
\xff\xf6\xf6\xf6\xff\x70\x70\x70\xff\xb9\xb9\xb9\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x7a\x7a\x7a\xff\x7d\x7d\x7c\xff\x7f\x7e\x7e\
\xff\x81\x81\x81\xff\x83\x83\x84\xff\x85\x85\x85\xff\x87\x87\x86\
\xff\x89\x88\x88\xff\x31\x31\x31\xff\x34\x34\x34\xff\x37\x37\x37\
\xff\x39\x3a\x3a\xff\x3c\x3c\x3d\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x80\x80\x80\xff\xcb\xcb\xcb\xff\xff\xff\xff\
\xff\xeb\xeb\xeb\xff\x60\x61\x61\xff\x6d\x6e\x6e\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x9a\x9a\x9b\xff\xb7\xb8\xb7\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x77\x77\x77\xff\x7a\x7a\x7a\xff\x7d\x7c\x7c\
\xff\x7f\x7f\x7e\xff\x81\x81\x81\xff\x83\x83\x83\xff\x85\x85\x85\
\xff\x86\x87\x86\xff\x2f\x2f\x2e\xff\x32\x31\x31\xff\x34\x34\x34\
\xff\x36\x36\x37\xff\x39\x39\x3a\xff\xcf\xcf\xcf\xff\xd0\xd0\xd0\
\xff\x89\x89\x89\xff\x8b\x8b\x8b\xff\xe9\xe9\xe9\xff\xbc\xbc\xbc\
\xff\x7b\x7a\x7a\xff\x5d\x5c\x5c\xff\xd5\xd5\xd5\xff\xd6\xd6\xd6\
\xff\xad\xad\xad\xff\x5d\x5d\x5e\xff\x61\x61\x60\xff\xc5\xc5\xc5\
\xff\xd9\xd9\xd9\xff\xb5\xb5\xb5\xff\xb6\xb6\xb6\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x74\x75\x75\xff\x77\x78\x77\xff\x7a\x7a\x79\
\xff\x7c\x7c\x7d\xff\x7e\x7f\x7e\xff\x81\x81\x81\xff\x83\x83\x83\
\xff\x85\x85\x85\xff\x2c\x2c\x2c\xff\x2f\x2e\x2f\xff\x31\x31\x31\
\xff\x33\x34\x34\xff\x36\x36\x37\xff\x39\x39\x39\xff\x3c\x3c\x3c\
\xff\x3f\x3f\x3f\xff\x42\x42\x42\xff\x45\x45\x45\xff\x48\x48\x48\
\xff\x4b\x4b\x4b\xff\x4e\x4e\x4e\xff\x51\x51\x51\xff\x54\x54\x54\
\xff\x57\x58\x57\xff\x5a\x5a\x5b\xff\x5d\x5e\x5d\xff\x60\x60\x61\
\xff\x64\x64\x63\xff\x66\x67\x67\xff\xb4\xb5\xb4\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x72\x72\x72\xff\x74\x74\x74\xff\x77\x77\x77\
\xff\x7a\x7a\x7a\xff\x7d\x7c\x7c\xff\x7f\x7e\x7e\xff\x81\x80\x81\
\xff\x83\x83\x83\xff\x29\x29\x2a\xff\x2b\x2c\x2c\xff\x2f\x2e\x2e\
\xff\x31\x31\x31\xff\x33\x33\x33\xff\x36\x36\x36\xff\x39\x39\x39\
\xff\x3c\x3c\x3c\xff\x3f\x3f\x3f\xff\x42\x42\x42\xff\x45\x45\x45\
\xff\x48\x48\x48\xff\x4b\x4b\x4b\xff\x4e\x4e\x4e\xff\x52\x51\x51\
\xff\x54\x54\x54\xff\x57\x57\x57\xff\x5a\x5b\x5b\xff\x5d\x5e\x5e\
\xff\x60\x61\x60\xff\x63\x63\x63\xff\xb3\xb3\xb3\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\x70\x70\x6f\xff\x72\x72\x72\xff\x74\x74\x74\
\xff\x77\x77\x77\xff\x7a\x79\x79\xff\x7c\x7c\x7c\xff\x7e\x7f\x7e\
\xff\x80\x81\x81\xff\x27\x27\x27\xff\x29\x29\x2a\xff\x2c\x2c\x2c\
\xff\x2e\x2e\x2f\xff\x31\x31\x31\xff\x33\x33\x33\xff\x36\x36\x36\
\xff\x39\x39\x39\xff\x3c\x3c\x3c\xff\x3f\x3f\x3f\xff\x41\x42\x42\
\xff\x45\x45\x45\xff\x48\x48\x48\xff\x4b\x4b\x4b\xff\x4e\x4e\x4e\
\xff\x51\x51\x51\xff\x54\x54\x54\xff\x58\x57\x57\xff\x5b\x5a\x5a\
\xff\x5e\x5d\x5d\xff\x60\x60\x61\xff\x8a\x8a\x8b\xff\xb3\xb3\xb3\
\xff\xb5\xb5\xb4\xff\x6c\x6c\x6c\xff\x6f\x6e\x6f\xff\x72\x71\x72\
\xff\x75\x74\x74\xff\x77\x77\x77\xff\x7a\x79\x7a\xff\x7c\x7c\x7c\
\xff\x7e\x7e\x7e\xff\x24\x25\x24\xff\x26\x27\x27\xff\x2a\x29\x2a\
\xff\x2c\x2b\x2c\xff\x2e\x2f\x2e\xff\x31\x31\x31\xff\x33\x34\x33\
\xff\x36\x36\x36\xff\x39\x39\x38\xff\x3c\x3b\x3b\xff\x3e\x3f\x3e\
\xff\x42\x42\x42\xff\x45\x45\x45\xff\x48\x48\x48\xff\x4b\x4b\x4b\
\xff\x4e\x4e\x4e\xff\x50\x51\x51\xff\x54\x54\x54\xff\x57\x57\x57\
\xff\x5a\x5b\x5b\xff\x5d\x5d\x5d\xff\x60\x61\x60\xff\x63\x64\x63\
\xff\x66\x66\x66\xff\x6a\x69\x69\xff\x6c\x6c\x6c\xff\x6f\x6e\x6f\
\xff\x71\x72\x71\xff\x74\x74\x74\xff\x77\x77\x77\xff\x79\x79\x79\
\xff\x7c\x7c\x7b\xff\x22\x23\x22\xff\x25\x25\x25\xff\x27\x27\x27\
\xff\x29\x29\x29\xff\x2c\x2b\x2b\xff\x2e\x2e\x2e\xff\x30\x30\x30\
\xff\x33\x33\x33\xff\x36\x36\x36\xff\x39\x39\x39\xff\x3b\x3c\x3b\
\xff\x3f\x3e\x3f\xff\x42\x42\x42\xff\x45\x44\x45\xff\x47\x47\x47\
\xff\x4b\x4a\x4a\xff\x4e\x4d\x4d\xff\x51\x51\x51\xff\x54\x54\x54\
\xff\x57\x57\x57\xff\x5a\x5a\x5a\xff\x5d\x5d\x5d\xff\x60\x60\x60\
\xff\x63\x63\x63\xff\x66\x66\x66\xff\x69\x69\x69\xff\x6c\x6c\x6c\
\xff\x6e\x6f\x6f\xff\x72\x71\x72\xff\x74\x74\x75\xff\x77\x77\x76\
\xff\x79\x7a\x7a\xff\x21\x21\x21\xff\x23\x22\x23\xff\x25\x24\x25\
\xff\x27\x27\x26\xff\x29\x29\x29\xff\x2c\x2b\x2b\xff\x2e\x2e\x2d\
\xff\x30\x31\x31\xff\x33\x33\x33\xff\x36\x36\x35\xff\x39\x39\x38\
\xff\x3b\x3b\x3b\xff\x3f\x3e\x3e\xff\x41\x41\x42\xff\x44\x44\x45\
\xff\x47\x47\x48\xff\x4b\x4a\x4a\xff\x4d\x4d\x4d\xff\x50\x51\x51\
\xff\x54\x54\x54\xff\x57\x57\x57\xff\x5a\x5a\x5a\xff\x5c\x5d\x5d\
\xff\x60\x60\x60\xff\x63\x63\x63\xff\x66\x66\x65\xff\x69\x69\x69\
\xff\x6b\x6c\x6c\xff\x6f\x6e\x6f\xff\x71\x71\x71\xff\x75\x74\x74\
\xff\x76\x77\x76\xff\x1f\x1f\x1e\xff\x21\x20\x20\xff\x22\x23\x22\
\xff\x24\x25\x25\xff\x26\x26\x27\xff\x29\x29\x29\xff\x2b\x2b\x2c\
\xff\x2e\x2e\x2e\xff\x30\x31\x31\xff\x33\x33\x33\xff\x36\x36\x35\
\xff\x39\x39\x39\xff\x3b\x3c\x3c\xff\x3e\x3e\x3e\xff\x41\x41\x41\
\xff\x44\x44\x44\xff\x48\x48\x47\xff\x4a\x4a\x4a\xff\x4d\x4d\x4d\
\xff\x50\x50\x50\xff\x54\x53\x53\xff\x57\x57\x57\xff\x5a\x59\x5a\
\xff\x5c\x5d\x5d\xff\x60\x5f\x60\xff\x63\x63\x63\xff\x66\x65\x66\
\xff\x69\x69\x69\xff\x6c\x6b\x6c\xff\x6e\x6e\x6f\xff\x71\x71\x71\
\xff\x74\x73\x74\xff\x1d\x1d\x1d\xff\x1e\x1f\x1f\xff\x21\x20\x21\
\xff\x22\x22\x22\xff\x24\x24\x24\xff\x26\x27\x26\xff\x29\x29\x29\
\xff\x2b\x2b\x2b\xff\x2e\x2d\x2d\xff\x30\x31\x30\xff\x33\x33\x33\
\xff\x35\x36\x35\xff\x39\x38\x39\xff\x3b\x3b\x3b\xff\x3e\x3e\x3e\
\xff\x41\x41\x41\xff\x44\x44\x44\xff\x47\x48\x47\xff\x4a\x4a\x4a\
\xff\x4d\x4d\x4d\xff\x50\x50\x50\xff\x53\x53\x53\xff\x57\x57\x56\
\xff\x5a\x59\x5a\xff\x5d\x5c\x5c\xff\x60\x60\x60\xff\x63\x63\x62\
\xff\x65\x65\x66\xff\x69\x68\x69\xff\x6c\x6b\x6b\xff\x6e\x6e\x6e\
\xff\x71\x71\x71\xff\x1c\x1c\x1b\xff\x1d\x1d\x1d\xff\x1e\x1f\x1f\
\xff\x20\x20\x20\xff\x22\x23\x22\xff\x24\x24\x25\xff\x27\x27\x26\
\xff\x28\x29\x28\xff\x2b\x2b\x2b\xff\x2e\x2e\x2d\xff\x30\x30\x30\
\xff\x33\x33\x33\xff\x35\x36\x36\xff\x39\x38\x38\xff\x3b\x3b\x3b\
\xff\x3e\x3e\x3e\xff\x41\x41\x41\xff\x44\x44\x44\xff\x47\x47\x47\
\xff\x4a\x4a\x4a\xff\x4d\x4d\x4d\xff\x50\x50\x50\xff\x53\x53\x53\
\xff\x56\x56\x56\xff\x59\x59\x59\xff\x5c\x5d\x5d\xff\x60\x5f\x60\
\xff\x63\x63\x62\xff\x65\x65\x66\xff\x68\x68\x69\xff\x6c\x6b\x6c\
\xff\x6e\x6e\x6e\xff\x1a\x1a\x1a\xff\x1b\x1b\x1b\xff\x1d\x1d\x1d\
\xff\x1e\x1e\x1f\xff\x20\x20\x20\xff\x22\x22\x22\xff\x24\x25\x24\
\xff\x27\x27\x26\xff\x29\x28\x28\xff\x2b\x2a\x2b\xff\x2e\x2d\x2e\
\xff\x30\x30\x30\xff\x33\x32\x33\xff\x36\x35\x36\xff\x38\x38\x38\
\xff\x3b\x3a\x3b\xff\x3e\x3d\x3d\xff\x40\x40\x40\xff\x43\x44\x44\
\xff\x47\x47\x47\xff\x4a\x4a\x4a\xff\x4d\x4d\x4d\xff\x50\x50\x50\
\xff\x53\x53\x53\xff\x56\x56\x56\xff\x59\x59\x59\xff\x5c\x5c\x5c\
\xff\x5f\x5f\x5f\xff\x63\x62\x63\xff\x65\x65\x66\xff\x68\x69\x68\
\xff\x6b\x6b\x6b\xff\x1a\x1a\x1a\xff\x1a\x1a\x1a\xff\x1c\x1b\x1b\
\xff\x1d\x1c\x1d\xff\x1e\x1f\x1f\xff\x20\x20\x21\xff\x22\x22\x22\
\xff\x24\x24\x24\xff\x26\x26\x26\xff\x29\x28\x28\xff\x2a\x2b\x2b\
\xff\x2d\x2e\x2d\xff\x30\x30\x30\xff\x33\x33\x32\xff\x35\x36\x35\
\xff\x38\x38\x37\xff\x3a\x3b\x3a\xff\x3d\x3d\x3e\xff\x40\x41\x41\
\xff\x43\x43\x43\xff\x47\x47\x47\xff\x49\x49\x4a\xff\x4d\x4d\x4c\
\xff\x4f\x50\x50\xff\x53\x53\x53\xff\x56\x56\x56\xff\x59\x59\x59\
\xff\x5c\x5d\x5c\xff\x5f\x5f\x5f\xff\x63\x62\x62\xff\x65\x65\x65\
\xff\x69\x68\x69\xff\x1a\x1a\x1a\xff\x1a\x1a\x1a\xff\x1a\x1a\x1a\
\xff\x1b\x1b\x1c\xff\x1d\x1d\x1c\xff\x1e\x1e\x1e\xff\x21\x20\x20\
\xff\x22\x22\x22\xff\x24\x24\x24\xff\x26\x26\x26\xff\x29\x29\x28\
\xff\x2b\x2b\x2b\xff\x2d\x2d\x2d\xff\x30\x30\x30\xff\x32\x32\x32\
\xff\x35\x35\x35\xff\x38\x38\x38\xff\x3a\x3b\x3a\xff\x3e\x3e\x3e\
\xff\x40\x40\x40\xff\x43\x44\x43\xff\x47\x47\x46\xff\x4a\x4a\x4a\
\xff\x4d\x4c\x4d\xff\x50\x50\x4f\xff\x53\x53\x52\xff\x56\x56\x56\
\xff\x59\x59\x59\xff\x5c\x5c\x5c\xff\x5f\x60\x5f\xff\x62\x62\x63\
\xff\x65\x65\x65\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\
"

qt_resource_name = "\
\x00\x03\
\x00\x00\x77\xfc\
\x00\x70\
\x00\x79\x00\x6c\
\x00\x05\
\x00\x6f\xa6\x53\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\
\x00\x07\
\x07\xff\x4f\x7f\
\x00\x70\
\x00\x79\x00\x6c\x00\x2e\x00\x69\x00\x63\x00\x6f\
"

qt_resource_struct = "\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x0c\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x1c\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
