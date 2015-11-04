import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = 'Thumbor mongodb storage adapters'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="tc_mongodb",
    version="5.1.0",
    author="Thumbor Community",
    description=("Thumbor thumbor storage adapters"),
    license="MIT",
    keywords="thumbor mongodb mongo",
    url="https://github.com/thumbor-community/mongodb",
    packages=[
        'tc_mongodb',
        'tc_mongodb.storages',
        'tc_mongodb.result_storages'
    ],
    long_description=long_description,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'thumbor>=5.0.0',
        'pymongo'
    ]
)
