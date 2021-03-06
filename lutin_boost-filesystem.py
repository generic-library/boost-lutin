#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-filesystem library"

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
	    'boost/libs/filesystem/src/codecvt_error_category.cpp',
	    'boost/libs/filesystem/src/operations.cpp',
	    'boost/libs/filesystem/src/path.cpp',
	    'boost/libs/filesystem/src/path_traits.cpp',
	    'boost/libs/filesystem/src/portability.cpp',
	    'boost/libs/filesystem/src/unique_path.cpp',
	    'boost/libs/filesystem/src/utf8_codecvt_facet.cpp',
	    'boost/libs/filesystem/src/windows_file_codecvt.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_FILESYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
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
	    'boost-system',
	    ])
	return True


