#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-container library"

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
	    'boost/libs/container/src/alloc_lib.c',
	    'boost/libs/container/src/dlmalloc.cpp',
	    'boost/libs/container/src/global_resource.cpp',
	    'boost/libs/container/src/monotonic_buffer_resource.cpp',
	    'boost/libs/container/src/pool_resource.cpp',
	    'boost/libs/container/src/synchronized_pool_resource.cpp',
	    'boost/libs/container/src/unsynchronized_pool_resource.cpp',
	    ])
	
	my_module.add_flag('c', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CONTAINER_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CONTAINER_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
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
	    'pthread',
	    ])
	return True


