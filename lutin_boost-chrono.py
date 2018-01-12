#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-chrono library"

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
	    'boost/libs/chrono/src/chrono.cpp',
	    'boost/libs/chrono/src/thread_clock.cpp',
	    'boost/libs/chrono/src/process_cpu_clocks.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_DYN_LINK=1',
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_NO_DEPRECATED',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-pedantic',
	    '-Wextra',
	    '-Wno-long-long',
	    ])
	
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    'boost-system',
	    ])
	return True

