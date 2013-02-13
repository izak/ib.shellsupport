from setuptools import setup, find_packages

version = '0.1'

setup(
    name='ib.shellsupport',
    version=version,
    description="Python library for writing shell-like scripts in python",
    long_description=open("README.txt").read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='python shell script',
    author='Izak Burger',
    author_email='isburger@gmail.com',
    url='https://github.com/izak/ib.shellsupport',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ib'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    )
