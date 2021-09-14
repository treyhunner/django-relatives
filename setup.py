from pathlib import Path
from setuptools import setup, find_packages
import relatives


setup(
    name="django-relatives",
    version=relatives.__version__,
    author="Trey Hunner",
    author_email="trey@treyhunner.com",
    url="https://github.com/treyhunner/django-relatives",
    description="Utilities for linking to related objects in Django admin",
    long_description='\n\n'.join((
        Path('README.rst').read_text(),
        Path('CHANGES.rst').read_text(),
    )),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.11'],
    tests_require=['Django >= 1.11'],
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Framework :: Django',
    ],
)
