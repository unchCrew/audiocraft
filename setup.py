# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from pathlib import Path
import setuptools  # Explicit import for clarity

NAME = 'audiocraft'
DESCRIPTION = 'Audio generation research library for PyTorch'
URL = 'https://github.com/facebookresearch/audiocraft'
AUTHOR = 'FAIR Speech & Audio'
EMAIL = 'defossez@meta.com, jadecopet@meta.com'
REQUIRES_PYTHON = '>=3.8.0,<=3.11'  # Explicitly include 3.11

# Extract version from audiocraft/__init__.py
HERE = Path(__file__).parent
try:
    with open(HERE / 'audiocraft' / '__init__.py', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if '__version__' in line:
                context = {}
                exec(line, context)
                VERSION = context['__version__']
                break
        else:
            raise ValueError("Version not found in __init__.py")
except FileNotFoundError:
    raise FileNotFoundError("Could not find audiocraft/__init__.py")

# Read README.md for long description
try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Read requirements from requirements.txt
try:
    with open(HERE / 'requirements.txt', encoding='utf-8') as f:
        REQUIRED = [line.strip() for line in f if line.strip() and not line.startswith('#')]
except FileNotFoundError:
    REQUIRED = []

setuptools.setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email=EMAIL,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    url=URL,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIRED,
    extras_require={
        'dev': ['coverage', 'flake8', 'mypy', 'pdoc3', 'pytest'],
        'wm': ['audioseal'],
    },
    packages=setuptools.find_packages(include=['audiocraft', 'audiocraft.*']),
    package_data={'audiocraft': ['py.typed']},
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',  # Explicitly list Python 3.11
    ],
)
