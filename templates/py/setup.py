import os
from setuptools import setup


def read(fp: str) -> str:
    return open(os.path.join(os.path.dirname(__file__), fp)).read()


setup(
    name="template project",
    version="0.0.1dev",
    author="Cameron King",
    author_email="cam@ckingdev.io",
    description=(""),
    license="MIT",
    packages=[""],
    long_description=read("README.md"),
)
