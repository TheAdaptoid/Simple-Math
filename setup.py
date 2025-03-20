from setuptools import setup, find_packages

setup(
    name="simple-math",
    version="1.0.1",
    packages=find_packages(exclude=["tests"]),
    install_requires=[],
    url="https://github.com/TheAdaptoid/Simple-Math",
    author="Marion Forrest",
    author_email="111011653+TheAdaptoid@users.noreply.github.com",
    description="Simple Math is a collection of functions for performing basic mathematical operations.",
    long_description="README.md",
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
