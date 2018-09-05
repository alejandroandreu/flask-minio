"""
Flask-Minio
-------------

Adds Minio support to your Flask application
"""
from setuptools import setup


setup(
    name='Flask-Minio',
    version='0.1',
    url='https://github.com/alejandroandreu/flask-minio',
    license='BSD',
    author='Alejandro Andreu',
    author_email='contact@alejandroandr.eu',
    description='Adds Minio support to your Flask application',
    long_description=__doc__,
    py_modules=['flask_minio'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
        'minio'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
