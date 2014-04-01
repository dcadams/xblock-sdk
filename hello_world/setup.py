"""Setup for hello_world XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='hello_world-xblock',
    version='0.1',
    description='hello_world XBlock',   # TODO: write a better description.
    packages=[
        'hello_world',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'hello_world = hello_world:HelloWorldXBlock',
        ]
    },
    package_data=package_data("hello_world", "static"),
)