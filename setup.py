"""
Flask-Minio
-------------

Adds Minio support to your Flask application
"""
from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='Flask-Minio',
    version='0.1.2',
    url='https://github.com/alejandroandreu/flask-minio',
    license='BSD',
    author='Alejandro Andreu',
    author_email='contact@alejandroandr.eu',
    description='Adds Minio support to your Flask application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'minio'
    ],
    tests_require=[
        'pytest>=3.8.1',
        'Flask',
        'minio'
    ],
    setup_requires=[
        'pytest-runner>=4.2'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
