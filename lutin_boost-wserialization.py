#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-wserialization library"

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
	    'boost/libs/serialization/src/basic_text_wiprimitive.cpp',
	    'boost/libs/serialization/src/basic_text_woprimitive.cpp',
	    'boost/libs/serialization/src/text_wiarchive.cpp',
	    'boost/libs/serialization/src/text_woarchive.cpp',
	    'boost/libs/serialization/src/xml_wgrammar.cpp',
	    'boost/libs/serialization/src/xml_wiarchive.cpp',
	    'boost/libs/serialization/src/xml_woarchive.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_SERIALIZATION_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-ftemplate-depth-255',
	    '-fvisibility=hidden',
	    '-fvisibility-inlines-hidden',
	    ])
	
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    'boost-serialization',
	    ])
	return True


