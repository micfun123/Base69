from setuptools import setup, find_packages

VERSION = "0.2.2"
DESCRIPTION = "Base 69 encoder and decoder"

setup(
    name="Base_69",
    version=VERSION,
    author="Michael Parker",
    author_email="michaelrbparker@protonmail.com",
    url="https://github.com/micfun123/Base69",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
)

# python3 setup.py bdist_wheel
# twine upload dist/*
# sudo rm -rf ./build ./dist ./*egg-info
