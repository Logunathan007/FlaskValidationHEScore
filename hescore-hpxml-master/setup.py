from setuptools import setup
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hescore-hpxml',
    version='2023.05.0',
    description='HPXML Translator for the HEScore API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NREL/hescore-hpxml',
    author='Noel Merket (NREL)',
    author_email='noel.merket@nrel.gov',
    license='BSD-2',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing :: Markup :: XML',
    ],
    keywords='home energy score hescore doe nrel',
    packages=['hescorehpxml'],
    python_requires='>=3.7',
    install_requires=[
        'lxml',
        'jsonschema',
        'flask',
        'flask-cors',
    ],
    extras_require={
        'dev': [
            'flake8',
            'coverage',
            'sphinx',
            'sphinx_rtd_theme',
            'sphinx-autobuild',
            'pytest',
            'pytest-cov',
        ],
        'test': [
            'flake8',
            'coverage',
            'sphinx',
            'sphinx_rtd_theme',
            'sphinx-autobuild',
            'pytest',
            'pytest-cov'
        ]
    },
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'hpxml2hescore=hescorehpxml:main',
            'hescorejsons=hescorehpxml.create_all_example_json:main'
        ]
    }
)
