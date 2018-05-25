# -*- coding: utf-8 -*-
"""`sphinx_ustack_theme` lives on `Github`_.

.. _github: https://github.com/unitedstack/sphinx_rtd_theme

"""
from io import open
from setuptools import setup
from sphinx_ustack_theme import __version__


setup(
    name='sphinx_ustack_theme',
    version=__version__,
    url='https://github.com/unitedstack/sphinx_rtd_theme',
    license='MIT',
    author='Yin Yang',
    author_email='yybnbn@126.com',
    description='Read the Docs theme for Sphinx',
    long_description=open('README.rst', encoding='utf-8').read(),
    zip_safe=False,
    packages=['sphinx_ustack_theme'],
    package_data={'sphinx_ustack_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/font/*.*'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'sphinx_ustack_theme = sphinx_ustack_theme',
        ]
    },
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
