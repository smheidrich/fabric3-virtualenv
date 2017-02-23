from setuptools import setup, find_packages


setup(
    name="fabric3-virtualenv",
    version="0.3.1",
    author='Andreas Nüßlein',
    url='https://github.com/nutztherookie/fabric3-virtualenv',
    description=(
        "Some additional functions for working with remote virtualenvs "
        "in Fabric3."
    ),
    long_description=open('README').read(),
    packages=find_packages(),
    install_requires=[
        'Fabric3'
    ]
)
