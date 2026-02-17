from setuptools import setup, find_packages

setup(
    name="Topsis-Kalpesh-102317087",
    version="1.0.2",
    author="Kalpesh",
    description="TOPSIS implementation as a Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        "console_scripts": [
            "topsis = topsis_Kalpesh_102317087.topsis:main"
        ]
    },
)
