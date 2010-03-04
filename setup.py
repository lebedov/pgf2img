#!/usr/bin/env python

from distutils.core import setup

NAME = 'pgf2img'
VERSION = str(0.01)
AUTHOR = 'Lev Givon'
AUTHOR_EMAIL = 'lev@columbia.edu'
URL = 'http://www.columbia.edu/~lev'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
DESCRIPTION = 'PGF/TiKZ to image conversion script'
LICENSE = 'BSD'
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering',
    'Topic :: Text Processing :: Markup :: LaTeX']
SCRIPTS = ['pgf2img']

setup(name = NAME,
      version = VERSION,
      author = AUTHOR,
      author_email = AUTHOR_EMAIL,
      url = URL,
      maintainer = MAINTAINER,
      maintainer_email = MAINTAINER_EMAIL,
      description = DESCRIPTION,
      license = LICENSE,
      classifiers = CLASSIFIERS,
      scripts = SCRIPTS)
