#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'pyne2013', 'local_settings.py')):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyne2013.local_settings")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyne2013.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
