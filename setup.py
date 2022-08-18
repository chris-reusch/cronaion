"""Setup file for package."""
import setuptools

setuptools.setup(
    name="cronaion",
    version="1.0.1",
    author="Chris Reusch",
    description="Scheduler for python tasks.",
    packages=["cronaion"],
    install_requires=[
        "cron_converter",
    ],
)
