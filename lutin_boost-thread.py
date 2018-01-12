#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-thread library"

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
	    'boost/libs/thread/src/pthread/thread.cpp',
	    'boost/libs/thread/src/pthread/once.cpp',
	    'boost/libs/thread/src/future.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_THREAD_BUILD_DLL=1',
	    '-DBOOST_THREAD_DONT_USE_CHRONO',
	    '-DBOOST_THREAD_POSIX',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-pedantic',
	    '-Wextra',
	    '-Wno-long-long',
	    '-Wno-unused-parameter',
	    '-Wunused-function',
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


