from setuptools import setup
import os

kws = {}

setup(name='pygarrayimage',
      description="Allow numpy arrays as source of texture data for pyglet.",
      long_description = \
"""pygarrayimage allows display of Python objects supporting the array
interface as OpenGL textures without a copy. The OpenGL texture
handling is done using pyglet.

In other words, this allows fast transfer of data from numpy arrays
(or any other data source supporting the array interface) to the video
card.

TODO: support the buffer interface added with Python 2.6/3.0 rather
than the numpy-defined array interface.

""",
      version='1.1', # keep in sync with pygarrayimage/arrayimage.py
      author='Andrew Straw',
      author_email='strawman@astraw.com',
      url='http://code.astraw.com/projects/motmot/wiki/pygarrayimage',
      license='BSD',
      packages=['pygarrayimage'],
      **kws)
