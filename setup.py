from distutils.core import setup
import PyTablePrinter

VERSION = PyTablePrinter.version

setup(
    name = 'PyTablePrinter',
    packages = [
        'PyTablePrinter'
    ],
    version = VERSION,
    description = 'A Python library for generating markdown tables',
    author = 'Jordan Matelsky',
    author_email = 'j6k4m8@gmail.com',
    url = 'https://github.com/j6k4m8/PyTablePrinter',
    download_url = 'https://github.com/j6k4m8/PyTablePrinter/tarball/' + VERSION,
    keywords = [
        'markdown',
        'table'
    ],
    classifiers = [],
)
