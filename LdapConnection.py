#!/usr/bin/env python
##############################################################################
# -*- coding: utf-8 -*-
# Project:     Autolabel
# Module:      LdapConnection.py
# Purpose:     Ldap connection
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

import ldap

class LdapConnection(object):

    def __init__(self,host,username,password):
		self.host = host
		self.username = username
		self.password = password

    def connectauth(self):
    	self.connectauth = ldap.open (self.host)
    	try:
		#self.connectauth = ldap.initialize(self.host)
	        # you should  set this to ldap.VERSION2 if you're using a v2 directory
	        self.protocol_version = ldap.VERSION3

	        # Any errors will throw an ldap.LDAPError exception 
	        # or related exception so you can ignore the result
	        self.connectauth.simple_bind_s(self.username, self.password)
    	except ldap.CONFIDENTIALITY_REQUIRED:
    		try:
                	self.connectauth=ldap.initialize("ldaps://" +self.host)
                	self.connectauth.simple_bind_s(self.username,self.password)
                	return True
            	except ldap.LDAPError,e:
    			print e
                	return False

	return True

    def connectanonim(self):
    	self.connectanonim = ldap.open (self.host)
    	try:
		#self.connectauth = ldap.initialize(self.host)
	        # you should  set this to ldap.VERSION2 if you're using a v2 directory
	        self.protocol_version = ldap.VERSION3

	        # Any errors will throw an ldap.LDAPError exception 
	        # or related exception so you can ignore the result
	        self.connectanonim.simple_bind_s()
    	except ldap.CONFIDENTIALITY_REQUIRED:
    		try:
                	self.connectanonim=ldap.initialize("ldaps://" +self.host)
                	self.connectanonim.simple_bind_s()
                	return True
            	except ldap.LDAPError,e:
    			print e
                	return False

	return True

    def search(self,baseDN,filter,retrieveAttributes):
		try:
			ldap_result_id = self.connectauth.search(baseDN+",dc=instituto,dc=extremadura,dc=es", ldap.SCOPE_SUBTREE, filter, retrieveAttributes)
			result_set = []
			while 1:
				result_type, result_data = self.connectauth.result(ldap_result_id, 0)
				if (result_data == []):
					break
				else:
					if result_type == ldap.RES_SEARCH_ENTRY:
						result_set.append(result_data)
			return result_set
		except ldap.LDAPError, e:
			print e
