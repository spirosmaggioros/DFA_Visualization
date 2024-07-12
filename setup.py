from setuptools import setup, find_packages
import codecs 
import os

VERSION = '1.0.3'
DESCRIPTION = 'A basic DFA/NFA visualization tool only for homework purposes'

setup(
    name="DFA-visual-demo",
    version=VERSION,
    author="Spiros Maggioros",
    author_email="<spirosmag@ieee.org>",
    description=DESCRIPTION,
    packages=find_packages()
)
