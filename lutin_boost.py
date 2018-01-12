#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools
import os

def get_type():
	return "LIBRARY"

def get_desc():
	return "boost include library"

#def get_licence():
#	return "UNKNOW"

def get_compagny_type():
	return "org"

def get_compagny_name():
	return "boost"

def get_version():
	return "version.txt"

def configure(target, my_module):
	my_module.compile_version('c++', 2011)
	my_module.add_depend([
	    'boost-include',
	    'boost-atomic',
	    'boost-system',
	    'boost-chrono',
	    'boost-container',
	    'boost-context',
	    'boost-thread',
	    'boost-coroutine',
	    'boost-date-time',
	    'boost-filesystem',
	    'boost-fiber',
	    'boost-regex',
	    'boost-graph',
	    'boost-iostreams',
	    'boost-locale',
	    'boost-log',
	    'boost-log-setup',
	    'boost-math-tr1',
	    'boost-math-tr1f',
	    'boost-math-tr1l',
	    'boost-math-c99',
	    'boost-math-c99f',
	    'boost-math-c99l',
	    'boost-program-options',
	    'boost-python3',
	    'boost-random',
	    'boost-serialization',
	    'boost-wserialization',
	    'boost-signals',
	    'boost-stacktrace-noop',
	    'boost-stacktrace-addr2line',
	    'boost-stacktrace-basic',
	    'boost-timer',
	    'boost-prg-exec-monitor',
	    'boost-unit-test-framework',
	    'boost-type-erasure',
	    'boost-wave',
	    ])


