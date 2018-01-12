#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-serialization library"

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
	    'boost/libs/serialization/src/basic_archive.cpp',
	    'boost/libs/serialization/src/basic_iarchive.cpp',
	    'boost/libs/serialization/src/basic_iserializer.cpp',
	    'boost/libs/serialization/src/basic_oarchive.cpp',
	    'boost/libs/serialization/src/basic_oserializer.cpp',
	    'boost/libs/serialization/src/basic_pointer_iserializer.cpp',
	    'boost/libs/serialization/src/basic_pointer_oserializer.cpp',
	    'boost/libs/serialization/src/basic_serializer_map.cpp',
	    'boost/libs/serialization/src/basic_text_iprimitive.cpp',
	    'boost/libs/serialization/src/basic_text_oprimitive.cpp',
	    'boost/libs/serialization/src/basic_xml_archive.cpp',
	    'boost/libs/serialization/src/binary_iarchive.cpp',
	    'boost/libs/serialization/src/binary_oarchive.cpp',
	    'boost/libs/serialization/src/extended_type_info.cpp',
	    'boost/libs/serialization/src/extended_type_info_typeid.cpp',
	    'boost/libs/serialization/src/extended_type_info_no_rtti.cpp',
	    'boost/libs/serialization/src/polymorphic_iarchive.cpp',
	    'boost/libs/serialization/src/polymorphic_oarchive.cpp',
	    'boost/libs/serialization/src/stl_port.cpp',
	    'boost/libs/serialization/src/text_iarchive.cpp',
	    'boost/libs/serialization/src/text_oarchive.cpp',
	    'boost/libs/serialization/src/void_cast.cpp',
	    'boost/libs/serialization/src/archive_exception.cpp',
	    'boost/libs/serialization/src/xml_grammar.cpp',
	    'boost/libs/serialization/src/xml_iarchive.cpp',
	    'boost/libs/serialization/src/xml_oarchive.cpp',
	    'boost/libs/serialization/src/xml_archive_exception.cpp',
	    'boost/libs/serialization/src/codecvt_null.cpp',
	    'boost/libs/serialization/src/utf8_codecvt_facet.cpp',
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
	    ])
	return True


