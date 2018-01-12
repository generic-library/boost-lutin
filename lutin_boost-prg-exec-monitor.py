#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-prg-exec-monitor library"

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
	    'boost/libs/test/src/execution_monitor.cpp',
	    'boost/libs/test/src/debug.cpp',
	    'boost/libs/test/src/cpp_main.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CHRONO_DYN_LINK=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_NO_DEPRECATED',
	    '-DBOOST_TEST_DYN_LINK=1',
	    '-DBOOST_TIMER_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-pedantic',
	    '-Wno-variadic-macros',
	    ])
	
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    'boost-timer',
	    'boost-system',
	    ])
	return True


