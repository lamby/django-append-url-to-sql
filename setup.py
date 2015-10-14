#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-append-url-to-sql',
    description="Appends the request URL to SQL statements in Django.",
    version='1.0.1',
    url='https://chris-lamb.co.uk/projects/django-append-url-to-sql',

    author='Chris Lamb',
    author_email='chris@chris-lamb.co.uk',
    license='BSD',

    packages=find_packages(),
)
