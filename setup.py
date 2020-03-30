from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sku",
    version="0.2",
    description="scikit-learn Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mythologic/sku",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    packages=["sku"],
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
