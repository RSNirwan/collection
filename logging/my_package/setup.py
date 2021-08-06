import setuptools


setuptools.setup(
    name="my_package",
    version="0.0.0",
    author="Rajbir Singh Nirwan",
    author_email="rajbir.nirwan@gmail.com",
    description="logging",
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[
    ],
    extras_require={
        "dev": [
        ],
    },
)

