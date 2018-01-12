#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-fiber library"

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
	    'boost/libs/fiber/src/numa/linux/pin_thread.cpp',
	    'boost/libs/fiber/src/numa/linux/topology.cpp',
	    'boost/libs/fiber/src/algo/algorithm.cpp',
	    'boost/libs/fiber/src/algo/round_robin.cpp',
	    'boost/libs/fiber/src/algo/shared_work.cpp',
	    'boost/libs/fiber/src/algo/work_stealing.cpp',
	    'boost/libs/fiber/src/algo/numa/work_stealing.cpp',
	    'boost/libs/fiber/src/barrier.cpp',
	    'boost/libs/fiber/src/condition_variable.cpp',
	    'boost/libs/fiber/src/context.cpp',
	    'boost/libs/fiber/src/fiber.cpp',
	    'boost/libs/fiber/src/future.cpp',
	    'boost/libs/fiber/src/mutex.cpp',
	    'boost/libs/fiber/src/properties.cpp',
	    'boost/libs/fiber/src/recursive_mutex.cpp',
	    'boost/libs/fiber/src/recursive_timed_mutex.cpp',
	    'boost/libs/fiber/src/timed_mutex.cpp',
	    'boost/libs/fiber/src/scheduler.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CONTEXT_DYN_LINK=1',
	    '-DBOOST_DISABLE_ASSERTS',
	    '-DBOOST_FIBERS_DYN_LINK=1',
	    '-DBOOST_FIBERS_SOURCE',
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
	    'boost-context',
	    'boost-filesystem',
	    'boost-system',
	    ])
	return True


