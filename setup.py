# -*- coding: utf-8 -*-
import os.path
from distutils.core import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='django-db-prefix',
    version='1.0',
    keywords='django database',
    author=u'Ben Slavin <benjamin.slavin@gmail.com>, Denilson Sá <denilsonsa@gmail.com>',
    packages=['django_db_prefix'],
    url='https://github.com/denilsonsa/django-db-prefix',
    license='BSD licence, see LICENCE',
    description='Allow specification of a global, per-app or per-model database table name prefix.',
    long_description=read('README.md'),
    requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
    ]
)
