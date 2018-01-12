#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-tr1f library"

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
	    'boost/libs/math/build/../src/tr1/assoc_laguerref.cpp',
	    'boost/libs/math/build/../src/tr1/assoc_legendref.cpp',
	    'boost/libs/math/build/../src/tr1/betaf.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_1f.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_2f.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_3f.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_if.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_jf.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_kf.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_neumannf.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_1f.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_2f.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_3f.cpp',
	    'boost/libs/math/build/../src/tr1/expintf.cpp',
	    'boost/libs/math/build/../src/tr1/hermitef.cpp',
	    'boost/libs/math/build/../src/tr1/laguerref.cpp',
	    'boost/libs/math/build/../src/tr1/legendref.cpp',
	    'boost/libs/math/build/../src/tr1/riemann_zetaf.cpp',
	    'boost/libs/math/build/../src/tr1/sph_besself.cpp',
	    'boost/libs/math/build/../src/tr1/sph_legendref.cpp',
	    'boost/libs/math/build/../src/tr1/sph_neumannf.cpp',
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


