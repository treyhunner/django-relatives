#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import django
from django.conf import settings


sys.path.insert(0, abspath(dirname(__file__)))


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.auth',
            'relatives',
            'relatives.tests',
            'django.contrib.admin',
        ),
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        ROOT_URLCONF='relatives.tests.urls',
        STATIC_URL='/static/',
    )


def runtests(*test_args):
    if hasattr(django, 'setup'):
        django.setup()
    if not test_args:
        test_args = ['tests']
    from django.test.simple import DjangoTestSuiteRunner
    failures = DjangoTestSuiteRunner(failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
