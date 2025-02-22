#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
from plans import __version__ as VERSION

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='django-plans',
    version=VERSION,
    description='Pluggable django app for managing pricing plans with quotas and accounts expiration',
    long_description=long_description,
    author='Krzysztof Dorosz',
    author_email='cypreess@gmail.com',
    url='https://github.com/cypreess/django-plans',
    license='MIT',

    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        # 'https://github.com/SmileyChris/django-countries/archive/master.zip#egg=django_countries',  # django-countries hack
        # 'django-countries>=4.5',
        'pytz>=2017.2',
        'django-ordered-model>=1.4.1',
        ' vatnumber3>=1.1.2',
        'celery',
        'suds-community>=1.1.2',
        'six',
    ],
    extras_require={
        'i18n': [
            'django-modeltranslation>=0.5b1',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
