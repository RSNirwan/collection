from setuptools import find_packages, setup


setup(
    name="ptut",
    version="0.0.0",
    packages=find_packages(where="src", exclude=("test",)),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=["pandas"],
    extras_require={
        "dev": ["pytest"],
    },
)
