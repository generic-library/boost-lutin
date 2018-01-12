#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-c99l library"

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
	    'boost/libs/math/build/../src/tr1/acoshl.cpp',
	    'boost/libs/math/build/../src/tr1/asinhl.cpp',
	    'boost/libs/math/build/../src/tr1/atanhl.cpp',
	    'boost/libs/math/build/../src/tr1/cbrtl.cpp',
	    'boost/libs/math/build/../src/tr1/copysignl.cpp',
	    'boost/libs/math/build/../src/tr1/erfcl.cpp',
	    'boost/libs/math/build/../src/tr1/erfl.cpp',
	    'boost/libs/math/build/../src/tr1/expm1l.cpp',
	    'boost/libs/math/build/../src/tr1/fmaxl.cpp',
	    'boost/libs/math/build/../src/tr1/fminl.cpp',
	    'boost/libs/math/build/../src/tr1/fpclassifyl.cpp',
	    'boost/libs/math/build/../src/tr1/hypotl.cpp',
	    'boost/libs/math/build/../src/tr1/lgammal.cpp',
	    'boost/libs/math/build/../src/tr1/llroundl.cpp',
	    'boost/libs/math/build/../src/tr1/log1pl.cpp',
	    'boost/libs/math/build/../src/tr1/lroundl.cpp',
	    'boost/libs/math/build/../src/tr1/nextafterl.cpp',
	    'boost/libs/math/build/../src/tr1/nexttowardl.cpp',
	    'boost/libs/math/build/../src/tr1/roundl.cpp',
	    'boost/libs/math/build/../src/tr1/tgammal.cpp',
	    'boost/libs/math/build/../src/tr1/truncl.cpp',
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


