#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-wave library"

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
	    'boost/libs/wave/src/instantiate_cpp_exprgrammar.cpp',
	    'boost/libs/wave/src/instantiate_cpp_grammar.cpp',
	    'boost/libs/wave/src/instantiate_cpp_literalgrs.cpp',
	    'boost/libs/wave/src/instantiate_defined_grammar.cpp',
	    'boost/libs/wave/src/instantiate_predef_macros.cpp',
	    'boost/libs/wave/src/instantiate_re2c_lexer.cpp',
	    'boost/libs/wave/src/instantiate_re2c_lexer_str.cpp',
	    'boost/libs/wave/src/token_ids.cpp',
	    'boost/libs/wave/src/wave_config_constant.cpp',
	    'boost/libs/wave/src/cpplexer/re2clex/aq.cpp',
	    'boost/libs/wave/src/cpplexer/re2clex/cpp_re.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_DYN_LINK=1',
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-w',
	    ])
	
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    'boost-filesystem',
	    'boost-thread',
	    'boost-date-time',
	    'boost-chrono',
	    'boost-system',
	    ])
	return True


