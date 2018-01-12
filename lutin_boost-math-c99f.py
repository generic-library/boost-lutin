#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-c99f library"

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
	    'boost/libs/math/build/../src/tr1/acoshf.cpp',
	    'boost/libs/math/build/../src/tr1/asinhf.cpp',
	    'boost/libs/math/build/../src/tr1/atanhf.cpp',
	    'boost/libs/math/build/../src/tr1/cbrtf.cpp',
	    'boost/libs/math/build/../src/tr1/copysignf.cpp',
	    'boost/libs/math/build/../src/tr1/erfcf.cpp',
	    'boost/libs/math/build/../src/tr1/erff.cpp',
	    'boost/libs/math/build/../src/tr1/expm1f.cpp',
	    'boost/libs/math/build/../src/tr1/fmaxf.cpp',
	    'boost/libs/math/build/../src/tr1/fminf.cpp',
	    'boost/libs/math/build/../src/tr1/fpclassifyf.cpp',
	    'boost/libs/math/build/../src/tr1/hypotf.cpp',
	    'boost/libs/math/build/../src/tr1/lgammaf.cpp',
	    'boost/libs/math/build/../src/tr1/llroundf.cpp',
	    'boost/libs/math/build/../src/tr1/log1pf.cpp',
	    'boost/libs/math/build/../src/tr1/lroundf.cpp',
	    'boost/libs/math/build/../src/tr1/nextafterf.cpp',
	    'boost/libs/math/build/../src/tr1/nexttowardf.cpp',
	    'boost/libs/math/build/../src/tr1/roundf.cpp',
	    'boost/libs/math/build/../src/tr1/tgammaf.cpp',
	    'boost/libs/math/build/../src/tr1/truncf.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DBOOST_BUILD_PCH_ENABLED',
	    '-DBOOST_MATH_TR1_DYN_LINK=1',
	    '-DNDEBUG',
	    ])
	
	
	my_module.add_flag('c', [
	    '-finline-functions',
	    '-Wno-inline',
	    '-Wall',
	    '-fvisibility=hidden',
	    '-Winvalid-pch',
	    ])
	
	
	my_module.add_path([
	    'boost/libs/math/src/tr1',
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


