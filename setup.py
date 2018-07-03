# -*- encoding: utf-8 -*-
# ! python3

import io

from setuptools import setup

setup(
    name='tf-serving-client',
    version='0.1.0',
    description="""Customised Tensorflow Serving API produced by coffeedjimmy""",
    # long_description=io.open("README.md", 'r', encoding="utf-8").read(),
    url='https://github.com/coffeedjimmy/tf-serving-client.git',
    license='Apache 2.0',
    keywords="TensorFlow Serving API libraries",
    author='Jimmy Woo',
    author_email='coffeedjimmy@gmail.com',
    packages=['tensorflow_serving'],
    install_requires=[
        'grpcio>=1.7.0',
        'numpy>=1.12.0'
    ],
    python_requires='~=3.5',
    include_package_data=True,
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent'
    ]
)