from setuptools import setup, find_packages
from pathlib import Path

long_description = (Path(__file__).parent / "README.md").read_text()

setup(
    name="fh-altair",
    description="Make is easy to use altair in FastHTML",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vincent D. Warmerdam",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["altair", "python-fasthtml"],
    extras_require={
        "dev": ["pytest", "pandas"],
    },
)
