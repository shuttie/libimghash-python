#!/usr/bin/env python

from distutils.core import setup, Extension

imghash_module = Extension('_imghash',
		    define_macros = [('MAGICKCORE_QUANTUM_DEPTH','8'),('MAGICKCORE_HDRI_ENABLE','0')],
		    include_dirs = ['include','/usr/include/ImageMagick', '/usr/include/ImageMagick-6', '/usr/include/imghash'],
		    libraries = ['imghash'],
                    sources = ['imghash_wrap.cpp'])

setup(name='imghash',
      version='0.1.4',
      description='Image hashing library python bindings',
      author='Roman Grebennikov',
      author_email='grebennikov.roman@gmail.com',
      url='https://github.com/shuttie/libimghash',
      ext_modules=[imghash_module],
      py_modules=['imghash'],
     )
