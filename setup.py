import pathlib
from setuptools import setup

version = open('Ctl/VERSION').read().strip()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="vegu-pandax",
    version=version,
    description="Dummy python package used for testing PyPI releases",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/vegu/panda",
    author="vegu",
    author_email="stefan@20c.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["panda"],
    include_package_data=True,
)
