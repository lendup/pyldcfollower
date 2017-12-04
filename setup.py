from os import path

from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


def get_install_requires():
    requires = []
    with open('requirements.txt', 'r') as fid:
        for ln in fid:
            ln = ln.strip()

            if len(ln) != 0 and ln[0] != '#':
                requires.append(ln)

        return requires


setup(
    name='pyldcfollower',
    version='0.0.2',

    author='Yang Zhang',
    author_email='yang.zhang@lendup.com',

    description="Provide connection to LDC follower database.",
    keywords="LDC follower database",
    package_dir={'': 'ldcfollower'},
    packages=find_packages('src/lib/'),

    install_requires=['psycopg2'],
)
