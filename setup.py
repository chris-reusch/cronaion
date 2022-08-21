"""Setup file for package."""
import setuptools

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="cronaion",
    version="1.0.4",
    author="Chris Reusch",
    description="Scheduler for python tasks.",
    packages=["cronaion"],
    install_requires=[
        "cron_converter",
    ],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
