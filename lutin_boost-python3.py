#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-python3 library"

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
	    'boost/libs/python/src/list.cpp',
	    'boost/libs/python/src/long.cpp',
	    'boost/libs/python/src/dict.cpp',
	    'boost/libs/python/src/tuple.cpp',
	    'boost/libs/python/src/str.cpp',
	    'boost/libs/python/src/slice.cpp',
	    'boost/libs/python/src/converter/from_python.cpp',
	    'boost/libs/python/src/converter/registry.cpp',
	    'boost/libs/python/src/converter/type_id.cpp',
	    'boost/libs/python/src/object/enum.cpp',
	    'boost/libs/python/src/object/class.cpp',
	    'boost/libs/python/src/object/function.cpp',
	    'boost/libs/python/src/object/inheritance.cpp',
	    'boost/libs/python/src/object/life_support.cpp',
	    'boost/libs/python/src/object/pickle_support.cpp',
	    'boost/libs/python/src/errors.cpp',
	    'boost/libs/python/src/module.cpp',
	    'boost/libs/python/src/converter/builtin_converters.cpp',
	    'boost/libs/python/src/converter/arg_to_python_base.cpp',
	    'boost/libs/python/src/object/iterator.cpp',
	    'boost/libs/python/src/object/stl_iterator.cpp',
	    'boost/libs/python/src/object_protocol.cpp',
	    'boost/libs/python/src/object_operators.cpp',
	    'boost/libs/python/src/wrapper.cpp',
	    'boost/libs/python/src/import.cpp',
	    'boost/libs/python/src/exec.cpp',
	    'boost/libs/python/src/object/function_doc_signature.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_PYTHON_SOURCE',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    ])
	
	
	my_module.add_path([
	    '/usr/include/python3.6m',
	    ], type='c++')
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    ])
	return True


