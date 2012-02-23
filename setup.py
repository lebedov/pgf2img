#!/usr/bin/env python
 
import os
import subprocess

import distutils.command.build 
import distutils.command.clean
from distutils.core import Command, setup

man_file = 'pgf2img.1'
man_src = 'pgf2img.rst'

class build(distutils.command.build.build):
    def run(self):
        distutils.command.build.build.run(self)
        p = subprocess.Popen('rst2man ' + man_src + ' ' + man_file, shell=True)
        returncode = p.wait()
        if returncode != 0:
            raise RuntimeError('docutils required to build man file')
        
class clean(distutils.command.clean.clean):
    def run(self):
        distutils.command.clean.clean.run(self)
        if os.path.isfile(man_file):
            os.unlink(man_file)
                                
NAME = 'pgf2img'
VERSION = str(0.011)
AUTHOR = 'Lev Givon'
AUTHOR_EMAIL = 'lev@columbia.edu'
URL = 'http://www.columbia.edu/~lev'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
DESCRIPTION = 'PGF/TikZ to image conversion script'
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
MODULES = ['pgf2img']
DATA_FILES = [('man/man1', [man_file])]
CMDCLASS = {'build': build,
            'clean': clean}

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
      scripts = SCRIPTS,
      py_modules = MODULES,
      data_files = DATA_FILES,
      cmdclass = CMDCLASS)
