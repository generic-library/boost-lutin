#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-date-time library"

#def get_licence():
#	return "UNKNOW"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "boost"

#def get_maintainer():
#	return "UNKNOW"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.add_src_file([
	    'boost/libs/date_time/src/gregorian/greg_month.cpp',
	    'boost/libs/date_time/src/gregorian/greg_weekday.cpp',
	    'boost/libs/date_time/src/gregorian/date_generators.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_DYN_LINK=1',
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DDATE_TIME_INLINE',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    ])
	
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    ])
	return True


