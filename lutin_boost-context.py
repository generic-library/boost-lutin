#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-context library"

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
	    'boost/libs/context/src/asm/make_x86_64_sysv_elf_gas.S',
	    'boost/libs/context/src/asm/jump_x86_64_sysv_elf_gas.S',
	    'boost/libs/context/src/asm/ontop_x86_64_sysv_elf_gas.S',
	    'boost/libs/context/src/posix/stack_traits.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CONTEXT_DYN_LINK=1',
	    '-DBOOST_CONTEXT_SOURCE',
	    '-DBOOST_DISABLE_ASSERTS',
	    '-DNDEBUG',
	    ])
	
	my_module.add_flag('s', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CONTEXT_DYN_LINK=1',
	    '-DBOOST_CONTEXT_SOURCE',
	    '-DBOOST_DISABLE_ASSERTS',
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


