#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost:boost-math-tr1 library"

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
	    'boost/libs/math/build/../src/tr1/assoc_laguerre.cpp',
	    'boost/libs/math/build/../src/tr1/assoc_legendre.cpp',
	    'boost/libs/math/build/../src/tr1/beta.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_1.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_2.cpp',
	    'boost/libs/math/build/../src/tr1/comp_ellint_3.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_i.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_j.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_bessel_k.cpp',
	    'boost/libs/math/build/../src/tr1/cyl_neumann.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_1.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_2.cpp',
	    'boost/libs/math/build/../src/tr1/ellint_3.cpp',
	    'boost/libs/math/build/../src/tr1/expint.cpp',
	    'boost/libs/math/build/../src/tr1/hermite.cpp',
	    'boost/libs/math/build/../src/tr1/laguerre.cpp',
	    'boost/libs/math/build/../src/tr1/legendre.cpp',
	    'boost/libs/math/build/../src/tr1/riemann_zeta.cpp',
	    'boost/libs/math/build/../src/tr1/sph_bessel.cpp',
	    'boost/libs/math/build/../src/tr1/sph_legendre.cpp',
	    'boost/libs/math/build/../src/tr1/sph_neumann.cpp',
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


