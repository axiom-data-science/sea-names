#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

test_requirements = [
    "pytest>=3"
]

with open("requirements.txt") as f:
    requirements = f.read().strip().split("\n")

setup(
    author="Luke Campbell",
    author_email='luke@axds.co',
    # Uncomment the following section when using git for versions
    # use_scm_version={
    #     "write_to": "python_boilerplate/_version.py",
    #     "write_to_template": '__version__ = "{version}"',
    #     "tag_regex": r"^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$",
    # },
    setup_requires=["setuptools_scm", "setuptools_scm_git_archive"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Determine the sea-name of any arbitrary point or shapely geometry.",
    entry_points={
        'console_scripts': [
            'sea-names=sea_names.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='sea-names',
    name='sea-names',
    packages=find_packages(include=['sea_names', 'sea_names.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='http://github.com/axiom-data-science/sea-names/',
    version='0.4.0',
    zip_safe=False,
)
