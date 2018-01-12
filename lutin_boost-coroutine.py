#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-coroutine library"

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
	    'boost/libs/coroutine/src/detail/coroutine_context.cpp',
	    'boost/libs/coroutine/src/exceptions.cpp',
	    'boost/libs/coroutine/src/posix/stack_traits.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CHRONO_DYN_LINK=1',
	    '-DBOOST_CONTEXT_DYN_LINK=1',
	    '-DBOOST_COROUTINES_DYN_LINK=1',
	    '-DBOOST_COROUTINES_SOURCE',
	    '-DBOOST_DISABLE_ASSERTS',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_NO_DEPRECATED',
	    '-DBOOST_THREAD_BUILD_DLL=1',
	    '-DBOOST_THREAD_POSIX',
	    '-DBOOST_THREAD_USE_DLL=1',
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
	    'boost-chrono',
	    'boost-context',
	    'boost-thread',
	    'boost-system',
	    ])
	return True


