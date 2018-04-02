from setuptools import find_packages, setup

with open("README.org") as readme_file:
    readme = readme_file.read()

setup(
    name="orgmod",
    version="0.1.0",
    description="Import modules written in org files",
    long_description=readme,
    author="Abhinav Tushar",
    author_email="lepisma@fastmail.com",
    url="https://github.com/lepisma/orgmod",
    install_requires=[],
    packages=find_packages(),
    classifiers=(
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only"
))
