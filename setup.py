from setuptools import setup, find_packages

setup(
    name='zoetrope',
    version='0.1',
    description='A templating tool that creates unit tests from an arbitrary file.',
    packages=find_packages(),
    scripts=['zoetrope/zoetrope'],
    install_requires=[
        'mock'
    ]
)
