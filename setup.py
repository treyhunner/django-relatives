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
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.4.2'],
    tests_require=['Django >= 1.4.2'],
    test_suite='runtests.runtests',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Framework :: Django',
    ],
)
