# Try to not clobber ispyb-api
# https://stackoverflow.com/questions/8936884/python-import-path-packages-with-the-same-name-in-different-folders

from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
