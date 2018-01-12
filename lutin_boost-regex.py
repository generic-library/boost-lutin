#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-regex library"

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
	    'boost/libs/regex/build/../src/c_regex_traits.cpp',
	    'boost/libs/regex/build/../src/cpp_regex_traits.cpp',
	    'boost/libs/regex/build/../src/cregex.cpp',
	    'boost/libs/regex/build/../src/fileiter.cpp',
	    'boost/libs/regex/build/../src/icu.cpp',
	    'boost/libs/regex/build/../src/instances.cpp',
	    'boost/libs/regex/build/../src/posix_api.cpp',
	    'boost/libs/regex/build/../src/regex.cpp',
	    'boost/libs/regex/build/../src/regex_debug.cpp',
	    'boost/libs/regex/build/../src/regex_raw_buffer.cpp',
	    'boost/libs/regex/build/../src/regex_traits_defaults.cpp',
	    'boost/libs/regex/build/../src/static_mutex.cpp',
	    'boost/libs/regex/build/../src/w32_regex_traits.cpp',
	    'boost/libs/regex/build/../src/wc_regex_traits.cpp',
	    'boost/libs/regex/build/../src/wide_posix_api.cpp',
	    'boost/libs/regex/build/../src/winstances.cpp',
	    'boost/libs/regex/build/../src/usinstances.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_HAS_ICU=1',
	    '-DBOOST_REGEX_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-pedantic',
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


