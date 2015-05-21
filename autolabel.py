#!/usr/bin/env python
##############################################################################
# -*- coding: utf-8 -*-
# Project:     Autolabel
# Module:      autolabel.py
# Purpose:     Auto labeled for laptops
# Language:    Python 2.5
# Date:        16-Oct-2014
# Ver:         16-Oct-2014
# Author:      Manuel Mora Gordillo
# Copyright:   2014 - Manuel Mora Gordillo    <manuito @nospam@ gmail.com>
#
# Autolabel is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# Autolabel is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with Autolabel. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from LdapConnection import LdapConnection
import fcntl, socket, struct
import fileinput
import os
import time
import ConfigParser

time.sleep(20)

dir = "/usr/share/autolabel"
defaultImage = "/usr/share/icons/gnome/48x48/places/icono-inicio.png"

def getHwAddr(ifname):
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
	return ''.join(['%02x:' % ord(char) for char in info[18:24]])[:-1]


def removeWhitespaces():
	for lines in fileinput.FileInput('/etc/gdm3/greeter.gsettings', inplace=1):    
	    lines = lines.strip()
	    print lines

def removePhoto():
        try:
		os.remove(dir+"/userphoto.jpg")
        except:
                pass

def getConfigUsername():
	parser = ConfigParser.SafeConfigParser(allow_no_value=True)
	parser.read(dir+'/config')
	username = parser.get('main', 'username')

	return username

def setConfigUsername(user):
	parser = ConfigParser.SafeConfigParser(allow_no_value=True)
	parser.read(dir+'/config')
	parser.set('main', 'username',user)

	with open(dir+'/config', 'w') as fp:
	    parser.write(fp)

	return username


def setData(name, photo):
	parser = ConfigParser.SafeConfigParser(allow_no_value=True)

	try:
		parser.read('/etc/gdm3/greeter.gsettings')
	except:
		removeWhitespaces()
		parser.read('/etc/gdm3/greeter.gsettings')

	parser.set('org.gnome.login-screen', 'logo', '\''+photo+'\'')
	parser.set('org.gnome.login-screen', 'fallback-logo', '\''+photo+'\'')
	parser.set('org.gnome.login-screen', 'banner-message-enable', 'true')
	parser.set('org.gnome.login-screen', 'banner-message-text', '\''+name+'\'')

	with open('/etc/gdm3/greeter.gsettings', 'w') as fp:
	    parser.write(fp)

def setDefault():
	setData("IES Sta Eulalia",defaultImage)
	setConfigUsername("default")
	removePhoto()

# try connection
response = os.system("ping -c 1 ldap")
if response != 0:
	exit()

# get mac
mac = getHwAddr('eth0')

# get username
l = LdapConnection("ldap", "", "")
l.connectauth()
search  = l.search("cn=DHCP Config","(dhcpHWAddress=ethernet " + mac + ")",["cn","uniqueIdentifier"])

try:
	username = search[0][0][1]['uniqueIdentifier'][0].replace("user-name ","")
except:
	username = ""

u = getConfigUsername()

if username == "" and u!="default":
	setDefault()

elif username!="" and username!=u:
	# get user data
	search  = l.search("ou=People","(uid="+username+")",["cn","jpegPhoto"])

	try:
		name = search[0][0][1]['cn'][0]
	except:
		name = username

	try:
		photo = search[0][0][1]['jpegPhoto'][0]
	except:
		photo = ""

	setConfigUsername(username)

	if photo=="":
		photo = defaultImage
		removePhoto()

	elif photo!="":
	        f = open(dir+"/userphoto.jpg","w+")
        	f.write(photo)
	        f.close()

		photo = dir+"/userphoto.jpg"

	# Set gdm banner
	setData(name, photo)

