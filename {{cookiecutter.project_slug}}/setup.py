import os
from setuptools import setup

def get_version():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'workflow', '{{cookiecutter.project_slug}}.VERSION')) as f:
        return f.readline().strip()

CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: {{cookiecutter.license}}",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
 name='{{cookiecutter.project_name}}',
 description="{{cookiecutter.project_description}}",
 version=get_version(),
 author="{{cookiecutter.full_name}}",
 author_email="{{cookiecutter.email}}",
 py_modules=['{{cookiecutter.project_slug}}'],
 install_requires=["snakemake=={{cookiecutter.snakemake_version}}",
                   "pyyaml=={{cookiecutter.pyyaml_version}}",
                   "Click=={{cookiecutter.click_version}}"],
 entry_points={
  'console_scripts': [
    '{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.__main__:main'
  ]},
 include_package_data=True,
)
