"""
    Project: Pana (https://github.com/azazelm3dj3d/pana)
    Author: azazelm3dj3d (https://github.com/azazelm3dj3d)
    License: BSD 2-Clause
"""

import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "pana",
    version = "0.1.0",
    author = "azazelm3dj3d",
    description = "Pana is a CLI and module built to check if a package name or username is available from common package managers.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/azazelm3dj3d/pana",
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
