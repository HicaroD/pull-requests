from setuptools import setup

long_description = None
with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='pull-request',
   version='1.0.0',
   description='A command line interface for creating pull requests',
   long_description=long_description,
   author='Hícaro Dânrlley',
   author_email='hdanrlley1@gmail.com',
   packages=['pull_request'],
   install_requires=['requests'], #external packages as dependencies
   python_requires=">=3.10",
   entry_points={
       "console_scripts": {
           "pr = pull_request.main:main",
       }
    }
)

