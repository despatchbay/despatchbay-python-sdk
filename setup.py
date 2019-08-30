import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="despatchbay",
    version="0.5.3",
    author="Despatch Bay",
    author_email="scott.keenan@thesalegroup.co.uk",
    description="Python SDK for the Despatch Bay API v15",
    install_requires=['suds-py3', 'requests'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://test.pypi.org/project/despatchbay/",
    packages=setuptools.find_namespace_packages(include=['despatchbay']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
