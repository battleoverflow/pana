"""
    Project: Pana (https://github.com/battleoverflow/pana)
    Author: battleoverflow (https://github.com/battleoverflow)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pana",
    version = "0.2.1",
    author = "battleoverflow",
    description = "Pana is a CLI and module built to check if a package name or username is available from common package managers.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/battleoverflow/pana",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    py_modules=['pana'],
    install_requires=[
        "requests",
        "colorama"
    ],
    scripts=["pana.py"],
    entry_points={
        'console_scripts': ["pana=pana:Pana.main"]
    },
    python_requires = ">=3.6"
)
