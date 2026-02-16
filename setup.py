from setuptools import setup, find_packages

setup(
    name="deleteme",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "aiohttp",
        "fpdf2",
    ],
    entry_points={
        "console_scripts": [
            "deleteme=deleteme.engine:scan",
        ],
    },
)