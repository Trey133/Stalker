#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 22:34:56 2017

@author: root
"""
import sys
from termcolor import colored
sys.path.insert(0, '/usr/share/stalker')
import basic
encrypt = basic.encrypt
decrypt = basic.decrypt
with open('/usr/share/stalker/gpg_test_file','w') as file:
    file.write("Testing\n Testing\n  Testing")
    file.close()
data = open('/usr/share/stalker/gpg_test_file','r')
data.read()
print colored(data,'blue',attrs=['bold'])
encrypt('/usr/share/stalker/gpg_test_file')
data = open('/usr/share/stalker/gpg_test_file','r')
data.read()
decrypt('/usr/share/stalker/gpg_test_file','/usr/share/stalker/gpg_test_file')
data = open('/usr/share/stalker/gpg_test_file','r')
data.read()