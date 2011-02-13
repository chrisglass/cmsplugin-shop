import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "cmsplugin-shop",
    version = "0.0.0",
    url = 'http://github.com/chrisglass/cmsplugin-shop',
    license = 'BSD',
    description = "django CMS plugin for django SHOP",
    author = 'Christopher Glass',
    author_email = 'tribaal@gmail.com',
    packages = find_packages(),
    install_requires=[
        'django-cms',
        'django-shop',
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    include_package_data=True,
    zip_safe = False
)

