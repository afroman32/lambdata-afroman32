# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata_afroman", # the name that you will install via pip
    version="1.0.1",
    author="Makoa Noble",
    author_email="makoa-noble@lambdastudents.com",
    description="A package for basic things",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/afroman32/lambdata-afroman32",
    #keywords="",
    packages= find_packages()
)