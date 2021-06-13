#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages

requirements = ['numpy', 'tqdm']

setup(name='nfor',
      version=0.1,
      description='Nested For Loops',
      author='Alex Hagen',
      author_email='alexhagen6@gmail.com',
      url='https://github.com/alexhagen/nfor',
      long_description=open('README.md').read(),
      packages=['nfor'],
      install_requires=requirements,
     )
