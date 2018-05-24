from setuptools import setup
from setuptools import find_packages

setup(
    name='hallo-web',
    version='0.1.0',
    author='Guido Barbaglia',
    author_email='guido.barbaglia@gmail.com',
    packages=find_packages(),
    license='LICENSE',
    long_description=open('README.md').read(),
    description='Hallo Web app with Flask',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=[
        'pytest>=3.0',
        'pytest-pep8',
        'pytest-sugar',
        'pytest-cov',
        'pytest-runner'
    ],
    url='https://github.com/Kalimaha/hallo-web/'
)
