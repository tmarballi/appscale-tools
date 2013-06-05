#!/usr/bin/env python
# Programmer: Chris Bunch (chris@appscale.com)
""" version_helper defines methods that can be used to check underlying
assumptions we make about the platform we're running on.

Currently it only has a single method, used to make sure that the version of
Python we're running on is new enough to support the syntax used by the
AppScale Tools.
"""


# First-party Python libraries
import sys


# Third-party Python libraries
import termcolor


def ensure_valid_python_is_used(system=sys):
  """ Makes sure that we are running a version of Python that the AppScale
  Tools supports.

  We use this check to ensure that if a user is running the AppScale Tools with
  Python 2.5 or older, then we can give them a more useful error message than
  the inevitable syntax errors that occur on lines like 'except Exception as e',
  which aren't Python 2.5-friendly.

  Args:
    system: A reference to the sys module. We add this in as an argument to make
      it easy to mock out (as mocking out it or hasattr and tuple purely with
      flexmock is difficult).
  Raises:
    SystemExit: If the version of Python that is running the AppScale Tools is
      older than 2.6.
  """
  if not hasattr(system, 'version_info'):
    termcolor.cprint("Very old versions of Python are not supported. Please "
      "use version 2.6 or newer.\n", "red")
    sys.exit(1)

  version_tuple = tuple(system.version_info[:2])
  if version_tuple < (2, 6):
    termcolor.cprint("Error: Python %d.%d is not supported. Please use "
      "version 2.6 or newer.\n" % version_tuple, "red")
    sys.exit(1)
