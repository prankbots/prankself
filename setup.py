from __future__ import with_statement
import re
##
# Setup.py Koplaxs ??
# DON'T EDIT ??
# Thanks ??
##
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup



setup(
        name='LINETCR',
        packages=['LINETCR'],
        version='0.9.9.9',
        description='May Waifu be with you...',
        license='BSD License',
        author='Koplaxs',
        author_email='zxchidden@gmail.com',
        url='canseethefuture.org',
        keywords=['LINETCR'],
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.1',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Communications :: Chat',
        ],
        install_requires=[
            'requests',
            'curve',
            'rsa',
		'thrift==0.9.3'
        ],
    )
