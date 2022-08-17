"""Setup file for package."""
import setuptools

setuptools.setup(
    name="aion",
    version="1.0.0",
    author="Chris Reusch",
    description="Scheduler for python tasks.",
    packages=["aion"],
    install_requires=[
        "cron_converter",
    ],
)
