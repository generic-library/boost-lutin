#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-program-options library"

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
	    'boost/libs/program_options/src/cmdline.cpp',
	    'boost/libs/program_options/src/config_file.cpp',
	    'boost/libs/program_options/src/options_description.cpp',
	    'boost/libs/program_options/src/parsers.cpp',
	    'boost/libs/program_options/src/variables_map.cpp',
	    'boost/libs/program_options/src/value_semantic.cpp',
	    'boost/libs/program_options/src/positional_options.cpp',
	    'boost/libs/program_options/src/utf8_codecvt_facet.cpp',
	    'boost/libs/program_options/src/convert.cpp',
	    'boost/libs/program_options/src/winmain.cpp',
	    'boost/libs/program_options/src/split.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_PROGRAM_OPTIONS_DYN_LINK=1',
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


