# setup.py
from setuptools import setup, find_packages

setup(
    name='py-fun',
    version='0.1.0',
    description='Python Project Assignment: Calculator with factorization.',
    author='Shoaib Khan', # Replace with your name
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        # Add any dependencies here, although they should be in requirements.txt
    ],
)