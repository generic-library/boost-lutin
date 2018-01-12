#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-locale library"

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
	    'boost/libs/locale/src/encoding/codepage.cpp',
	    'boost/libs/locale/src/shared/date_time.cpp',
	    'boost/libs/locale/src/shared/format.cpp',
	    'boost/libs/locale/src/shared/formatting.cpp',
	    'boost/libs/locale/src/shared/generator.cpp',
	    'boost/libs/locale/src/shared/ids.cpp',
	    'boost/libs/locale/src/shared/localization_backend.cpp',
	    'boost/libs/locale/src/shared/message.cpp',
	    'boost/libs/locale/src/shared/mo_lambda.cpp',
	    'boost/libs/locale/src/util/codecvt_converter.cpp',
	    'boost/libs/locale/src/util/default_locale.cpp',
	    'boost/libs/locale/src/util/info.cpp',
	    'boost/libs/locale/src/util/locale_data.cpp',
	    'boost/libs/locale/src/icu/boundary.cpp',
	    'boost/libs/locale/src/icu/codecvt.cpp',
	    'boost/libs/locale/src/icu/collator.cpp',
	    'boost/libs/locale/src/icu/conversion.cpp',
	    'boost/libs/locale/src/icu/date_time.cpp',
	    'boost/libs/locale/src/icu/formatter.cpp',
	    'boost/libs/locale/src/icu/icu_backend.cpp',
	    'boost/libs/locale/src/icu/numeric.cpp',
	    'boost/libs/locale/src/icu/time_zone.cpp',
	    'boost/libs/locale/src/posix/codecvt.cpp',
	    'boost/libs/locale/src/posix/collate.cpp',
	    'boost/libs/locale/src/posix/converter.cpp',
	    'boost/libs/locale/src/posix/numeric.cpp',
	    'boost/libs/locale/src/posix/posix_backend.cpp',
	    'boost/libs/locale/src/std/codecvt.cpp',
	    'boost/libs/locale/src/std/collate.cpp',
	    'boost/libs/locale/src/std/converter.cpp',
	    'boost/libs/locale/src/std/numeric.cpp',
	    'boost/libs/locale/src/std/std_backend.cpp',
	    'boost/libs/locale/src/util/gregorian.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_CHRONO_DYN_LINK=1',
	    '-DBOOST_LOCALE_DYN_LINK=1',
	    '-DBOOST_LOCALE_NO_WINAPI_BACKEND=1',
	    '-DBOOST_LOCALE_WITH_ICONV=1',
	    '-DBOOST_LOCALE_WITH_ICU=1',
	    '-DBOOST_SYSTEM_DYN_LINK=1',
	    '-DBOOST_SYSTEM_NO_DEPRECATED',
	    '-DBOOST_THREAD_BUILD_DLL=1',
	    '-DBOOST_THREAD_NO_LIB=1',
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
	    'boost-thread',
	    'boost-system',
	    ])
	return True


