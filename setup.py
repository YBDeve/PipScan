from setuptools import setup, find_packages

setup(
    name="pipscan",
    version="1",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author="YB",
    description="A Python Library used for network port scanning. Choose between single scanning and multi scanning.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YBDeve/PipScan",
    license="MIT",
)


