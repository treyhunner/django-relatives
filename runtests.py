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
        MIDDLEWARE=[
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
        ],
        ROOT_URLCONF='relatives.tests.urls',
        STATIC_URL='/static/',
        TEMPLATES=[
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'APP_DIRS': True,
                'OPTIONS': {
                    "context_processors": [
                        'django.contrib.auth.context_processors.auth'
                    ]
                }
            },
        ],
    )


def runtests():
    if hasattr(django, 'setup'):
        django.setup()
    try:
        from django.test.runner import DiscoverRunner
        runner_class = DiscoverRunner
        test_args = ['relatives.tests']
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner
        runner_class = DjangoTestSuiteRunner
        test_args = ['tests']
    failures = runner_class(failfast=False).run_tests(test_args)
    sys.exit(failures)


if __name__ == "__main__":
    runtests(*sys.argv[1:])
