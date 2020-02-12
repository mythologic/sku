from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="itemvec",
    version="0.0.1",
    description="🔨 Item Vectorizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maxhumber/itemvec",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    py_modules=["itemvec"],
    install_requires=["scipy", "numpy"],
    python_requires=">=3.6",
    setup_requires=["setuptools>=38.6.0"],
)
