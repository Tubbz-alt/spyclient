import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='spyclient',  
    version='1.0',
    packages=['spyclient'],
    author="sam210723",
    author_email="pypi@vksdr.com",
    description="Airspy SpyServer client implementation for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sam210723/spyclient",
    install_requires = [],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Communications :: Ham Radio"
    ],
)
