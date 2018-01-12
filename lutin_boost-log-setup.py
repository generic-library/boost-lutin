#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-log-setup library"

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
	    'boost/libs/log/src/setup/parser_utils.cpp',
	    'boost/libs/log/src/setup/init_from_stream.cpp',
	    'boost/libs/log/src/setup/init_from_settings.cpp',
	    'boost/libs/log/src/setup/settings_parser.cpp',
	    'boost/libs/log/src/setup/filter_parser.cpp',
	    'boost/libs/log/src/setup/formatter_parser.cpp',
	    'boost/libs/log/src/setup/default_filter_factory.cpp',
	    'boost/libs/log/src/setup/matches_relation_factory.cpp',
	    'boost/libs/log/src/setup/default_formatter_factory.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_ATOMIC_DYN_LINK=1',
	    '-DBOOST_CHRONO_DYN_LINK=1',
	    '-DBOOST_DATE_TIME_DYN_LINK=1',
	    '-DBOOST_FILESYSTEM_DYN_LINK=1',
	    '-DBOOST_HAS_ICU=1',
	    '-DBOOST_LOG_DYN_LINK=1',
	    '-DBOOST_LOG_HAS_PTHREAD_MUTEX_ROBUST',
	    '-DBOOST_LOG_SETUP_BUILDING_THE_LIB=1',
	    '-DBOOST_LOG_SETUP_DLL',
	    '-DBOOST_LOG_USE_AVX2',
	    '-DBOOST_LOG_USE_NATIVE_SYSLOG',
	    '-DBOOST_LOG_USE_SSSE3',
	    '-DBOOST_LOG_WITHOUT_EVENT_LOG',
	    '-DBOOST_SPIRIT_USE_PHOENIX_V3=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_NO_DEPRECATED',
	    '-DBOOST_THREAD_BUILD_DLL=1',
	    '-DBOOST_THREAD_DONT_USE_CHRONO=1',
	    '-DBOOST_THREAD_POSIX',
	    '-DBOOST_THREAD_USE_DLL=1',
	    '-DDATE_TIME_INLINE',
	    '-DNDEBUG',
	    '-D_XOPEN_SOURCE=600',
	    '-D__STDC_CONSTANT_MACROS',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-fno-strict-aliasing',
	    '-ftemplate-depth-1024',
	    '-fvisibility=hidden',
	    ])
	
	
	my_module.add_path([
	    'boost/libs/log/src',
	    ], type='c++')
	
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'z',
	    'm',
	    'cxx',
	    'boost-include',
	    'pthread',
	    'boost-log',
	    'boost-regex',
	    'boost-filesystem',
	    'boost-date-time',
	    'boost-thread',
	    'boost-chrono',
	    'boost-system',
	    'boost-atomic',
	    ])
	return True


