"""
    Battery Data API

    A standard API for accessing battery experiment datasets and metadata  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: martin.robinson@cs.ox.ac.uk
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "batteryclient"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

setup(
    name=NAME,
    version=VERSION,
    description="Battery Data API",
    author="OpenAPI Generator community",
    author_email="martin.robinson@cs.ox.ac.uk",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Battery Data API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="Apache 2.0",
    long_description="""\
    A standard API for accessing battery experiment datasets and metadata  # noqa: E501
    """
)