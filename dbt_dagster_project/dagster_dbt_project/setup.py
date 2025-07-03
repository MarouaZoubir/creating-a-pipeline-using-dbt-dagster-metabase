from setuptools import find_packages, setup

setup(
    name="dagster_dbt_project",
    packages=find_packages(exclude=["dagster_dbt_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
