# coding: utf8
# Part of the bioread package for reading BIOPAC data.
#
# Copyright (c) 2010 Board of Regents of the University of Wisconsin System
#
# Written by John Ollinger <ollinger@wisc.edu> and Nate Vack <njvack@wisc.edu>
# at the Waisman Laboratory for Brain Imaging and Behavior, University of
# Wisconsin-Madison
# Project home: http://github.com/njvack/bioread

from bioread.readers import AcqReader

raise DeprecationWarning("""
***** Outdated bioread version! *****
No need for this version of bioread anymore.

Please use the version from https://github.com/njvack/bioread instead.
It's fast and memory-efficient (tested with 2GB files).
*****
""")

def read_file(filelike, simple_layout=False):
    """
    Read a file (either an IO object or a filename) and return a biopac.
    Datafile object.
    Simply a shorthand for bioread.readers.AcqReader.read_file()
    """
    return AcqReader.read_file(filelike, simple_layout)
