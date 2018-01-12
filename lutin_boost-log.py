#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-log library"

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
	    'boost/libs/log/src/attribute_name.cpp',
	    'boost/libs/log/src/attribute_set.cpp',
	    'boost/libs/log/src/attribute_value_set.cpp',
	    'boost/libs/log/src/code_conversion.cpp',
	    'boost/libs/log/src/core.cpp',
	    'boost/libs/log/src/record_ostream.cpp',
	    'boost/libs/log/src/severity_level.cpp',
	    'boost/libs/log/src/global_logger_storage.cpp',
	    'boost/libs/log/src/named_scope.cpp',
	    'boost/libs/log/src/process_name.cpp',
	    'boost/libs/log/src/process_id.cpp',
	    'boost/libs/log/src/thread_id.cpp',
	    'boost/libs/log/src/timer.cpp',
	    'boost/libs/log/src/exceptions.cpp',
	    'boost/libs/log/src/default_attribute_names.cpp',
	    'boost/libs/log/src/default_sink.cpp',
	    'boost/libs/log/src/text_ostream_backend.cpp',
	    'boost/libs/log/src/text_file_backend.cpp',
	    'boost/libs/log/src/text_multifile_backend.cpp',
	    'boost/libs/log/src/thread_specific.cpp',
	    'boost/libs/log/src/once_block.cpp',
	    'boost/libs/log/src/timestamp.cpp',
	    'boost/libs/log/src/threadsafe_queue.cpp',
	    'boost/libs/log/src/event.cpp',
	    'boost/libs/log/src/trivial.cpp',
	    'boost/libs/log/src/spirit_encoding.cpp',
	    'boost/libs/log/src/format_parser.cpp',
	    'boost/libs/log/src/date_time_format_parser.cpp',
	    'boost/libs/log/src/named_scope_format_parser.cpp',
	    'boost/libs/log/src/unhandled_exception_count.cpp',
	    'boost/libs/log/src/permissions.cpp',
	    'boost/libs/log/src/dump.cpp',
	    'boost/libs/log/src/dump_avx2.cpp',
	    'boost/libs/log/src/dump_ssse3.cpp',
	    'boost/libs/log/src/posix/ipc_reliable_message_queue.cpp',
	    'boost/libs/log/src/posix/object_name.cpp',
	    'boost/libs/log/src/syslog_backend.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_ATOMIC_DYN_LINK=1',
	    '-DBOOST_CHRONO_DYN_LINK=1',
	    '-DBOOST_DATE_TIME_DYN_LINK=1',
	    '-DBOOST_FILESYSTEM_DYN_LINK=1',
	    '-DBOOST_HAS_ICU=1',
	    '-DBOOST_LOG_BUILDING_THE_LIB=1',
	    '-DBOOST_LOG_DLL',
	    '-DBOOST_LOG_HAS_PTHREAD_MUTEX_ROBUST',
	    '-DBOOST_LOG_USE_AVX2',
	    '-DBOOST_LOG_USE_NATIVE_SYSLOG',
	    '-DBOOST_LOG_USE_SSSE3',
	    '-DBOOST_LOG_WITHOUT_DEBUG_OUTPUT',
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
	    '-mavx',
	    '-mavx2',
	    '-msse',
	    '-msse2',
	    '-msse3',
	    '-mssse3',
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
	    'boost-atomic',
	    'boost-chrono',
	    'boost-thread',
	    'boost-date-time',
	    'boost-filesystem',
	    'boost-system',
	    'boost-regex',
	    ])
	return True


