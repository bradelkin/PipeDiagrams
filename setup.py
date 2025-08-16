from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='PipeDiagrams',
   version='1.0',
   description='Make PipeDream diagrams',
   license="GPL 3.0",
   long_description=long_description,
   author='Brad Elkin',
   author_email='brad.elkin@gmail.com',
   url = "https://github.com/bradelkin/PipeDream",
   packages=['pipedream_diagrams'],
   install_requires=['pillow', ], #external packages as dependencies
   )
