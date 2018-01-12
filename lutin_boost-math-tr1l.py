#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-tr1l library"

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
	    'boost/libs/math/config/has_long_double_support.cpp',
	    'boost/libs/math/build/../src/tr1/assoc_laguerrel.cpp',
	    'boost/libs/math/build/../src/tr1/assoc_legendrel.cpp',
	    'boost/libs/math/build/../src/tr1/betal.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_1l.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_2l.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_3l.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_il.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_jl.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_kl.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_neumannl.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_1l.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_2l.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_3l.cpp',
	    'boost/libs/math/build/../src/tr1/expintl.cpp',
	    'boost/libs/math/build/../src/tr1/hermitel.cpp',
	    'boost/libs/math/build/../src/tr1/laguerrel.cpp',
	    'boost/libs/math/build/../src/tr1/legendrel.cpp',
	    'boost/libs/math/build/../src/tr1/riemann_zetal.cpp',
	    'boost/libs/math/build/../src/tr1/sph_bessell.cpp',
	    'boost/libs/math/build/../src/tr1/sph_legendrel.cpp',
	    'boost/libs/math/build/../src/tr1/sph_neumannl.cpp',
	    ])
	
	my_module.add_flag('c++', [
	    '-DBOOST_ALL_NO_LIB=1',
	    '-DNDEBUG',
	    '-DBOOST_BUILD_PCH_ENABLED',
	    '-DBOOST_MATH_TR1_DYN_LINK=1',
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


