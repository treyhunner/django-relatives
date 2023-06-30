#!/usr/bin/env python
import sys
from os.path import abspath, dirname

import django
from django.conf import settings


sys.path.insert(0, abspath(dirname(__file__)))


if not settings.configured:
    settings.configure(
        INSTALLED_APPS=(
            "django.contrib.contenttypes",
            "django.contrib.sessions",
            "django.contrib.messages",
            "django.contrib.auth",
            "relatives",
            "relatives.tests",
            "django.contrib.admin",
        ),
        DATABASES={
            "default": {
                "NAME": ":memory:",
                "ENGINE": "django.db.backends.sqlite3",
            }
        },
        MIDDLEWARE=[
            "django.contrib.sessions.middleware.SessionMiddleware",
            "django.middleware.common.CommonMiddleware",
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
        ],
        ROOT_URLCONF="relatives.tests.urls",
        SECRET_KEY="secret",
        STATIC_URL="/static/",
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "APP_DIRS": True,
                "OPTIONS": {
                    "context_processors": [
                        "django.template.context_processors.request",
                        "django.contrib.auth.context_processors.auth",
                        "django.contrib.messages.context_processors.messages",
                    ]
                },
            },
        ],
    )


def runtests():
    if hasattr(django, "setup"):
        django.setup()
    try:
        from django.test.runner import DiscoverRunner

        runner_class = DiscoverRunner
        test_args = ["relatives.tests"]
    except ImportError:
        from django.test.simple import DjangoTestSuiteRunner

        runner_class = DjangoTestSuiteRunner
        test_args = ["tests"]
    failures = runner_class(failfast=False).run_tests(test_args)
    sys.exit(failures)


def run_management_command(arguments):
    if hasattr(django, "setup"):
        django.setup()
    from django.core.management import execute_from_command_line

    execute_from_command_line(arguments)


if __name__ == "__main__":
    if sys.argv[1:]:
        run_management_command(sys.argv)
    else:
        runtests()
