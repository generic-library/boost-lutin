#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-c99 library"

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
	    'boost/libs/math/build/../src/tr1/acosh.cpp',
	    'boost/libs/math/build/../src/tr1/asinh.cpp',
	    'boost/libs/math/build/../src/tr1/atanh.cpp',
	    'boost/libs/math/build/../src/tr1/cbrt.cpp',
	    'boost/libs/math/build/../src/tr1/copysign.cpp',
	    'boost/libs/math/build/../src/tr1/erfc.cpp',
	    'boost/libs/math/build/../src/tr1/erf.cpp',
	    'boost/libs/math/build/../src/tr1/expm1.cpp',
	    'boost/libs/math/build/../src/tr1/fmax.cpp',
	    'boost/libs/math/build/../src/tr1/fmin.cpp',
	    'boost/libs/math/build/../src/tr1/fpclassify.cpp',
	    'boost/libs/math/build/../src/tr1/hypot.cpp',
	    'boost/libs/math/build/../src/tr1/lgamma.cpp',
	    'boost/libs/math/build/../src/tr1/llround.cpp',
	    'boost/libs/math/build/../src/tr1/log1p.cpp',
	    'boost/libs/math/build/../src/tr1/lround.cpp',
	    'boost/libs/math/build/../src/tr1/nextafter.cpp',
	    'boost/libs/math/build/../src/tr1/nexttoward.cpp',
	    'boost/libs/math/build/../src/tr1/round.cpp',
	    'boost/libs/math/build/../src/tr1/tgamma.cpp',
	    'boost/libs/math/build/../src/tr1/trunc.cpp',
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


