from setuptools import setup, find_packages

setup(
    name="sro_sto_plume",  # Replace with your package name
    version="0.1",
    description="Repository for SRO_STO_Plume project",
    author="Yichen Guo",
    package_dir={"": "src"},
    packages=find_packages(where="src"),  # Finds packages inside 'src'
    install_requires=[],  # Add dependencies if needed, e.g., ['numpy']
)
