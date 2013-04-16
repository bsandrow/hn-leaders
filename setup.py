from __future__ import print_function

try:
    from setuptools import setup
except ImportError:
    print("Falling back to distutils. Functionality may be limited.")
    from distutils.core import setup

requires = []
long_description = open('README.md').read()

config = {
    'name'            : 'hn-leaders',
    'description'     : 'A script to archive a copy of the HackerNews leaders list.',
    'long_description': long_description,
    'author'          : 'Brandon Sandrowicz',
    'author_email'    : 'brandon@sandrowicz.org',
    'url'             : 'https://github.com/bsandrow/hn-leaders',
    'version'         : '0.1',
    'packages'        : [''],
    'package_data'    : { '': ['LICENSE'] },
    'scripts'         : 'hn-leaders',
    'install_requires': requires,
    'license'         : open('LICENSE').read(),
    'test_suite'      : '',
    'classifiers'     : (,
    ),
}

setup(**config)
