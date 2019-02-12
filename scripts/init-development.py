#!/usr/bin/env python3

import os
import textwrap

def get_value(value_name):
    if os.environ.get(value_name) == None:
        if os.environ.get("TRAVIS") == "true":
            raise Exception("Cannot read from stdin during Travis-CI build")
        return input(value_name + " environment variable is not set. Enter value manually: ")
    else:
        return os.environ[value_name]

pypi_user_name = get_value("PYPI_USER_NAME")
print("PYPI user name: {0}".format(pypi_user_name))

pypi_test_password = get_value("PYPI_TEST_PASSWORD")

pypirc_name = os.path.expanduser("~/.pypirc")
if os.path.isfile(pypirc_name):
    print("WARNING: will overwrite existing {0}".format(pypirc_name))
with open(pypirc_name, "w") as f:
    f.write(textwrap.dedent(f"""\
        [distutils]
        index-servers =
          pypi
          pypitest

        [pypi]
        username={pypi_user_name}
        password=asdf

        [pypitest]
        repository: https://test.pypi.org/legacy/
        username={pypi_user_name}
        password={pypi_test_password}
    """))
