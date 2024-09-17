from setuptools import find_packages, setup

setup(
    name="dagster_dlt_staging",
    packages=find_packages(exclude=["dagster_dlt_staging_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
