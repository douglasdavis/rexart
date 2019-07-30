from setuptools import setup
from setuptools import find_packages
import os


with open("requirements.txt") as f:
    requirements = f.read().splitlines()


with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"), "rb") as f:
    long_description = f.read().decode("utf-8")


setup(
    name="rexplotlib",
    version="0.0.1",
    scripts=[],
    packages=find_packages(exclude=["tests"]),
    entry_points={"console_scripts": ["rexpl = rexplotlib._app:cli"]},
    description="Plot TRExFitter results with matplotlib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Doug Davis",
    author_email="ddavis@ddavis.io",
    license="MIT",
    test_suite="tests",
    python_requires=">=3.7",
    install_requires=requirements,
    tests_require=["pytest>=4.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
    ],
)
