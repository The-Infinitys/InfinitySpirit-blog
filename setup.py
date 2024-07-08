from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0'
DESCRIPTION = 'An Simple and useful Static Site Generator for markdown, html, css, and javascript. '
LONG_DESCRIPTION = DESCRIPTION

# Setting up
setup(
    name="infinityspirit",
    version=VERSION,
    author="The Infinity's",
    author_email="the.infinitys.infinity@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('readme.md').read(),
    packages=find_packages(),
    install_requires=["markdown","pygments"],
    keywords=["the infinity's","the_infinitys","the-infinitys","markdown","static","site","generator","ssg"],
    url='https://github.com/The-Infinitys/InfinitySpirit',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
